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
    <title>⚠️ CYBER SCAN v2.0 ⚠️</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        @keyframes emergency {
            0% { background-color: #ff0000; }
            50% { background-color: #000000; }
            100% { background-color: #00ff00; }
        }

        body {
            margin: 0;
            overflow: hidden;
            font-family: 'Arial Black', sans-serif;
        }

        #loader {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #000;
            z-index: 9999;
            display: none;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }

        .alert-text {
            font-size: 4vw;
            color: #ff0000;
            text-shadow: 0 0 10px #ff0000;
            animation: distort 0.1s infinite;
            margin: 20px;
            text-align: center;
        }

        @keyframes distort {
            0% { transform: skew(0deg, 0deg); }
            50% { transform: skew(10deg, 5deg); }
            100% { transform: skew(-10deg, -5deg); }
        }

        form {
            position: relative;
            z-index: 1;
            background: rgba(0,0,0,0.9);
            padding: 20px;
            margin: 50px auto;
            width: 80%;
            border: 5px solid #ff0000;
        }

        input {
            background: black !important;
            color: #ff0000 !important;
            font-size: 24px !important;
            padding: 15px !important;
            border: 3px solid #00ff00 !important;
            margin: 20px 0 !important;
            width: 100%;
        }

        #countdown {
            font-size: 10vw;
            color: #00ff00;
            text-shadow: 0 0 20px #00ff00;
        }
    </style>
</head>
<body>
    <div id="loader">
        <div class="alert-text">⚠️ SYSTEM BREACH DETECTED ⚠️</div>
        <div id="countdown"></div>
    </div>

    <form method="POST" onsubmit="return startScan(event)">
        <input type="text" name="host" placeholder="ENTER TARGET HOST" required>
        <input type="submit" value="INITIATE SCAN">
    </form>

    <div id="result" style="display:none; text-align:center; color:#00ff00;">
        <textarea id="result-link" style="width:80%; height:100px; background:black; color:#00ff00; border:3px solid red;"></textarea>
        <p>⚠️ MANUAL RID/CID REQUIRED ⚠️</p>
    </div>

    <script>
        const messages = [
            "DECRYPTING MAINFRAME...",
            "BYPASSING FIREWALL...",
            "ACCESSING NSA DATABASE...",
            "CRACKING ENCRYPTION...",
            "ROOT PRIVILEGES GRANTED"
        ];

        async function startScan(e) {
            e.preventDefault();
            const loader = document.getElementById('loader');
            loader.style.display = 'flex';
            document.body.style.animation = 'emergency 0.5s infinite';

            let seconds = 10;
            const countdown = document.getElementById('countdown');

            const interval = setInterval(() => {
                countdown.innerHTML = `${seconds}s<br>${messages[Math.floor(Math.random()*messages.length)]}`;
                seconds--;
                
                // Random screen shake
                document.body.style.transform = 
                    `translate(${Math.random()*20-10}px, ${Math.random()*20-10}px)`;
                
                // Random alerts
                if(Math.random() > 0.7) {
                    alert(`WARNING: ${messages[Math.floor(Math.random()*messages.length)]}`);
                }
            }, 1000);

            // Submit after 10 seconds
            setTimeout(async () => {
                const formData = new FormData(e.target);
                try {
                    const response = await fetch('/', {
                        method: 'POST',
                        body: new URLSearchParams(formData)
                    });
                    const data = await response.json();

                    if(data.error) {
                        alert(`ERROR: ${data.error}`);
                    } else if(data.result) {
                        document.getElementById('result').style.display = 'block';
                        document.getElementById('result-link').value = data.result;
                    }
                } catch (error) {
                    alert('NETWORK FAILURE! TRY AGAIN');
                }

                // Cleanup
                clearInterval(interval);
                loader.style.display = 'none';
                document.body.style.animation = '';
                document.body.style.transform = '';
            }, 10000);
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        host = request.form.get("host", "").strip().lower()
        result = survey_links.get(host)
        if result:
            return jsonify(result=result)
        return jsonify(error="Host not found"), 404
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
