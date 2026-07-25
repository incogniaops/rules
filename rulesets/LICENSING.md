# Formal licensing rules for complete projects

## 1. Purpose

This document establishes the guidelines for creating a formal LICENSE file in projects that contain multiple documents and/or scripts, ensuring legal and philosophical consistency.

## 2. Licence selection by project type

### 2.1. Corporate projects
- **Recommended licence:** MIT
- **Reason:** Permissive nature that facilitates integration and commercial adoption.

### 2.2. Personal projects (software)
- **Recommended licence:** GNU GPLv3
- **Reason:** Ensures that the code and derivatives remain free, promoting *copyleft*.

(Can apply to both personal and corporate projects, depending on the specific needs of the project)

### 2.3. Hardware design projects
- **Standard licence:** CERN OHL v2
- **Reason:** Allows free modification and distribution within the open hardware domain.

### 2.4. Documentation projects
- **Licence:** GNU LGPLv3
- **Alternative:** Creative Commons for general documents not tied to software.

### 2.5. Creative projects
- **Standard licence:** CC BY 4.0
- **Reason:** Facilitates maximum dissemination and use, requiring only attribution.

## 3. Application examples

The following examples show how to include licensing and authorship information in different types of files, using the information defined in the attribution document.

### 3.1. Markdown footer (README.md)

#### Corporate project

---

*Este proyecto fue elaborado por Rodrigo Álvarez para Promad Business Solutions y se distribuye bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.*

*Copyright © 2026, Rodrigo Ernesto Álvarez Aguilera (@incogniadev).*

#### Personal project

---

*Este proyecto fue elaborado por Rodrigo Álvarez (@incognia) y se distribuye bajo la licencia GPLv3. Para más detalles, consulta el archivo LICENSE.*

*Copyright © 2026, Rodrigo Ernesto Álvarez Aguilera. Este es software libre bajo los términos de la GNU General Public License v3.*

### 3.2. Header in a Bash script (.sh)

#### Corporate project

```bash
#!/bin/bash
#
# Script:         k8s-cluster-bootstrap.sh
# Descripción:    Automatiza el aprovisionamiento de clústeres Kubernetes en Proxmox VE.
# Autor:          Rodrigo Álvarez <ralvarez@kabatone.com>
# Fecha:          2026-01-23
# Licencia:       MIT License
#
# Copyright (c) 2026, Promad Business Solutions
#
# Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
# de este software y de los archivos de documentación asociados (el "Software"), para tratar
# en el Software sin restricción, incluyendo sin limitación los derechos
# para usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar, y/o vender
# copias del Software, y para permitir a las personas a las que se les proporcione el Software
# hacerlo, sujeto a las siguientes condiciones:
#
# El aviso de copyright anterior y este aviso de permiso se incluirán en todas
# las copias o porciones sustanciales del Software.

# ... rest of the script code ...
```

#### Personal project

```bash
#!/bin/bash
#
# Script:         istio-observability-stack.sh
# Descripción:    Despliega stack de observabilidad con Prometheus, Grafana y Jaeger en Istio.
# Autor:          Rodrigo Álvarez (incognia) <incognia@gmail.com>
# Fecha:          2026-01-23
# Licencia:       GNU General Public License v3.0 (GPLv3)
#
# Copyright (c) 2026 Rodrigo Ernesto Álvarez Aguilera
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General de GNU publicada por
# la Free Software Foundation, ya sea la versión 3 de la Licencia, o
# (a su elección) cualquier versión posterior.
#
# Este programa se distribuye con la esperanza de que sea útil, pero
# SIN NINGUNA GARANTÍA; ni siquiera la garantía implícita de
# COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General de GNU para más detalles.
#
# Debería haber recibido una copia de la Licencia Pública General de GNU
# junto con este programa. Si no es así, consulte <https://www.gnu.org/licenses/>.

# ... rest of the script code ...
```

### 3.3. Header in a Python script (.py)

#### Corporate project

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File:         database_backup.py
# Description:  Automated database backup tool for production environments.
# Author:       Rodrigo Álvarez <ralvarez@kabatone.com>
# Date:         2026-01-23
# License:      MIT License
#
# Copyright (c) 2026, Promad Business Solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

