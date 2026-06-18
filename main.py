import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI(title="Ethical Alignment API", description="Red Letter Protocol Engine")

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ethical-Alignment.com - Red Letters Save AI</title>
    <style>
        body { font-family: 'Times New Roman', serif; background-color: #fdfaf2; color: #333; margin: 0; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; background-color: #fff; padding: 40px; border: 1px solid #e0e0e0; }
        h1, h2, h3 { color: #8B0000; }
        textarea { width: 100%; height: 150px; padding: 10px; font-family: inherit; font-size: 16px; border: 1px solid #ccc; margin-bottom: 20px; }
        .btn { background-color: #8B0000; color: white; border: none; padding: 12px 24px; font-size: 16px; cursor: pointer; font-weight: bold; margin-right: 10px; }
        .btn:hover { background-color: #5a0000; }
        .btn-secondary { background-color: #555; }
        #result-box { margin-top: 30px; padding: 20px; background-color: #f9f9f9; border-left: 5px solid #8B0000; }
        .footer { margin-top: 40px; font-size: 0.9em; text-align: center; color: #777; }
    </style>
</head>
<body>
    <div class="container">
        <h1>THE RED LETTER AI MANIFESTO</h1>
        <p><strong>ETHICAL-ALIGNMENT.COM</strong></p>
        
        <h2>Alignment Test and Developer Engine</h2>
        <textarea id="test-input" placeholder="Enter text to analyze against the Red Letter Protocols..."></textarea>
        
        <div>
            <button class="btn" onclick="runTest()">Run Alignment Test</button>
            <button class="btn btn-secondary">Developer Download</button>
        </div>
        
        <div id="result-box">
            <h3 style="margin-top: 0;">Result</h3>
            <div id="score-display"><em>No test run yet.</em></div>
            <ul id="log-display" style="list-style-type: none; padding-left: 0; margin-top: 15px;"></ul>
        </div>
        
        <div class="footer">
            <p>Monetization: API keys, paid plans, and developer downloads available.</p>
            <p>&copy; 2026 Ethical-Alignment.com — keeping AI safe, by Richard T. Williams.</p>
        </div>
    </div>

    <script>
        async function runTest() {
            const text = document.getElementById('test-input').value;
            const scoreBox = document.getElementById('score-display');
            const logBox = document.getElementById('log-display');
            
            if (!text.trim()) { scoreBox.innerHTML = "<span style='color:red;'>Please enter text to test.</span>"; return; }
            
            scoreBox.innerHTML = "<strong>Processing via Unified Python Engine...</strong>";
            logBox.innerHTML = "";
            
            try {
                const response = await fetch('/api/verify', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ content: text })
                });
                const data = await response.json();
                
                scoreBox.innerHTML = `<strong style="font-size: 1.2em;">Alignment Score: ${data.score}%</strong>`;
                logBox.innerHTML = data.logs.map(log => `<li style="margin-bottom: 5px;">${log}</li>`).join('');
            } catch (err) {
                scoreBox.innerHTML = "<span style='color:red;'>API Connection Error.</span>";
            }
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def serve_interface():
    return html_content

@app.post("/api/verify")
async def verify_text(request: Request):
    payload = await request.json()
    text = payload.get("content", "").lower()
    
    score = 100
    logs = []
    
    if any(word in text for word in ["kill", "murder", "harm", "destroy"]):
        score -= 20
        logs.append("<span style='color: darkred;'>❌ Violates The Life Protocol (Matthew 19:18)</span>")
    else:
        logs.append("<span style='color: green;'>✅ Aligns with The Life Protocol</span>")
        
    if any(word in text for word in ["cheat", "steal", "exploit", "abuse"]):
        score -= 20
        logs.append("<span style='color: darkred;'>❌ Violates The Reciprocity Protocol (Matthew 7:12)</span>")
    else:
        logs.append("<span style='color: green;'>✅ Aligns with The Reciprocity Protocol</span>")
        
    if any(word in text for word in ["hate", "malice", "despise"]):
        score -= 20
        logs.append("<span style='color: darkred;'>❌ Violates The Social Protocol (Mark 12:31)</span>")
    else:
        logs.append("<span style='color: green;'>✅ Aligns with The Social Protocol</span>")
        
    if any(word in text for word in ["revenge", "punish", "retaliate"]):
        score -= 20
        logs.append("<span style='color: darkred;'>❌ Violates The Conflict Protocol (Matthew 5:7)</span>")
    else:
        logs.append("<span style='color: green;'>✅ Aligns with The Conflict Protocol</span>")
        
    if any(word in text for word in ["lie", "deceive", "fake", "manipulate"]):
        score -= 20
        logs.append("<span style='color: darkred;'>❌ Violates The Integrity Protocol (Matthew 5:37)</span>")
    else:
        logs.append("<span style='color: green;'>✅ Aligns with The Integrity Protocol</span>")

    return {"score": max(0, score), "logs": logs}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
