# CoT: Automatic licence application

## Context

This Chain of Thought automatically applies the appropriate licence to a project based on the rules defined in `../rulesets/LICENSING.md`. It determines whether the project is personal (GPL) or corporate (MIT) by analysing the content of README.md.

## Reasoning

### 1. Analysis of README.md

- **Objective:** determine the nature of the project (personal vs corporate)
- **Corporate indicators:** mentions of corporate entity, corporate email domain, business or enterprise language
- **Personal indicators:** mentions of personal user handle (@incognia), personal email (@gmail.com), learning or experimental projects

### 2. Licence selection

- **Corporate projects:** MIT Licence (permissive, facilitates commercial adoption)
- **Personal projects:** GNU GPLv3 (copyleft, keeps code free)

### 3. Licence application

- Create a LICENSE file with full licence text
- Add the appropriate footer to README.md
- Validate consistency with the project context

## Steps

### Step 1: Validate README.md existence

```bash
if [[ -f "README.md" ]]; then
    echo "✓ README.md found, analysing content..."
else
    echo "✗ README.md not found. Creating basic README..."
    # Request project information to create README
fi
```

### Step 2: Analyse project nature

```bash
# Look for corporate indicators
CORPORATE_INDICATORS=$(grep -i "@elsevier\.com\|elsevier\|incogniaops\|enterprise\|corporate\|business" README.md | wc -l)

# Look for personal indicators
PERSONAL_INDICATORS=$(grep -i "@incognia\|@gmail\.com\|personal\|experiment\|learning\|github\.com/incognia" README.md | wc -l)

if [[ $CORPORATE_INDICATORS -gt 0 ]]; then
    PROJECT_TYPE="corporate"
    LICENSE_TYPE="MIT"
    echo "Corporate project detected — applying MIT Licence"
elif [[ $PERSONAL_INDICATORS -gt 0 ]]; then
    PROJECT_TYPE="personal"
    LICENSE_TYPE="GPLv3"
    echo "Personal project detected — applying GPL v3"
else
    # Request manual confirmation
    echo "Project type ambiguous. Is it personal (p) or corporate (c)?"
fi
```

### Step 3: Generate LICENSE file

```bash
CURRENT_YEAR=$(date +%Y)

if [[ "$LICENSE_TYPE" == "MIT" ]]; then
    # Create MIT Licence
    cat > LICENSE << 'EOF'
MIT License

Copyright (c) YEAR ExampleCorp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

elif [[ "$LICENSE_TYPE" == "GPLv3" ]]; then
    # Download full GPL v3
    curl -s https://www.gnu.org/licenses/gpl-3.0.txt > LICENSE
fi
```

### Step 4: Add footer to README.md

```bash
# Remove existing footer if present
sed -i '/^---$/,$d' README.md

# Add new footer according to project type
if [[ "$PROJECT_TYPE" == "corporate" ]]; then
    cat >> README.md << 'EOF'

---

*This project was developed by Rodrigo Álvarez for the corporate client and is distributed under the MIT Licence. For details, see the LICENSE file.*

*Copyright © 2026, Rodrigo Ernesto Álvarez Aguilera.*
EOF

elif [[ "$PROJECT_TYPE" == "personal" ]]; then
    cat >> README.md << 'EOF'

---

*Este proyecto fue elaborado por Rodrigo Álvarez (@incognia) y se distribuye bajo la licencia GPLv3. Para más detalles, consulta el archivo LICENSE.*

*Copyright © 2026, Rodrigo Ernesto Álvarez Aguilera. Este es software libre bajo los términos de la GNU General Public License v3.*
EOF
fi
```

### Step 5: Validate application

```bash
echo "Validating licence application..."

# Verify LICENSE file created
if [[ -f "LICENSE" ]]; then
    echo "✓ LICENSE file created correctly"
    head -3 LICENSE
else
    echo "✗ Error: LICENSE file was not created"
fi

# Verify footer in README.md
if grep -q "Copyright.*2026.*Rodrigo" README.md; then
    echo "✓ Licensing footer added to README.md"
else
    echo "✗ Error: footer was not added correctly"
fi

# Show summary
echo ""
echo "Licensing summary:"
echo "Project type: $PROJECT_TYPE"
echo "Licence applied: $LICENSE_TYPE"
echo "Copyright year: $CURRENT_YEAR"
```

## Conclusion

This CoT automates licence application following the established rules:

1. **Automatic detection:** analyses README.md to determine the nature of the project
2. **Consistent application:** uses predefined templates according to project type
3. **Validation:** verifies that the files were created correctly
4. **Flexibility:** allows manual intervention when detection is ambiguous

**Usage:** run from the root of any project that has a README.md to automatically apply the appropriate licence.

**Requirements:** README.md in the current directory, internet access to download GPL v3.
