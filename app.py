from flask import Flask, request, render_template_string, jsonify
import random

app = Flask(__name__)

survey_links = {
    "nsv.netr.jp": "https://notch.insights.supply/cb?token=c8e8a4ee-bc1f-4fb7-8b91-bc104de23079&RID=",
    "survey.qualtrics.com": "https://s.cint.com/Survey/Complete?ProjectToken=82935c18-f510-4057-9db3-b2e4dbeb2c94&cid=",
    "as-c1-web01.opinion.life": "https://stop.opinion.life/finished/10/fingerprint/4D62E3F6-201C-4D88-8D3B-1B5DB643F8AC/C1/17238/?startUtc=",
}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>🔥 CYBER HACK PRO MAX 🔥</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        @keyframes glitch {
            0% { text-shadow: 3px 3px red, -3px -3px blue; }
            25% { transform: skew(10deg); }
            50% { text-shadow: -5px 5px green, 5px -5px yellow; }
            75% { transform: skew(-10deg); }
            100% { text-shadow: none; }
        }

        body {
            margin: 0;
            overflow: hidden;
            background: #000;
            font-family: 'Courier New', monospace;
        }

        #loader {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.95);
            z-index: 9999;
            display: none;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }

        #matrix-canvas {
            position: fixed;
            top: 0;
            left: 0;
            pointer-events: none;
            z-index: -1;
        }

        form {
            position: relative;
            z-index: 2;
            background: rgba(0,0,0,0.8);
            padding: 30px;
            margin: 50px auto;
            width: 80%;
            border: 3px solid #ff0000;
            border-radius: 10px;
        }

        input {
            background: #111 !important;
            color: #0f0 !important;
            font-size: 24px !important;
            padding: 15px !important;
            border: 2px solid #00f !important;
            margin: 15px 0 !important;
            width: 100%;
        }

        #countdown {
            font-size: 10vw;
            color: #0f0;
            text-shadow: 0 0 20px #0f0;
        }

        #result {
            display: none;
            text-align: center;
            margin-top: 30px;
        }

        #copy-btn {
            background: #0f0;
            color: #000;
            border: none;
            padding: 12px 24px;
            font-size: 20px;
            cursor: pointer;
            margin: 15px;
            display: none;
        }
    </style>
</head>
<body>
    <canvas id="matrix-canvas"></canvas>
    
    <div id="loader">
        <div id="countdown">10</div>
        <div style="color:#0f0; font-size:24px;">HACKING DATA...</div>
    </div>

    <form onsubmit="startHacking(event)">
        <input type="text" name="host" placeholder="🌐 ENTER TARGET HOST" required>
        <input type="submit" value="🚀 LAUNCH CYBER NUKES" style="background:#f00; color:#000; cursor:pointer;">
    </form>

    <div id="result">
        <textarea id="result-link" readonly></textarea>
        <button id="copy-btn" onclick="copyToClipboard()">📋 COPY LINK</button>
    </div>

    <script>
        // Matrix Rain
        const canvas = document.getElementById('matrix-canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()';
        const drops = new Array(Math.floor(canvas.width/10)).fill(1);

        function drawMatrix() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#0f0';
            ctx.font = '18px monospace';

            drops.forEach((drop, i) => {
                const char = chars[Math.floor(Math.random()*chars.length)];
                ctx.fillText(char, i*20, drop*20);
                drops[i] = drop > canvas.height/20 ? 0 : drop+1;
            });
        }
        setInterval(drawMatrix, 50);

        // Hacking System
        async function startHacking(e) {
            e.preventDefault();
            const loader = document.getElementById('loader');
            loader.style.display = 'flex';
            
            let seconds = 10;
            const countdown = document.getElementById('countdown');
            
            // Crazy Effects
            const interval = setInterval(() => {
                countdown.textContent = `${seconds}s`;
                seconds--;
                
                // Screen Shaking
                document.body.style.transform = 
                    `translate(${Math.random()*20-10}px, ${Math.random()*20-10}px)`;
                
                // Random Color Flash
                document.body.style.backgroundColor = 
                    `rgb(${Math.random()*255},${Math.random()*255},${Math.random()*255})`;
            }, 1000);

            // Submit After 10s
            setTimeout(async () => {
                const formData = new FormData(e.target);
                try {
                    const response = await fetch('/', {
                        method: 'POST',
                        body: new URLSearchParams(formData)
                    });
                    const data = await response.json();

                    if(data.result) {
                        document.getElementById('result').style.display = 'block';
                        document.getElementById('result-link').value = data.result;
                        document.getElementById('copy-btn').style.display = 'block';
                    } else {
                        alert('❌ HOST NOT FOUND IN DARK WEB!');
                    }
                } catch(error) {
                    alert('🌐 NETWORK FAILURE!');
                }

                clearInterval(interval);
                loader.style.display = 'none';
                document.body.style.transform = '';
                document.body.style.backgroundColor = '#000';
            }, 10000);
        }

        // Copy Function
        function copyToClipboard() {
            navigator.clipboard.writeText(document.getElementById('result-link').value)
                .then(() => alert('✅ Copied to clipboard!'))
                .catch(() => alert('❌ Failed to copy!'));
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        host = request.form.get("host", "").strip().lower()
        return jsonify(result=survey_links.get(host)) if host in survey_links else jsonify(error=True)
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
