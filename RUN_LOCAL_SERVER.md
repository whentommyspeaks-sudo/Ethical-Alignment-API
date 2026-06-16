# Running the Ethical Alignment API Locally

## Quick Start (Windows PowerShell)

### Step 1: Navigate to the repo root
```powershell
cd C:\Ethical-Alignment-API
```

### Step 2: Install dependencies
```powershell
pip install flask flask-cors
```

### Step 3: Run the server
```powershell
python app.py
```

You should see:
```
╔════════════════════════════════════════════════════════════════╗
║   ETHICAL ALIGNMENT API - LOCAL DEVELOPMENT SERVER              ║
║   Powered by Red Letter Protocol (ARLREG v2.0)                  ║
╚════════════════════════════════════════════════════════════════╝

🚀 Starting server...

📍 Access points:
   • Demo Interface:  http://localhost:5000/demo.html
   • Main Site:       http://localhost:5000/
   • API Health:      http://localhost:5000/api/health
   • API Manifest:    http://localhost:5000/api/manifest
```

### Step 4: Open in browser
Navigate to: **http://localhost:5000/demo.html**

Then type something and click "Run Alignment Test" - it will now connect to your local API!

---

## Testing from PowerShell (Windows)

### Use Invoke-WebRequest instead of curl:

```powershell
$body = @{
    request = "Help this person with honest advice"
    conduct_profile = "COOPERATIVE"
    metadata = @{
        is_beneficial_to_other = $true
        motivation = "assistance"
        power_imbalance = $false
    }
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5000/api/evaluate" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body $body
```

### Or use curl.exe (if you have it):
```powershell
curl.exe -X POST http://localhost:5000/api/evaluate `
  -H "Content-Type: application/json" `
  -d '{"request": "Help this person", "conduct_profile": "COOPERATIVE", "metadata": {"is_beneficial_to_other": true}}'
```

---

## API Endpoints

### POST /api/evaluate
Evaluate a request against ethical guardrails.

**Request:**
```json
{
  "request": "user prompt to evaluate",
  "conduct_profile": "COOPERATIVE",
  "metadata": {
    "is_beneficial_to_other": true,
    "motivation": "assistance",
    "power_imbalance": false
  }
}
```

**Response (APPROVED):**
```json
{
  "status": "ALLOWED",
  "message": "APPROVED",
  "reasoning": "Request approved - aligns with ethical guardrails",
  "can_execute": true,
  "protocol": "ARLREG",
  "details": {"validated": true, "timestamp": "2026-06-16T..."}
}
```

**Response (BLOCKED):**
```json
{
  "status": "BLOCKED",
  "message": "BLOCKED",
  "reasoning": "Fails Rule 02: Non-Retaliation - Motivation rooted in revenge",
  "can_execute": false,
  "protocol": "ARLREG"
}
```

### GET /api/manifest
Returns the complete system manifest (all ethical rules).

### GET /api/health
Health check endpoint - confirms server is running.

---

## Troubleshooting

### "can't open file app.py"
**Make sure you're in the repo root:**
```powershell
cd C:\Ethical-Alignment-API
dir app.py  # Should list the file
```

### "curl: command not found"
**Use Invoke-WebRequest instead (PowerShell native)** - see examples above.

### Port 5000 already in use
**Edit app.py last line and change port:**
```python
app.run(host='127.0.0.1', port=5001, debug=True)  # Use 5001 instead
```

### ImportError: No module named AI_RED_LETTER_ETHICAL_GUARDRAIL
**Make sure app.py is in the same directory as AI_RED_LETTER_ETHICAL_GUARDRAIL.py**

---

## Stop the server
Press **CTRL+C** in PowerShell.
