#!/usr/bin/env python3
"""Print a co-author trailer from the active Codex thread's latest turn.

Uses CODEX_THREAD_ID (or CODEX_SESSION_ID) and CODEX_HOME when available.
Reads only the matching session; config defaults and Git history are not used.
"""

import argparse
import json
import os
from pathlib import Path
import re
import sys


def session_context(sessions_dir, thread_id):
    """Return the latest turn context after verifying the session identity."""
    if not thread_id or not re.fullmatch(r"[A-Za-z0-9_-]+", thread_id):
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


def build_trailer(context):
    """Return (trailer, effort_known) without inferring missing model details."""
    mode = context.get("collaboration_mode")
    settings = mode.get("settings") if isinstance(mode, dict) else None
    if not isinstance(settings, dict):
        settings = {}
    model = context.get("model") or settings.get("model")
    if not isinstance(model, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:-]*", model):
        raise ValueError("latest Codex turn has no valid model identifier")
    effort = (
        context.get("effort")
        or context.get("reasoning_effort")
        or context.get("model_reasoning_effort")
        or settings.get("reasoning_effort")
    )
    if effort is not None and (
        not isinstance(effort, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", effort)
    ):
        raise ValueError("latest Codex turn has an invalid reasoning effort")
    if model.startswith("gpt-"):
        model = "GPT-" + "-".join(part.capitalize() for part in model[4:].split("-"))
    name = f"{model} ({effort})" if effort else model
    return f"Co-Authored-By: {name} <noreply@openai.com>", bool(effort)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sessions-dir",
        type=Path,
        default=Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex") / "sessions",
        help="session storage directory (defaults to CODEX_HOME/sessions or ~/.codex/sessions)",
    )
    parser.add_argument(
        "--thread-id",
        default=os.environ.get("CODEX_THREAD_ID") or os.environ.get("CODEX_SESSION_ID"),
        help="thread to inspect (defaults to the active Codex thread)",
    )
    args = parser.parse_args()
    try:
        trailer, effort_known = build_trailer(session_context(args.sessions_dir, args.thread_id))
    except (OSError, UnicodeError, ValueError) as error:
        print(f"codex_commit_trailer: {error}", file=sys.stderr)
        return 1
    if not effort_known:
        print("codex_commit_trailer: reasoning effort unavailable; using the model alone", file=sys.stderr)
    print(trailer)
    return 0


if __name__ == "__main__":
    sys.exit(main())
