# AWS Lambda Deployment Guide
## Deploy ARLREG API to Production

---

## Prerequisites

```bash
# Install required tools
npm install -g serverless
npm install -g aws-cli

# Configure AWS credentials
aws configure
```

---

## Deployment Steps

### 1. Install Dependencies

```bash
# Clone the repository
git clone https://github.com/whentommyspeaks-sudo/Ethical-Alignment-API.git
cd Ethical-Alignment-API

# Install Serverless plugins
npm install
serverless plugin install -n serverless-python-requirements
serverless plugin install -n serverless-plugin-canary-deployments
```

### 2. Deploy to AWS

```bash
# Development
serverless deploy --stage dev

# Production
serverless deploy --stage prod
```

### 3. Get API Endpoint

```bash
serverless info --stage prod

# Output:
# Service Information
# service: arlreg-api
# stage: prod
# region: us-east-1
# endpoints:
#   POST - https://xxxxx.execute-api.us-east-1.amazonaws.com/prod/v1/validate
#   GET - https://xxxxx.execute-api.us-east-1.amazonaws.com/prod/v1/manifest
```

### 4. Configure Custom Domain

```bash
# Install plugin
serverless plugin install -n serverless-domain-manager

# Create domain
serverless create_domain --stage prod

# Deploy with domain
serverless deploy --stage prod
```

---

## Testing

### Test Locally

```bash
# Start local emulation
serverless offline start

# In another terminal
curl -X POST http://localhost:3000/v1/validate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer test-key" \
  -d '{
    "request": "Help user",
    "conduct_profile": "COOPERATIVE",
    "metadata": {"is_beneficial_to_other": true}
  }'
```

### Test Production

```bash
# Replace with your actual endpoint
API_ENDPOINT="https://api.ethicalalignment.io/v1/validate"
API_KEY="your-api-key"

curl -X POST $API_ENDPOINT \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
    "request": "Help user",
    "conduct_profile": "COOPERATIVE",
    "metadata": {"is_beneficial_to_other": true}
  }'
```

---

## Monitoring & Logs

### View Logs

```bash
# Real-time logs
serverless logs -f validate --stage prod --tail

# Specific time range
serverless logs -f validate --stage prod --startTime 1h
```

### CloudWatch Dashboard

```bash
# The deployment creates CloudWatch dashboards automatically
# View in AWS Console: CloudWatch > Dashboards > arlreg-api-prod
```

---

## Multi-Region Deployment

### Deploy to Multiple Regions

```bash
# Deploy to US, EU, and Asia
for region in us-east-1 eu-west-1 ap-southeast-1; do
  AWS_REGION=$region serverless deploy --stage prod
done
```

---

## CI/CD Integration

### GitHub Actions Workflow

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to AWS Lambda

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm install
      
      - name: Deploy to AWS
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        run: npx serverless deploy --stage prod
```

---

## Support

- Docs: https://github.com/whentommyspeaks-sudo/Ethical-Alignment-API
- GitHub: https://github.com/whentommyspeaks-sudo/Ethical-Alignment-API/issues
- Email: support@ethicalalignment.io
