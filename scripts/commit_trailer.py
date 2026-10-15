#!/usr/bin/env python3
"""Print a co-author trailer for the model running the active coding-agent session.

Supports Codex (CODEX_THREAD_ID or CODEX_SESSION_ID, CODEX_HOME) and Claude Code
(CLAUDE_CODE_SESSION_ID, CLAUDE_EFFORT). Reads only the active session; config
defaults and Git history are never used.
"""

import argparse
import json
import os
from pathlib import Path
import re
import sys

ID_RE = r"[A-Za-z0-9_-]+"
EFFORT_RE = r"[A-Za-z0-9][A-Za-z0-9_-]*"


def detect_tool():
    if os.environ.get("CODEX_THREAD_ID") or os.environ.get("CODEX_SESSION_ID"):
        return "codex"
    if os.environ.get("CLAUDE_CODE_SESSION_ID"):
        return "claude"
    raise ValueError("no active Codex or Claude Code session detected")


def valid_effort(effort):
    if effort is not None and (not isinstance(effort, str) or not re.fullmatch(EFFORT_RE, effort)):
        raise ValueError("active session has an invalid reasoning effort")
    return effort or None


def format_name(model, effort):
    return f"{model} ({effort})" if effort else model


# ---------------------------------------------------------------- Codex

def codex_context(sessions_dir, thread_id):
    """Return the latest turn context after verifying the session identity."""
    if not thread_id or not re.fullmatch(ID_RE, thread_id):
        raise ValueError("missing or invalid active Codex thread ID")
    matches = list(sessions_dir.rglob(f"*-{thread_id}.jsonl"))
    if len(matches) != 1:
        raise ValueError("expected exactly one session file for the active Codex thread")

    session_id = None
    context = None
    with matches[0].open(encoding="utf-8") as stream:
        for line in stream:
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                raise ValueError("active Codex session contains an incomplete or invalid record") from None
            if not isinstance(record, dict):
                continue
            payload = record.get("payload")
            if record.get("type") == "session_meta" and isinstance(payload, dict):
                session_id = payload.get("id")
            elif record.get("type") == "turn_context":
                context = payload
    if session_id != thread_id:
        raise ValueError("session metadata does not match the active Codex thread")
    if not isinstance(context, dict):
        raise ValueError("active Codex session has no readable turn context")
    return context


def codex_trailer(context):
    """Return (trailer, effort_known) without inferring missing model details."""
    mode = context.get("collaboration_mode")
    settings = mode.get("settings") if isinstance(mode, dict) else None
    if not isinstance(settings, dict):
        settings = {}
    model = context.get("model") or settings.get("model")
    if not isinstance(model, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:-]*", model):
        raise ValueError("latest Codex turn has no valid model identifier")
    effort = valid_effort(
        context.get("effort")
        or context.get("reasoning_effort")
        or context.get("model_reasoning_effort")
        or settings.get("reasoning_effort")
    )
    if model.startswith("gpt-"):
        model = "GPT-" + "-".join(part.capitalize() for part in model[4:].split("-"))
    return f"Co-Authored-By: {format_name(model, effort)} <noreply@openai.com>", bool(effort)


# ---------------------------------------------------------------- Claude Code

def claude_model(projects_dir, session_id):
    """Return the model of the latest main-thread assistant turn in the active session."""
    if not session_id or not re.fullmatch(ID_RE, session_id):
        raise ValueError("missing or invalid active Claude Code session ID")
    matches = list(projects_dir.glob(f"*/{session_id}.jsonl"))
    if len(matches) != 1:
        raise ValueError("expected exactly one transcript for the active Claude Code session")

    verified = False
    model = None
    with matches[0].open(encoding="utf-8") as stream:
        for line in stream:
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue  # the active transcript may end with a partially written line
            if not isinstance(record, dict):
                continue
            if record.get("sessionId") == session_id:
                verified = True
            if record.get("type") != "assistant" or record.get("isSidechain"):
                continue
            message = record.get("message")
            candidate = message.get("model") if isinstance(message, dict) else None
            if isinstance(candidate, str) and re.fullmatch(r"claude-[a-z0-9-]+", candidate):
                model = candidate
    if not verified:
        raise ValueError("transcript records do not match the active Claude Code session")
    if not model:
        raise ValueError("active Claude Code session has no assistant turn with a valid model")
    return model


def claude_display_name(model):
    """Turn 'claude-opus-5-5' into 'Claude Opus 5.5' (dated snapshot suffixes are dropped)."""
    parts = model.split("-")[1:]
    if parts and re.fullmatch(r"\d{8}", parts[-1]):
        parts = parts[:-1]
    words = [p.capitalize() for p in parts if not p.isdigit()]
    version = ".".join(p for p in parts if p.isdigit())
    if not words:
        raise ValueError(f"cannot derive a display name from model '{model}'")
    return " ".join(["Claude", *words, *([version] if version else [])])


def claude_trailer(model, effort):
    effort = valid_effort(effort)
    name = format_name(claude_display_name(model), effort)
    return f"Co-Authored-By: {name} <noreply@anthropic.com>", bool(effort)


# ---------------------------------------------------------------- CLI

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tool", choices=("codex", "claude"), help="force the tool instead of detecting it")
    parser.add_argument(
        "--sessions-dir",
        type=Path,
        default=Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex") / "sessions",
        help="Codex session storage (defaults to CODEX_HOME/sessions or ~/.codex/sessions)",
    )
    parser.add_argument(
        "--thread-id",
        default=os.environ.get("CODEX_THREAD_ID") or os.environ.get("CODEX_SESSION_ID"),
        help="Codex thread to inspect (defaults to the active Codex thread)",
    )
    parser.add_argument(
        "--projects-dir",
        type=Path,
        default=Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude") / "projects",
        help="Claude Code transcript storage (defaults to ~/.claude/projects)",
    )
    parser.add_argument(
        "--session-id",
        default=os.environ.get("CLAUDE_CODE_SESSION_ID"),
        help="Claude Code session to inspect (defaults to the active session)",
    )
    parser.add_argument(
        "--effort",
        default=os.environ.get("CLAUDE_EFFORT"),
        help="Claude Code effort (defaults to CLAUDE_EFFORT)",
    )
    args = parser.parse_args()
    try:
        tool = args.tool or detect_tool()
        if tool == "codex":
            trailer, effort_known = codex_trailer(codex_context(args.sessions_dir, args.thread_id))
        else:
            trailer, effort_known = claude_trailer(claude_model(args.projects_dir, args.session_id), args.effort)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"commit_trailer: {error}", file=sys.stderr)
        return 1
    if not effort_known:
        print("commit_trailer: reasoning effort unavailable; using the model alone", file=sys.stderr)
    print(trailer)
    return 0


if __name__ == "__main__":
    sys.exit(main())
