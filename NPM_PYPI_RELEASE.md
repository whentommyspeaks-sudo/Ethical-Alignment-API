# PyPI & NPM Release Guide
## Publish ARLREG to Global Package Registries

---

## PyPI Release (Python)

### 1. Setup PyPI Account

```bash
# Create account at https://pypi.org/account/register/
# Generate API token
```

### 2. Configure PyPI Credentials

```bash
# Create ~/.pypirc file
cat > ~/.pypirc << EOF
[distutils]
index-servers = pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-AgEIcHlwaS5vcmc...
EOF

chmod 600 ~/.pypirc
```

### 3. Build Distribution

```bash
# Install build tools
pip install --upgrade build twine

# Build source and wheel distributions
python -m build

# This creates:
# - dist/ethical-alignment-api-2.0.0.tar.gz (source)
# - dist/ethical-alignment_api-2.0.0-py3-none-any.whl (wheel)
```

### 4. Validate Distribution

```bash
# Check metadata
twine check dist/*

# Should show: PASSED
```

### 5. Upload to PyPI

```bash
# Upload to PyPI
twine upload dist/*

# Or just wheels (recommended for binary distributions)
twine upload dist/*.whl
```

### 6. Verify Installation

```bash
# Test installation
pip install --upgrade ethical-alignment-api

# Verify
python -c "from ethical_alignment import ARLREG; print(ARLREG)"
```

---

## NPM Release (JavaScript)

### 1. Setup NPM Account

```bash
# Create account at https://www.npmjs.com/signup
# Login locally
npm login
# Enter username, password, email, 2FA token (if enabled)
```

### 2. Prepare Package

```bash
# Make sure package.json has correct metadata
# Version should match git tag
jq '.version' package.json  # Should be "2.0.0"
```

### 3. Build JavaScript Distribution

```bash
# Compile TypeScript
npm run build

# This creates:
# - dist/index.js
# - dist/index.d.ts (TypeScript definitions)
```

### 4. Test Local Installation

```bash
# Create test directory
mkdir test-install && cd test-install

# Install locally from file system
npm install ../ethical-alignment-api

# Test
node -e "const ARLREG = require('ethical-alignment-api'); console.log(ARLREG);"
```

### 5. Publish to NPM

```bash
# From package root
npm publish

# Or with specific access (public/restricted)
npm publish --access public
```

### 6. Verify Publication

```bash
# Check on npm
npm view ethical-alignment-api

# Install from registry
npm install ethical-alignment-api
```

---

## Automated Release Pipeline

### GitHub Actions Workflow

Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI & NPM

on:
  release:
    types: [created]

jobs:
  publish-pypi:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install build dependencies
        run: pip install --upgrade build twine
      
      - name: Build distributions
        run: python -m build
      
      - name: Upload to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*

  publish-npm:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          registry-url: 'https://registry.npmjs.org'
      
      - name: Install dependencies
        run: npm install
      
      - name: Build
        run: npm run build
      
      - name: Publish to NPM
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
        run: npm publish
```

---

## Versioning & Git Tags

### Create Release

```bash
# Update version numbers
echo '2.0.1' > VERSION

# Update setup.py
sed -i 's/version=".*"/version="2.0.1"/' setup.py

# Update package.json
jq '.version = "2.0.1"' package.json > temp && mv temp package.json

# Commit changes
git add .
git commit -m "Bump version to 2.0.1"

# Create git tag
git tag -a v2.0.1 -m "Release version 2.0.1"

# Push to GitHub
git push origin main
git push origin v2.0.1
```

GitHub Actions will automatically publish when tag is pushed.

---

## Monitoring Package Health

### PyPI Stats

```bash
# Check download statistics
open "https://pypistats.org/packages/ethical-alignment-api"
```

### NPM Stats

```bash
# Check download statistics
open "https://www.npmtrends.com/ethical-alignment-api"
```

---

## Troubleshooting

### PyPI Issues

**401 Unauthorized**: Check API token in ~/.pypirc
**Invalid metadata**: Run `twine check dist/*`
**Already exists**: Version must be unique, bump to next version

### NPM Issues

**403 Forbidden**: Check npm login status with `npm whoami`
**Missing files**: Add files to `package.json` "files" array
**Not published**: Check `npm view ethical-alignment-api`

---

## Next Steps

1. ✅ Build and test locally
2. ✅ Setup automated publishing
3. ✅ Monitor downloads and metrics
4. ✅ Gather user feedback
5. ✅ Plan next release cycle
