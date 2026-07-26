# Philosophy of a brown bastard who sometimes *codes* but always goes all in

*Last modified: 27 March 2026, 23:21 (CST)*

> «Technological development and scientific discoveries cannot be considered progress if they are not within everyone’s reach.»
>
> —Rodrigo Álvarez

Technology environments in Latin America suffer from three endemic issues that this manifesto confronts head-on:

- **Mercenary work:** professionals delivering mediocre output because they are only in it for the cash, with no real commitment to excellence or to the client.
- **Technical selfishness:** hoarding knowledge and tools to create artificial dependency, blocking others’ growth for purely economic interest.
- **Identity loss:** the insecure brown guy who speaks shitty English, writes with their ass, and bastardises his own Spanish in a desperate attempt to feel gringo.

Against these three issues, here is the answer: honest work, shared knowledge, and the satisfaction that comes from doing things properly, without insecurities and without bullshit.

This manifesto is not only about excelling in DevOps from the desk—where they call me «Agüelo» because I am a veteran, even though I stay as current as the latest *commit*—but also about applying that same philosophy in the classroom, where they say I look like Hagrid because I am big and bearded. Sure, mastering Kubernetes is awesome, but what's truly badass is sharing technical knowledge. We are not here to be code mercenaries hoarding secrets: we are here to teach without holding back, so everyone can master the tools that are genuinely worth it.

## 1. Coherent professional identity

This duality between being «Agüelo» and «Hagrid» is not accidental: it reflects a professional identity that operates across two complementary contexts, each with its own ecosystem but united by the same ethical principles.

### 1.1. Technical specialisation

My work is centred on **DevOps engineering**, focused on cloud-native Kubernetes platforms and advanced observability:

- **Kubernetes on Proxmox *bare-metal*:** provisioning with kubeadm, containerd, and cloud-init
- **GitOps and automation:** Argo CD workflows, Helm *charts*, and versioned manifests
- **Service mesh and networking:** Istio, Envoy, Cilium, MetalLB, bridge/VLAN configuration
- **Observability and traceability:** Prometheus, Grafana, OpenTelemetry, distributed tracing
- **Enterprise CI/CD:** Jenkins, GitLab CI with GitOps integration
- **Service mesh security:** mTLS, RBAC, and network policies

### 1.2. Application contexts

This technical specialisation is applied in two environments:

- **Corporate (`incogniaops`):** projects for Elsevier under MIT licensing
- **Personal and educational (`incognia`):** projects under GPLv3 and teaching methodologies that democratise access to professional tools

In both cases, DevOps methodologies support both production infrastructure and reproducible learning environments built with Docker Compose and automation.

## 2. Linguistic culture as a reference

### 2.1. Mexican Spanish as standard

All documentation is written in **Mexican Spanish** as a cultural reference, avoiding:

- English calques that do not sound natural
- Regionalisms from other Spanish variants
- Impersonal third-person constructions

### 2.2. Technical bilingualism

The theoretical approach states that code and *commit* messages should be written in **international English** to ensure global interoperability, while documentation uses Mexican Spanish to preserve cultural identity.

However, the reality of working in Mexican teams requires a pragmatic adaptation:

**Code comments:** although I have a B2 level of English approaching C1, my colleagues operate at A2 and B1 levels. To comply with **transparency and accessibility** principles, internal comments are written in Mexican Spanish, ensuring the whole team can understand and maintain the code without language barriers.

**Commit messages:** they remain in English for an additional practical reason: PMs and managers rarely read extended technical documentation. Their interaction with technical development is usually limited to checking a few *commits* (if they read them at all) or simply counting activity frequency in charts. English in *commits* maintains a professional standard in those surface-level reviews.

**Educational context:** most primary and secondary students in Mexico, regardless of whether they come from public or private schools, do not speak fluent English. We are geographically close neighbours to the U.S., but culturally still far away. This reality reinforces the importance of teaching in Mexican Spanish: democratising technical knowledge means making it accessible in the language our students actually command, not the one we think they should command.

## 3. Transparency and traceability

### 3.1. Clear change history

Every modification must have a single purpose and be documented in a way that allows:

- Understanding the *what* and the *why* of each change
- Preserving atomicity in contributions
- Facilitating future review and maintenance

### 3.2. Synchronized documentation

Update `CHANGELOG.md` **before** every *commit*, keeping documentation and code in sync.

## 4. Ethical and pragmatic licensing

### 4.1. Licensing philosophy

- **Work projects:** MIT to facilitate commercial integration.
- **Personal projects:** GPLv3 to preserve software freedom.
- **Hardware:** CERN OHL v2 for open designs.
- **Documentation:** LGPLv3 or Creative Commons depending on context.
- **Private projects:** case-by-case negotiation with each client.

### 4.2. Social responsibility

The chosen licences reflect a commitment to the free software ecosystem and respect for intellectual property, balancing commercial practicality with ethical principles.

## 5. Quality and consistency

### 5.1. Technical standards

- Adherence to recognised specifications (*Conventional Commits*).
- Use of standard tooling (Mermaid for diagrams).
- Consistency in structure and format.

### 5.2. Attention to detail

Small details are where excellence shows:

- Correct capitalisation in titles.
- Proper use of angular quotes in Spanish.
- Italics for technical loanwords.
- Avoiding emojis in professional contexts.

## 6. Evolution and adaptability

### 6.1. Living documents

These rules and philosophies are living documents that evolve with experience and changing technical needs.

### 6.2. Continuous learning

This philosophy incorporates lessons learned and emerging best practices, keeping a balance between stability and innovation.

## 7. Commitment to the community

### 7.1. Contribution to the ecosystem

Personal GPLv3 projects contribute to the free software *commons*, while work projects under MIT facilitate broad adoption.

## References

Specific implementation details of this philosophy are organised in the following documents (for a quick overview, see README.md):

### Universal rules (both contexts)

- **[LINGUISTICS.md](./rulesets/LINGUISTICS.md)** - Mexican Spanish linguistic rules as a reference
- **[COMMITTING.md](./rulesets/COMMITTING.md)** - rules for *commit* messages and change management
- **[BACKUPS.md](./rulesets/BACKUPS.md)** - backup and destructive-operation policies
- **[GIT.md](./rulesets/GIT.md)** - initial repository setup
- **[GLOSSARY.md](./rulesets/GLOSSARY.md)** - glossary of technical terms used
- **[CHANGELOG.md](./CHANGELOG.md)** - project change history
- **[AGENTS.md](./AGENTS.md)** - guide for AI agents

### Dual-use rules (context-dependent application)

- **[LICENSING.md](./rulesets/LICENSING.md)** - licensing rules for projects
- **[CORPORATE.md](./rulesets/CORPORATE.md)** - corporate professional profile
- **[TEACHING.md](./rulesets/TEACHING.md)** - educational and scientific outreach profile

### Personal-only rules

- **[ATTRIBUTION.md](./rulesets/ATTRIBUTION.md)** - personal attribution rules

### Work-only rules

- **[STYLING.md](./rulesets/STYLING.md)** - style rules for corporate Markdown documents

*This document was created by Rodrigo Álvarez (@incognia) and is distributed under the GPLv3 licence. For details, see the LICENSE file.*

*Copyright © 2026, Rodrigo Ernesto Álvarez Aguilera. This is free software under the terms of the GNU General Public License v3.*
