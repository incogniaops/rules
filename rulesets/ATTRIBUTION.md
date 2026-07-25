# Personal attribution rules

## 1. Purpose

This document establishes how to credit and attribute authorship in individual documents, scripts, or files that do not require a full LICENSE file. For projects with multiple files requiring formal licensing, see **[LICENSING.md](./LICENSING.md)**.

## 2. Author identity

### 2.1. Full name
- **Legal name:** Rodrigo Ernesto Álvarez Aguilera

### 2.2. Common names
- **Short name:** Rodrigo Álvarez
- **Primary surname for indexing:** Álvarez

### 2.3. Naming convention
- **Spanish-speaking context:** two surnames are used — paternal «Álvarez» and maternal «Aguilera».
- **Technical and international context:** to ensure correct attribution in systems that do not handle compound names, use «Álvarez» as the primary surname.
- **Mandatory exception:** the surname is always written as «Álvarez» in documentation and text, including in English.

## 3. Professional specialisation

Rodrigo is **Systems Engineering Lead at Elsevier**, specialised in native Kubernetes platforms, GitOps, and advanced observability. With experience building and operating full stacks on bare-metal infrastructure, focused on automation, reliability, and service meshes.

Key technical competencies:

- **Bare-metal Kubernetes platforms:** building and operating clusters on Proxmox VE, provisioning with kubeadm and cloud-init
- **GitOps and declarative automation:** implementing workflows with Argo CD, managing Helm charts and versioned manifests
- **Service mesh and advanced networking:** configuring Istio, Envoy, Cilium, MetalLB, bridges, and VLANs
- **Observability and distributed tracing:** instrumentation with OpenTelemetry, Prometheus, Grafana, Fluentd, and Elasticsearch
- **Enterprise CI/CD:** designing pipelines with Jenkins and GitLab CI integrated into GitOps workflows
- **Service mesh security:** implementing mTLS, RBAC, and network policies in production environments

## 4. Digital identifiers

### 4.1. Personal
- **GitHub:** `incognia`
- **GitLab:** `incognia`
- **Email:** `incognia@gmail.com`

### 4.2. Corporate (Elsevier)
- **GitHub:** `incogniaops`
- **GitLab:** `incogniadev`
- **Email:** `r.alvarez1@elsevier.com`

## 5. Attribution and credits

### 5.1. Suggested formats
- **Personal contribution:** «created by Rodrigo Álvarez (@incognia)»
- **Technical documentation:** «documented by Rodrigo Ernesto Álvarez Aguilera (GitHub: @incognia)»
- **Corporate contribution:** «this work was carried out by Rodrigo Álvarez in his capacity as Systems Engineering Lead for Elsevier (@incogniaops)»

### 5.2. Git commit signature
- **For personal projects:**
  ```bash
  git config user.name "Rodrigo Álvarez"
  git config user.email "incognia@gmail.com"
  ```
- **For corporate projects (Elsevier):**
  ```bash
  git config user.name "Rodrigo Álvarez"
  git config user.email "r.alvarez1@elsevier.com"
  ```

## 6. Licensing and contribution signature

### 6.1. Licensing philosophy
- **Corporate/professional projects:** the licence to use is **MIT**, for its permissiveness and compatibility.
- **Personal projects:** licensing may vary, but the preference is for open-source licences such as MIT or Apache 2.0.

### 6.2. Contribution signature (alias)
- **Personal contributions:** sign under the alias `incognia`.
- **Corporate or contracted contributions:** sign under the alias `incogniaops`.
- **Legal requirements:** in licence headers or legal documents that require it, use the full name: `Rodrigo Ernesto Álvarez Aguilera`.

## 7. Coding and documentation standards

### 7.1. Language
- **Commit messages and code:** commit messages and inline code comments must be in **international English**.
- **Documentation (README, CHANGELOG, etc.):** the language is **Mexican Spanish**, unless the project context explicitly requires English. Titles and headings in Spanish follow sentence case (only the first word capitalised).
- **File and directory names:** always in **international English** to maintain technical consistency.

### 7.2. Commit messages
- **Convention:** follow the Conventional Commits specification.
- **Language:** write messages in English.
- **Format:** structure them with a prefix (`feat`, `fix`, `docs`, `refactor`, etc.).
- **Emojis:** do not use emojis.

### 7.3. Diagrams
For diagrams in Markdown files, use **Mermaid** exclusively.

---

*This document is intended for personal projects, detailing how to provide proper attribution without requiring a full licence file. For corporate projects or those with multiple scripts/documents, see **[LICENSING.md](./LICENSING.md)**.*

---

*Written by Rodrigo Álvarez (@incognia)*
