from flask import Flask, request, render_template_string, jsonify
import time

app = Flask(__name__)

# Survey Links by Provider
survey_links = {
    # Cint Links
    "cint": {
        "survey.qualtrics.com": "https://s.cint.com/Survey/Complete?ProjectToken=82935c18-f510-4057-9db3-b2e4dbeb2c94&cid=abd323f8-dfde-07bc-5a8b-16f86d8e8d7d ",
        "survey.euro.confirmit.com": "https://s.cint.com/Survey/Complete?ProjectToken=a7311842-5dc7-44ff-acd4-45bc2617c2f2 ",
        "ts1.eu.qualtrics.com": "https://s.cint.com/Survey/Complete?ProjectToken=bcef6b5b-ec3b-482d-ad20-bd1e98ef77a3&memno=97d85a8d-ff6f-c3bb-a9ff-6ff3d5f5a508 ",
        "radiointelligence.qualtrics.com": "https://s.cint.com/Survey/Complete?ProjectToken=6ed619c1-0f8b-47c2-8c54-a753e7b14bcc ",
        "join.survey-researchonline.com": "https://s.cint.com/Survey/Complete?ProjectToken=ffa06f14-1c07-4864-b060-aea4a8cbf5dc&ID=30feadd9-17cd-8ed3-0ca7-98d50492d95f0 ",
        "tolunaapac.decipherinc.com": "https://s.cint.com/Survey/Complete?ProjectToken=6983cf67-96ed-47de-b1e7-9464eea8f5a7 ",
        "no.mantapsurvey.com": "https://s.cint.com/Survey/Complete?ProjectToken=60d7c929-35e8-4740-9bc4-9a86cb2ccee6 ",
        "unitedminds.nu": "https://s.cint.com/Survey/Complete?ProjectToken=4ee25533-0429-4f26-8534-7be28ef278be ",
        "secure.bandasurvey.ie": "https://s.cint.com/Survey/Complete?ProjectToken=d8dc73fb-4e56-4d28-b121-5867490d2a8e ",
        "hub.decipherinc.com": "https://s.cint.com/Survey/Complete?ProjectToken=4a114089-0284-4e1f-ac00-e2d006964dd5 ",
        "selfserve.decipherinc.com/survey/selfserve/20e9": "https://s.cint.com/Survey/Complete?ProjectToken=ea25e4cb-95a5-4757-90cb-cad968b63474 "
    },
    
    # Samplicio Links
    "samplicio": {
        "nsv.netr.jp": "https://notch.insights.supply/cb?token=c8e8a4ee-bc1f-4fb7-8b91-bc104de23079&RID=67f3526c-0719-9f2b-18e0-4714efa34c48 ",
        "welcome.walr.com": "https://notch.insights.supply/cb?token=288a1257-09e2-43e3-8765-e0c35d1affad&RID=680cb56d-63c5-d565-2016-692d458c1282 ",
        "survey.bva-bdrc.com": "https://notch.insights.supply/cb?token=f0de7179-e61e-43d0-89ad-916c9b57b2f4&RID=67fe7767-3030-4149-9daa-ec9dbcac70ef ",
        "surveys.sago.com": "https://notch.insights.supply/cb?token=312ef1b8-f520-4c8e-b19f-57d47ded4a9d&RID= ",
        "research.statista.com": "https://notch.insights.supply/cb?token=646b929b-79ca-49e0-a4e9-606f1a8b489c&RID= ",
        "m.survey.bz": "https://notch.insights.supply/cb?token=8c11ba96-5605-486f-9feb-0021fd40c3b4&RID= ",
        "operations.horizoom.io": "https://operations.horizoom.io/survey/finish/?m=6006&return=complete&i_survey=3___HZTU_C1XbRWpuHTCZzl1zbjrBPVQdpHrkK6m4Z8y7 ",
        "router.cint": "https://notch.insights.supply/cb?token=0749a007-a1d3-48c1-8ff3-12960c555867&RID=680a1075-f8d6-c662-6490-ac5bf550e2bb ",
        "surveys.thepanelstation.com": "https://notch.insights.supply/cb?token=6212d07b-2455-478a-b1a0-7e2b420b6887&RID=680dd547-9fdb-4167-aeab-277fcbd1fb6c ",
        "us1se.voxco.com": "https://notch.insights.supply/cb?token=d9af61cb-78d3-401d-93c1-d2ce388a8cd4&RID=681b21a4-62bd-cf88-4e5c-a4be0a78e74a ",
        "ex-plorsurvey.com": "https://notch.insights.supply/cb?token=feea7119-8b04-41f6-979f-8ca2a130ed78&RID= ",
        "survey.alchemer.com/s3": "https://notch.insights.supply/cb?token=58f6aab2-8efe-40ea-aba7-f458e7615a76&RID=6813929c-93af-0bc4-89c4-d1fdbdde5e0d0 ",
        "survey-d.yoursurveynow.com": "https://notch.insights.supply/cb?token=ae73d5f2-56f0-4a2d-a235-328e8ac28275&RID= ",
        "research.qualtrics.com": "https://notch.insights.supply/cb?token=0d0dc9e7-9541-4365-b4b2-b9522e4a21a7&RID= ",
        "survey.sapioresearch.com": "https://notch.insights.supply/cb?token=ca8743bc-77fd-45f7-9777-f8a2692c0d50&RID=681ee956-31d4-d0e8-3b18-4c1136131f86&hash=qamXWQ4L1BK0mZNE6xf5opxm9eA ",
        "survey.gavenze.com": "https://notch.insights.supply/cb?token=4efe325d-fea9-44c0-8cc3-56ff71bbf160&RID= ",
        "kanaka.com": "https://notch.insights.supply/cb?token=d415cc7d-6d67-41b8-81e1-d92733e9e762&RID= ",
        "surveysconnect.co.uk": "https://notch.insights.supply/cb?token=68f41caf-9154-4775-991e-9f1e08ec325c&RID= "
    },

    # Samplecube Links
    "samplecube": {
        "as-c1-web01.opinion.life": "https://stop.opinion.life/finished/10/622e2ced-3751-6a31-639c-19054c232e68/4D62E3F6-201C-4D88-8D3B-1B5DB643F8AC/C1/17238/?startUtc= ",
        "nrg.decipherinc.com": "https://surveys.sample-cube.com/ending?RS=1&RID=0a435efb-2af9-40a9-8f02-fe6ec580327b&secret=25611 ",
        "emea.focusvision.com": "https://surveys.sample-cube.com/ending?RS=1&RID=7f08e822-339a-4de6-8f0e-8598214ea38d&secret=606 ",
        "snapchat.co1.qualtrics.com": "https://surveys.sample-cube.com/ending?RS=1&RID=xxxxxxxxxxxxxxxxxxxxxxxx&secret=2995 ",
        "bizpinionsurveys.com": "https://surveys.sample-cube.com/ending?RS=1&RID=02d6ee5d-610d-4204-876e-1ff0bfaf6e31&secret=785 ",
        "survey.euro.confirmit.com/wix/7/": "https://surveys.sample-cube.com/ending/?RS=1&RID=e93825f2-61de-44e5-ab58-66c24f5b33c0&secret=34828 "
    },

    # Direct Links
    "direct": {
        "survey.opinionest.com": "https://message.opinionest.com/survey/survey-callback.aspx?s=3&TOID=41695376E06919EACC2FD0104CE0266E ",
        "zampcomplete.zamplia.com": "https://zampcomplete.zamplia.com/?UID=26328551 ",
        "uf.sampleeye.com": "https://uf.sampleeye.com/end?RT=9CD70677-3159-4580-93DA-CBFAE0EAED8A&Status=1 ",
        "message.insight.rakuten.com": "https://message.insight.rakuten.com/survey/Spassback.do?pid=177722116&uid=26791196=a2Ta8FjT&st=c ",
        "rf2.symmppl.io": "https://rf2.symmppl.io/ending?eid=5abfe63278ac4f098ed047981620f890&estsid=1 ",
        "d8aspring.post-survey.com": "https://d8aspring.post-survey.com/ans/back/?status=comp ",
        "surveys.irbureau.com": "https://surveys.irbureau.com/panelistResponse?panelistResponse=103&rid= "
    }
}

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>ðŸ”¥ AB Survey Tool ðŸ”¥</title>
  <style>
    body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      color: white;
    }

    .container {
      background: rgba(255, 255, 255, 0.05);
      padding: 30px;
      border-radius: 15px;
      box-shadow: 0 8px 20px rgba(0, 255, 153, 0.2);
      text-align: center;
      width: 90%;
      max-width: 400px;
    }

    h1 {
      color: #00ff99;
      font-size: 2em;
      margin-bottom: 20px;
      text-shadow: 0 0 10px #00ff99;
    }

    form {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }

    select, input[type="text"], button {
      padding: 12px;
      font-size: 16px;
      border: none;
      border-radius: 8px;
      background: #ffffff;
      color: #333;
      outline: none;
    }

    button {
      background: #00ff99;
      color: white;
      font-weight: bold;
    }

    button:hover {
      background: #00cc80;
    }

    textarea {
      margin-top: 20px;
      width: 100%;
      min-height: 100px;
      padding: 12px;
      border-radius: 8px;
      font-size: 16px;
      background: #fff;
      color: #333;
      resize: vertical;
    }

    .copy-btn {
      background: #00ff99;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 8px;
      margin-top: 10px;
      cursor: pointer;
    }

    .copy-btn:hover {
      background: #00cc80;
    }

    /* Unique Pulse Ring Loader */
    .loader {
      display: none;
      margin: 30px auto;
      width: 50px;
      height: 50px;
      border-radius: 50%;
      border: 5px solid #00ff99;
      border-top: 5px solid transparent;
      animation: pulse 1s infinite linear;
    }

    @keyframes pulse {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    @media (max-width: 600px) {
      h1 {
        font-size: 1.5em;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>AB Survey Tool </h1>
    <form id="survey-form" onsubmit="startHacking(event)">
      <select name="provider" required>
        <option value="">Select Provider</option>
        <option value="cint">Cint</option>
        <option value="samplicio">Samplicio</option>
        <option value="samplecube">Samplecube</option>
        <option value="direct">Direct</option>
      </select>
      <input type="text" name="host" placeholder=" ENTER TARGET HOST" required />
      <button type="submit">Generate Link</button>
    </form>

    <div class="loader" id="loader"></div>

    <div class="result" style="display: none;">
      <textarea id="result-link" readonly></textarea>
      <button class="copy-btn" onclick="copyToClipboard()">‹ COPY LINK</button>
    </div>
  </div>

  <script>
    async function startHacking(e) {
      e.preventDefault();
      document.getElementById('loader').style.display = 'block';
      document.querySelector('.result').style.display = 'none';

      const formData = new FormData(document.getElementById('survey-form'));
      try {
        const response = await fetch('/', {
          method: 'POST',
          body: new URLSearchParams(formData)
        });
        const data = await response.json();

        if (data.result) {
          setTimeout(() => {
            document.getElementById('loader').style.display = 'none';
            document.querySelector('.result').style.display = 'block';
            document.getElementById('result-link').value = data.result;
          }, 5000);
        } else {
          alert('âŒ HOST NOT FOUND IN DATABASE!');
          document.getElementById('loader').style.display = 'none';
        }
      } catch (error) {
        alert('ðŸŒ NETWORK FAILURE!');
        document.getElementById('loader').style.display = 'none';
      }
    }

    function copyToClipboard() {
      navigator.clipboard.writeText(document.getElementById('result-link').value)
        .catch(() => console.error('Copy failed'));
    }
  </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        provider = request.form.get("provider")
        host = request.form.get("host").strip().lower()
        
        if provider in survey_links:
            links = survey_links[provider]
            for key in links:
                if host in key.lower():
                    # Simulate processing delay
                    time.sleep(5)  # 5 seconds
                    return jsonify(result=links[key])
        
        return jsonify(error=True)
    
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
