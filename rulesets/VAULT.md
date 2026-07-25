# Vault CLI rules

## Context and purpose

These rules are designed for operations with HashiCorp Vault CLI in environments managed by Rodrigo Álvarez, particularly for tasks related to secure authentication, secret management, and DevOps operations within distributed infrastructure.

## Initial configuration

### Environment variables

```bash
# Vault server URL
export VAULT_ADDR="https://vault.example.com:8200"

# Authentication token (use secure variables)
export VAULT_TOKEN="$(cat ~/.vault-token)"

# Default namespace (if applicable)
export VAULT_NAMESPACE="kv"
```

### Authentication

```bash
# Interactive authentication
vault auth -method=userpass username=incognia

# Verify authentication status
vault auth -method=token -verify

# Renew token
vault token renew
```

## Standard path structure

### Namespace: kv (Key-Value v2)

| Path | Purpose | Format |
|------|---------|--------|
| `kv/incognia/passwords` | Credentials and temporary passwords | JSON with fields: `username`, `password`, `expires` |
| `kv/incognia/ssh` | Private and public SSH keys | JSON with fields: `private_key`, `public_key`, `comment` |
| `kv/incognia/tokens` | API tokens and external service tokens | JSON with fields: `token`, `service`, `expires`, `scope` |
| `kv/incognia/certificates` | SSL/TLS certificates | JSON with fields: `cert`, `key`, `ca`, `expires` |
| `kv/incognia/database` | Database credentials | JSON with fields: `host`, `port`, `username`, `password`, `database` |
| `kv/incognia/kubernetes` | Kubernetes secrets | JSON with fields: `kubeconfig`, `token`, `namespace` |

## Basic operations

### Secret management

```bash
# List secrets at a path
vault kv list kv/incognia/

# Create/update secret
vault kv put kv/incognia/passwords/myapp username="admin" password="secure123" expires="2025-12-31T23:59:59Z"

# Read secret (table format)
vault kv get kv/incognia/passwords/myapp

# Read secret (JSON format)
vault kv get -format=json kv/incognia/passwords/myapp

# Delete specific version
vault kv delete -versions=1,2 kv/incognia/passwords/myapp

# Permanently destroy
vault kv destroy -versions=1 kv/incognia/passwords/myapp

# Undo deletion
vault kv undelete -versions=1 kv/incognia/passwords/myapp
```

### Secret versioning

```bash
# View version history
vault kv metadata get kv/incognia/passwords/myapp

# Read specific version
vault kv get -version=2 kv/incognia/passwords/myapp

# Configure maximum retention
vault kv metadata put -max-versions=5 kv/incognia/passwords/myapp
```

## SSH key processing

### Downloading and formatting SSH keys

Keys stored in `kv/incognia/ssh` require post-processing with `jq` to extract them correctly from the JSON output.

```bash
# Extract private SSH key
vault kv get -format=json kv/incognia/ssh/mykey | jq -r '.data.data.private_key' > ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa

# Extract public SSH key
vault kv get -format=json kv/incognia/ssh/mykey | jq -r '.data.data.public_key' > ~/.ssh/id_rsa.pub
chmod 644 ~/.ssh/id_rsa.pub

# Extract both keys in a single command
vault kv get -format=json kv/incognia/ssh/mykey | \
  jq -r '.data.data |
    "\(.private_key)" > "~/.ssh/id_rsa",
    "\(.public_key)" > "~/.ssh/id_rsa.pub"'
```

### SSH key validation

```bash
# Validate private key format
ssh-keygen -y -f ~/.ssh/id_rsa > /dev/null && echo "Clave privada válida" || echo "Clave privada inválida"

# Verify match between private and public key
ssh-keygen -y -f ~/.ssh/id_rsa | diff - ~/.ssh/id_rsa.pub
```

## Token and credential management

### API tokens

```bash
# Store API token
vault kv put kv/incognia/tokens/github \
  token="ghp_xxxxxxxxxxxxxxxxxxxx" \
  service="GitHub API" \
  expires="2025-12-31T23:59:59Z" \
  scope="repo,admin:org"

# Extract token for use in scripts
GITHUB_TOKEN=$(vault kv get -format=json kv/incognia/tokens/github | jq -r '.data.data.token')
export GITHUB_TOKEN
```

