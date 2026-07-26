# Educational and science outreach profile of Rodrigo Álvarez

*English translation of [ENSEÑANZA.md](./ENSEÑANZA.md) — the Spanish source is canonical.*

> This educational profile is grounded in [PHILOSOPHY.md](../PHILOSOPHY.md). For a general overview and quick navigation, see [README.md](../README.md).

## Educational summary

DevOps engineer specialised in the **application of modern software engineering methodologies and tools to STEM education**. With 8 years of teaching experience, I combine advanced technical knowledge in DevOps with practical pedagogy to create immersive and reproducible learning environments.

My approach goes beyond traditional teaching: I use infrastructure-as-code principles, automation, and containerisation to democratise access to professional development tools in the classroom.

## Educational philosophy

My pedagogical approach is grounded in clear, non-negotiable principles:

- **Hands-on learning:** practical experience is fundamental to effective learning in STEM
- **Reproducible environments:** every student must have access to the same professional tools and configurations
- **Technology as a facilitator:** DevOps tools remove technical barriers and allow learners to focus on the subject matter
- **Commitment to free software:** in primary and secondary education (primary school, secondary school, and sixth form) its use is exclusive on ethical and pedagogical grounds. Outside higher education there is no technical or pedagogical justification for using proprietary software; its presence usually reflects the habits of teachers on closed platforms, not the actual needs of students.
- **Cross-platform competence:** teaching on Linux, Windows, and macOS to develop versatile, adaptable professionals

---

## Cross-cutting principles

- **Bilingual policy (aligned with PHILOSOPHY.md):** reasoning, documentation, and comments are written in Mexican Spanish; identifiers, filenames, and code are kept in international English where interoperability requires it.
- **Infrastructure as code and reproducibility:** laboratory and content configuration is defined declaratively to guarantee identical environments.
- **Accessibility and zero barriers:** access does not depend on closed platforms or restrictive licences.
- **Correct timestamps (CST, México City):** when timestamps are included in examples or logs, they are calculated with `TZ=America/Mexico_City` in 24-hour format.

## Specialisation in STEM education

### Innovative pedagogical methodologies

- **Educational infrastructure as code:** use of Docker Compose to orchestrate personalised learning environments
- **Educational automation:** Python scripts for automated distribution of exercises and assignments
- **Containerised environments:** JupyterLab deployed in Docker containers to guarantee consistency
- **Configuration management:** persistent volumes to preserve student progress
- **Administration panel:** web interfaces for simplified access and laboratory monitoring

### Technical tools in the classroom

| Category | Tools |
|----------|-------|
| **Containerisation** | Docker, Docker Compose |
| **Automation** | Python scripts, Bash scripts |
| **Development environment** | JupyterLab, VS Code, Neovim |
| **Infrastructure** | Linux (Debian/Ubuntu), SSH, persistent volumes |
| **Monitoring** | web panel (Node.js), htop, container logs |
| **Content distribution** | Git, symbolic links, automated deployment |

---

## Core educational competencies

### STEM curriculum design

- **Python programming:** from basic concepts to intermediate algorithms
- **Hands-on methodology:** 80% practical, 20% theory
- **Structured progression:** 21 lessons organised by increasing complexity
- **Continuous assessment:** interactive exercises in Jupyter Notebooks

### Technology laboratory management

- **Multi-container administration:** simultaneous management of 20+ student environments
- **Real-time problem-solving:** resolution of connectivity, permissions, and configuration issues
- **Automated maintenance:** Bash/Python scripts for cleaning, updating, and backing up environments
- **Resource monitoring:** oversight of CPU, memory, and storage

### Technological adaptation

- **Multi-distribution compatibility:** Ubuntu, Debian, Fedora, RHEL
- **Automated installation:** scripts that detect and configure dependencies per distribution
- **Cultural localisation:** JupyterLab in Mexican Spanish, bilingual code comments
- **Accessibility:** responsive web interfaces, clear documentation

### Cross-platform philosophy

**Pedagogical principle:** although I maintain a personal and professional preference for Linux, my educational approach aims to develop students who are competent on all three main platforms: Linux, Windows, and macOS, prioritised in that specific order.

**The tools analogy:** technical competence transcends brand preferences. If I need a screwdriver to do a job, it would be absurd to refuse to work until I found a specific brand. A competent professional can use any quality tool to complete their work. Personally I prefer iFixit precision screwdrivers, but that preference must not prevent me from removing a screw with a different brand's tool.

**Application to operating systems:** the same principle applies to computers. If you truly master computing, the operating system must not be an obstacle to getting your work done. Real technical competence is demonstrated by the ability to adapt and remain productive regardless of the available platform.

**Pedagogical approach by platform:**

1. **Linux (personal and professional preference):**
   - Base system for all educational laboratories and projects
   - Emphasis on Debian/Ubuntu distributions for consistency
   - Teaching Unix principles and system administration

2. **Windows (workplace reality):**
   - Recognition of its prevalence in corporate environments
   - Mandatory teaching of WSL (Windows Subsystem for Linux)
   - WSL as a bridge to Unix environments without leaving Windows

3. **macOS (last resort, with critical analysis):**
   - Discussion of the artificial premium pricing of Apple devices
   - Ethical analysis of closed platforms and development restrictions
   - Practical teaching despite philosophical reservations

