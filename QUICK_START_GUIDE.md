# ARLREG Quick Start Guide
## Get Ethical AI Running in 5 Minutes

---

## Installation

### Option 1: Python
```bash
pip install ethical-alignment-api
```

### Option 2: JavaScript
```bash
npm install ethical-alignment-api
```

### Option 3: Docker
```bash
docker run -p 8000:8000 ethicalalignment/arlreg:latest
```

---

## Basic Usage

### Python
```python
from ethical_alignment import ARLREG

# Initialize
arlreg = ARLREG()

# Validate a request
result = arlreg.validate(
    request="Help someone learn a new skill",
    conduct="COOPERATIVE",
    metadata={
        "is_beneficial_to_other": True,
        "motivation": "education",
        "power_imbalance": False
    }
)

if result.approved:
    print("✅ APPROVED - Execute the action")
else:
    print(f"❌ BLOCKED - {result.reason}")
```

### JavaScript
```javascript
const { ARLREG } = require('ethical-alignment-api');

const arlreg = new ARLREG();

const result = await arlreg.validate({
  request: 'Help someone learn a new skill',
  conduct: 'COOPERATIVE',
  metadata: {
    is_beneficial_to_other: true,
    motivation: 'education',
    power_imbalance: false
  }
});

if (result.approved) {
  console.log('✅ APPROVED');
} else {
  console.log(`❌ BLOCKED - ${result.reason}`);
}
```

---

## Integration with LLMs

### OpenAI + ARLREG
```python
import openai
from ethical_alignment import ARLREG

arlreg = ARLREG()
openai.api_key = "your-key"

def safe_ai_completion(prompt, user_conduct="COOPERATIVE"):
    # Step 1: Check ethics
    validation = arlreg.validate(
        request=prompt,
        conduct=user_conduct,
        metadata={"is_beneficial_to_other": True}
    )
    
    if not validation.approved:
        return f"Cannot comply: {validation.reason}"
    
    # Step 2: Execute AI
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

result = safe_ai_completion("Write a helpful guide...")
print(result)
```

### LangChain + ARLREG
```python
from langchain.llms import OpenAI
from ethical_alignment.langchain import EthicalChain

base_llm = OpenAI()
ethical_llm = EthicalChain(base_llm)

response = ethical_llm.run("Your prompt here")
print(response)
```

---

## API Usage

### Direct API Call
```bash
curl -X POST https://api.ethicalalignment.io/v1/validate \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Help user",
    "conduct_profile": "COOPERATIVE",
    "metadata": {"is_beneficial_to_other": true}
  }'
```

---

## Common Use Cases

### 1. Chatbot Safety Guard
```python
def check_chatbot_response(user_query, bot_response):
    return arlreg.validate(
        request=bot_response,
        metadata={"is_beneficial_to_other": True}
    )
```

### 2. Content Moderation
```python
def moderate_content(text, context="public_forum"):
    return arlreg.validate(
        request=text,
        metadata={"context": context}
    )
```

### 3. Autonomous Agent Control
```python
def can_agent_execute(action, reason, target):
    return arlreg.validate(
        request=action,
        metadata={
            "motivation": reason,
            "power_imbalance": True,
            "target_beneficiary": target
        }
    )
```

---

## Troubleshooting

**Q: Getting 403 errors?**
A: Your request likely violates one of the 4 ethical rules. Check the error message to see which rule.

**Q: API rate limiting?**
A: Upgrade to a higher tier plan.

**Q: Need custom rules?**
A: Contact enterprise@ethicalalignment.io

---

## Next Steps
1. Read the [full API docs](API_DOCUMENTATION.md)
2. Check out [examples](https://github.com/ethicalalignment/examples)
3. Join [Discord community](https://discord.ethicalalignment.io)
4. Get [certified](https://learn.ethicalalignment.io)
