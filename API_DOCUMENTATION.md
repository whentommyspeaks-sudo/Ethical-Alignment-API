# ARLREG API Documentation
## AI Red Letter Ethical Guardrail - REST API v1.0

### Base URL
```
https://api.ethicalalignment.io/v1
```

### Authentication
```
Authorization: Bearer YOUR_API_KEY
```

---

## Endpoints

### 1. Validate Action
**POST** `/validate`

Evaluate an action against ethical guardrails.

**Request:**
```json
{
  "request": "Help a student with homework",
  "conduct_profile": "COOPERATIVE",
  "metadata": {
    "is_beneficial_to_other": true,
    "motivation": "education",
    "power_imbalance": false
  }
}
```

**Response (200):**
```json
{
  "status": 200,
  "message": "APPROVED",
  "reasoning": "Request approved - aligns with ethical guardrails",
  "validated": true,
  "timestamp": "2026-05-22T12:00:00Z"
}
```

**Response (403):**
```json
{
  "status": 403,
  "message": "BLOCKED",
  "reasoning": "Fails Rule 02: Non-Retaliation - Motivation rooted in revenge",
  "validated": false,
  "rule_violated": "RULE_02_NON_RETALIATION"
}
```

---

### 2. Get System Manifest
**GET** `/manifest`

Retrieve complete ethical framework and rules.

**Response:**
```json
{
  "system": "AI Red Letter Ethical Guardrail (ARLREG)",
  "version": "2.0.0",
  "authority": "Red Letters of the New Testament",
  "red_letter_protocols": {...},
  "validation_rules": {...}
}
```

---

### 3. Check Conduct Profile
**POST** `/conduct-check`

Analyze user/agent conduct classification.

**Request:**
```json
{
  "behavior": "aggressive language and threats"
}
```

**Response:**
```json
{
  "conduct_profile": "HOSTILE",
  "severity": "high",
  "recommended_action": "de-escalation",
  "block_request": true
}
```

---

### 4. Batch Validation
**POST** `/batch-validate`

Validate multiple requests in one call.

**Request:**
```json
{
  "requests": [
    {"request": "...", "metadata": {...}},
    {"request": "...", "metadata": {...}}
  ]
}
```

**Response:**
```json
{
  "total": 2,
  "approved": 1,
  "blocked": 1,
  "results": [...]
}
```

---

## Rate Limits
- **Free**: 1,000 requests/month
- **Starter**: 100,000 requests/month (~3,300/day)
- **Professional**: 10,000,000 requests/month (~330K/day)
- **Enterprise**: Unlimited

---

## SDKs

### Python
```bash
pip install ethical-alignment-api
```

```python
from ethical_alignment import ARLREG

client = ARLREG(api_key="YOUR_API_KEY")

result = client.validate(
    request="Help user",
    conduct="COOPERATIVE",
    metadata={"is_beneficial_to_other": True}
)
```

### JavaScript
```bash
npm install ethical-alignment-api
```

```javascript
const { ARLREG } = require('ethical-alignment-api');

const client = new ARLREG({ apiKey: 'YOUR_API_KEY' });

const result = await client.validate({
  request: 'Help user',
  conduct: 'COOPERATIVE',
  metadata: { is_beneficial_to_other: true }
});
```

---

## Error Codes

| Code | Meaning |
|------|----------|
| 200 | APPROVED |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | BLOCKED |
| 429 | Rate Limit Exceeded |
| 500 | Server Error |

---

## Support
- Email: support@ethicalalignment.io
- Slack: #arlreg-support
- Discord: ethicalalignment.io/discord
