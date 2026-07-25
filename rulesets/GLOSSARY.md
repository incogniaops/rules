# Technical glossary for Rodrigo Álvarez's projects

This glossary collects key terms used in the rules and development philosophy documents for personal and corporate projects. Its purpose is to reinforce consistency and clarity in the use of concepts within Rodrigo Álvarez's professional environment and community.

---

**Atom / Atomicity**
: principle by which each commit or contribution must have a single purpose and be self-contained, so that it can be isolated, understood, and reverted without affecting other changes.

**Argo CD**
: GitOps tool for continuous deployment management in Kubernetes clusters. Automates the synchronisation of declarative repository configuration with the actual cluster state.

**Bare-metal** (in *bare-metal*)
: direct physical infrastructure, without virtualisation; commonly refers to dedicated servers that are not under a hypervisor layer.

**CI/CD** (*Continuous Integration / Continuous Delivery*)
: practices and tools for automating the software integration and delivery cycle. Includes automated testing, building, and deployment of code across various environments.

**Changelog**
: file where each relevant change to the project is recorded chronologically, ensuring traceability and transparency for all involved parties.

**Chart (Helm Chart)**
: templates and configuration files used with the Helm tool to describe, manage, and install applications on Kubernetes.

**Cloud-init**
: automated initialisation system for cloud instances and virtual machines, customising configuration at boot time.

**Commit** (in *commit*)
: basic unit of contribution or change record in a version control system. Must be written in international English and concisely describe the purpose of the modification.

**Commons** (*commons*)
: resources and knowledge shared and maintained collectively by a community; here, refers especially to the free software ecosystem.

**Containerd**
: container runtime used by Kubernetes and other platforms to manage Linux containers in a standard and efficient manner.

**Copyleft**
: licensing philosophy and practice (e.g. GPLv3) that requires derivative works to retain the same licence and freedom rights as the original.

**Declarative / declarative automation**
: paradigm in which the desired state of the system is described explicitly, and tools implement it automatically (e.g. GitOps flows, YAML manifests).

**DevOps**
: culture and set of practices that seek to integrate development and operations teams to deliver software more efficiently, stably, and securely.

**Context duality (personal/corporate)**
: distinction between personal projects (GPLv3 licence, alias incognia) and corporate projects (MIT licence, alias incogniaops), each with specific rules and attribution.

**Emojis (in commits)**
: graphic icons that are strongly discouraged in commit messages and professional documentation within this system.

**GitOps flow**
: model in which all environment state is described and controlled via Git (infrastructure versioning), so that configuration changes are made through pull requests and traceable reviews.

**Helm**
: package manager for Kubernetes that simplifies the deployment and update of complex applications through templates called charts.

**Istio**
: service mesh for Kubernetes that provides advanced routing, load balancing, security, policy, and observability for microservices.

**Kubernetes**
: container orchestration platform for automating the deployment, management, and scaling of applications in distributed clusters.

**Manifest (manifest, YAML manifests)**
: configuration file in YAML/JSON format that describes the desired state of resources in Kubernetes, GitOps, or another declarative tool.

**Mermaid**
: text language and tool for creating dynamic diagrams and charts embedded in Markdown files.

**OpenTelemetry**
: standard for instrumenting, collecting, and exporting metrics, logs, and distributed traces in modern systems.

**Pipeline** (*pipeline*)
: automated sequence of steps for building, testing, or deploying software; managed by CI/CD tools.

**Network policies**
: rules implemented in Kubernetes, Istio, or other systems to control traffic between applications and prevent unauthorised access.

**Proxmox VE**
: open-source virtualisation platform based on KVM and LXC, used to deploy private infrastructure and bare-metal Kubernetes clusters.

**Elsevier**
: corporate entity associated with projects under the MIT licence and the professional alias incogniaops.

**RBAC (Role-Based Access Control)**
: security mechanism that restricts access to resources in Kubernetes and applications based on roles assigned to users or groups.

**Service mesh**
: architecture that introduces a dedicated network layer between microservices to manage traffic, metrics, and security without modifying the original services.

**Traceability**
: ability to track the origin, reason, and author of each change made to code, configurations, and documentation.

**YAML**
: data serialisation language widely used for configuration files, especially in DevOps and Kubernetes.

**Reasoning chain (Chain-of-Thought, CoT)**
: prompting technique for language models in which the model is asked to generate intermediate reasoning steps before giving the final answer. Improves performance on multi-step tasks (arithmetic, logic, technical diagnosis) and facilitates verification of units, assumptions, and dependencies. Best practices in this repository: reasoning in Mexican Spanish; identifiers/code in English where appropriate; numbered steps and a verifiable conclusion; no secrets included; use reference paths `~/rules/...`. See [`~/rules/PROMPTS.md`](./PROMPTS.md) and Wei et al. (arXiv:2201.11903).

---

*Written by Rodrigo Álvarez (@incognia)*

**For linguistic terms, see also [`~/rules/LINGUISTICS.md`](./LINGUISTICS.md)**