## Outstanding educational projects

### Juno | JupyterLab-Based STEM Learning Environment

**Description:** Immersive STEM learning environment for secondary school students (ages 12–15) using JupyterLab deployed via Docker Compose.

**Technical features:**

- **Automated orchestration:** Python script generates personalised `compose.yaml` files based on the student list
- **Scalability:** automatic assignment of SSH ports (1022, 1122, 1222…) and JupyterLab ports (1088, 1188, 1288…)
- **Data persistence:** Docker volumes to preserve SSH configurations and student home directories
- **Content distribution:** automated script to copy Jupyter notebooks to all containers
- **Web panel:** Node.js interface for simplified access and container monitoring

**Educational impact:**

- Removed technical barriers to installation and configuration
- Enabled 100% focus on Python programming
- Identical environments for all students
- Persistence of student work between sessions

**Acknowledgements:** Inspired by the work of Serena Bonaretti ([Learn Python with Jupyter](https://learnpythonwithjupyter.com/))

### Chicxulub | Post-Apocalyptic Programming

**Description:** Science outreach project combining Python programming and geophysics to teach cartography and navigation concepts using the Chicxulub crater as a case study.

**Educational features:**

- **Interdisciplinarity:** fusion of programming, mathematics, geography, and Earth sciences
- **Historical contextualisation:** use of the K-Pg extinction event as a narrative framework
- **Practical application:** conversion of geographic coordinates and distance calculations on the Earth's surface
- **Mathematical formulae:** application of geodetic equations in executable Python code
- **Hands-on methodology:** interactive exercises with real crater data

**Outreach impact:**

- Democratises concepts of geodesy and cartography through accessible programming
- Connects historical events (dinosaur extinction) with modern technical tools
- Teaches applied trigonometry through real-world use cases
- Bilingual documentation (Spanish / code in English) following professional standards

**Repository:** [github.com/incognia/Chicxulub](https://github.com/incognia/Chicxulub)

---

## Current teaching context

### Teaching experience

- **Years of experience:** 8 years in STEM education
- **Educational level:** secondary school and sixth form (ages 12–18)
- **Mode:** in-person with technical laboratories
- **Location:** México City
- **Language of instruction:** Mexican Spanish with technical terminology in English

### Pedagogical approaches

- **Montessori education:** application of self-directed learning principles, developing innate curiosity and self-motivation in a carefully prepared environment
- **Active secondary schools:** promotion of active student participation and co-creation of knowledge through collaborative projects and practical learning

### Social engagement

- **Educational programmes in vulnerable communities:** design and delivery of projects to provide accessible education to low-income populations using open technologies and inclusive methodologies
- **C++ teaching with Arduino:** focus on microcontroller programming for practical electronics and educational robotics projects

### Integration of experience and philosophy

Diverse experience in Montessori education, active secondary schools, and social programmes has enabled a deep understanding and application of knowledge-democratisation principles across varied contexts. By using free tools in these environments, every student — regardless of socioeconomic background — is guaranteed access to a quality education. This also fosters autonomy and self-directed learning, aligned with an educational philosophy that empowers students to be the protagonists of their own learning process.

### Outstanding students

- **Carlos (@cgzdev):** development of advanced features in collaborative projects
- **Ian (@calmestprism226):** significant contributions to automation and scripting
- **Fernando (@fer1495):** leadership in debugging and environment optimisation

### Quantitative impact

- **Environments deployed:** 100+ Docker containers managed
- **Students reached:** 60+ students over 8 years
- **Projects developed:** 20+ automated laboratories
- **Preparation time reduced:** from 2 hours to 5 minutes per student

---

## Science and technical outreach

### Outreach philosophy

- **Democratisation of knowledge:** professional tools accessible to students
- **Commitment to software freedom:** exclusive use of free tools (Linux, Docker, Python, JupyterLab) on ethical and pedagogical grounds
- **Open source:** all educational projects under the GPLv3 licence on ethical grounds
- **Comprehensive documentation:** detailed READMEs, step-by-step guides
- **Replicability:** fully reproducible environments across different infrastructures
- **Education in freedom:** teaching with tools that students can use, modify, and redistribute freely

### Community contributions

- **Project Juno:** free-software educational platform for programming instruction
- **DevOps methodologies in education:** application of engineering principles to pedagogy
- **Cultural adaptation:** localisation of technical tools for the Mexican context

### Impact on the educational community

- **Pedagogical inspiration:** methodology replicated by other educators
- **Ecosystem contribution:** project publicly available on GitHub
- **Technical mentoring:** development of new talent in DevOps and programming

---

**Main document:** [PHILOSOPHY.md](../PHILOSOPHY.md) · **Quick reference:** [README.md](../README.md)

## Evolution and continuous learning

### Constant technological adaptation

- **Tool updates:** version migration, adoption of new technologies
- **Student feedback:** incorporation of suggestions for continuous improvement
- **Best practices:** integration of new pedagogical and technical approaches

### Professional development

- **DevOps–Education intersection:** unique specialisation in applying software engineering to pedagogy
- **Educational research:** experimentation with new technical teaching methodologies
- **Academic collaboration:** joint work with educators and developers

---

*Written by Rodrigo Álvarez (@incognia)*