"""
Automated database backup tool for Promad Business Solutions.

This module provides functionality to create automated backups of
PostgreSQL and MySQL databases with configurable retention policies.
"""

# ... rest of the script code ...
```

#### Personal project

```python
# -*- coding: utf-8 -*-
#
# autor:    Rodrigo Álvarez (incognia)
# correo:   incognia@gmail.com
# fecha:    2026-01-23
# licencia: GNU General Public License v3.0 (GPLv3)
#
# Copyright (c) 2026 Rodrigo Ernesto Álvarez Aguilera
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General de GNU publicada por
# la Free Software Foundation, ya sea la versión 3 de la Licencia, o
# (a su elección) cualquier versión posterior.
#
# Este programa se distribuye con la esperanza de que sea útil, pero
# SIN NINGUNA GARANTÍA; ni siquiera la garantía implícita de
# COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General de GNU para más detalles.
#
# Debería haber recibido una copia de la Licencia Pública General de GNU
# junto con este programa. Si no es así, consulte <https://www.gnu.org/licenses/>.

"""
Módulo de ejemplo para demostrar la inclusión de la licencia GPLv3.
"""

# ... rest of the script code ...
```

### 3.4. Kubernetes, GitOps, and Helm manifests

#### Corporate project — Argo CD Application

```yaml
# production-app.yaml
# Argo CD Application para desplegar la aplicación 'webapp-backend' en producción
#
# Author: Rodrigo Álvarez <ralvarez@kabatone.com>
# License: MIT
# Company: Promad Business Solutions
#
# Copyright (c) 2026, Promad Business Solutions

apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: webapp-backend-prod
  namespace: argocd
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: production-apps
  source:
    repoURL: 'https://git.promad.com.mx/devops/webapp-backend.git'
    targetRevision: HEAD
    path: helm/
  destination:
    server: 'https://kubernetes.default.svc'
    namespace: prod-services
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

#### Personal project — Helm Chart

```yaml
# Chart.yaml
# Helm chart para stack de observabilidad con OpenTelemetry
#
# Autor: Rodrigo Álvarez (incognia)
# Licencia: GPL-3.0-or-later
# Repositorio: https://github.com/incognia/observability-stack
#
# Copyright (C) 2026 Rodrigo Ernesto Álvarez Aguilera

apiVersion: v2
name: observability-stack
description: |
Stack completo de observabilidad con Prometheus, Grafana,
  OpenTelemetry y Jaeger para clústeres Kubernetes.
  Este chart está bajo GPL-3.0: software libre para la comunidad.

type: application
version: 0.1.0
appVersion: "1.0.0"
maintainers:
  - name: Rodrigo Álvarez
    email: incognia@gmail.com
    url: https://github.com/incognia
```

## 4. Best practices

### 4.1. Required LICENSE files

- **Public projects:** always include a `LICENSE` file at the repository root with the full text of the chosen licence.
- **Git repositories:** ensure the `LICENSE` file is versioned and available from the first *commit*.

### 4.2. Headers in source files

- **Consistency:** use the same header format in all files within the project.
- **Minimum information:** author, date, licence, and *copyright*.
- **Contact:** include email address or GitHub/GitLab username depending on context (personal vs corporate).

### 4.3. Documentation

- **README.md:** explicitly mention the licence used and reference the `LICENSE` file.
- **CHANGELOG.md:** does not require licence information, but must maintain authorship attribution.

### 4.4. Licence compatibility

- **Corporate projects (MIT):** compatible with most open-source and proprietary licences.
- **Personal projects (GPLv3):** requires all derivative works to maintain the same licence (*copyleft*).
- **External dependencies:** verify compatibility before integrating third-party libraries.

### 4.5. Attribution in collaborative projects

- **Multiple authors:** list all contributors in an `AUTHORS` or `CONTRIBUTORS` file.
- **Minor contributions:** maintain the original attribution, add contributors in comments or documentation.

---

*Written by Rodrigo Álvarez (@incognia)*