### Database credentials

```bash
# Store PostgreSQL credentials
vault kv put kv/incognia/database/postgresql \
  host="postgres.example.com" \
  port="5432" \
  username="dbadmin" \
  password="secure_password" \
  database="production"

# Extract credentials for connection
DB_HOST=$(vault kv get -format=json kv/incognia/database/postgresql | jq -r '.data.data.host')
DB_USER=$(vault kv get -format=json kv/incognia/database/postgresql | jq -r '.data.data.username')
DB_PASS=$(vault kv get -format=json kv/incognia/database/postgresql | jq -r '.data.data.password')
```

## Kubernetes integration

### kubeconfig management

```bash
# Store kubeconfig
vault kv put kv/incognia/kubernetes/cluster1 \
  kubeconfig="$(cat ~/.kube/config | base64 -w 0)" \
  namespace="production" \
  context="cluster1-admin"

# Restore kubeconfig
vault kv get -format=json kv/incognia/kubernetes/cluster1 | \
  jq -r '.data.data.kubeconfig' | base64 -d > ~/.kube/config
chmod 600 ~/.kube/config
```

## Security best practices

### Token management

1. **Regular rotation**: rotate tokens every 30–90 days
2. **Principle of least privilege**: grant only the minimum necessary permissions
3. **Audit**: regularly review secret access

```bash
# Create token with limited TTL
vault token create -ttl=24h -display-name="temp-access"

# Verify current token capabilities
vault token capabilities kv/incognia/passwords/myapp
```

### Access policies

```bash
# View policies assigned to the current token
vault token lookup -format=json | jq -r '.data.policies[]'

# Verify a specific policy
vault policy read incognia-dev
```

## Automation and scripting

### Backup scripts

```bash
#!/bin/bash
# backup-vault-secrets.sh

BACKUP_DIR="/backup/vault/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

# Respaldar todos los secretos del namespace incognia
for path in $(vault kv list -format=json kv/incognia/ | jq -r '.[]'); do
    vault kv get -format=json "kv/incognia/$path" > "$BACKUP_DIR/${path}.json"
done

echo "Respaldo completado en: $BACKUP_DIR"
```

### Secret validation

```bash
#!/bin/bash
# validate-secrets.sh

# Verificar que los secretos críticos existen
CRITICAL_SECRETS=(
    "kv/incognia/database/postgresql"
    "kv/incognia/ssh/admin"
    "kv/incognia/tokens/github"
)

for secret in "${CRITICAL_SECRETS[@]}"; do
    if vault kv get "$secret" >/dev/null 2>&1; then
        echo "✓ $secret - OK"
    else
        echo "✗ $secret - MISSING"
        exit 1
    fi
done
```

## Monitoring and auditing

### Diagnostic commands

```bash
# Vault server status
vault status

# Current token information
vault token lookup

# List secret mounts
vault secrets list

# View audit logs (requires admin permissions)
vault audit list
```

### Metrics and usage

```bash
# KV store usage statistics
vault kv metadata get kv/incognia/ | grep -E "(created_time|updated_time|version)"

# List secrets by modification date
vault kv list -format=json kv/incognia/ | \
  jq -r '.[] | select(length > 0)' | \
  while read -r secret; do
    echo "$secret: $(vault kv metadata get kv/incognia/$secret | grep updated_time)"
  done
```

## Common troubleshooting

### Authentication errors

```bash
# Expired token
vault token renew || vault auth -method=userpass username=incognia

# Verify connectivity
curl -k "$VAULT_ADDR/v1/sys/health"
```

### Permission issues

```bash
# Verify current user's policies
vault token lookup -format=json | jq '.data.policies'

# Test access to a specific path
vault kv get kv/incognia/test 2>&1 | grep -q "permission denied" && \
  echo "Sin permisos" || echo "Acceso permitido"
```

---

*This document was developed by Rodrigo Álvarez for secure secret management in DevOps infrastructure and is distributed under the MIT licence. For further details, see the LICENSE file.*

*Copyright © 2026, Rodrigo Ernesto Álvarez Aguilera (@incogniadev).*
