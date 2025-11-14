from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    lan_ip = request.remote_addr

    template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>IP & ISP Info</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #667eea, #764ba2, #ff6a00);
            background-size: 600% 600%;
            animation: gradientBG 15s ease infinite;
            color: #fff;
        }
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .card {
            background: rgba(0,0,0,0.6);
            border-radius: 20px;
            padding: 40px;
            max-width: 500px;
            width: 90%;
            box-shadow: 0 12px 30px rgba(0,0,0,0.3);
            text-align: center;
        }
        h1 {
            margin-bottom: 20px;
            font-size: 2.2em;
            letter-spacing: 1px;
        }
        .info {
            font-size: 1.2em;
            margin: 15px 0;
            padding: 15px;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.1);
            transition: background 0.3s;
        }
        .info:hover {
            background: rgba(255, 255, 255, 0.2);
        }
        .label {
            font-weight: bold;
            color: #ffd369;
        }
        footer {
            margin-top: 20px;
            font-size: 0.85em;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🌍 Your Network Info</h1>
        <div class="info"><span class="label">LAN IP:</span> {{ lan_ip }}</div>
        <div class="info"><span class="label">Public IP:</span> <span id="public_ip">Loading...</span></div>
        <div class="info"><span class="label">ISP / Org:</span> <span id="org">Loading...</span></div>
        <div class="info"><span class="label">Country:</span> <span id="country">Loading...</span></div>
        <footer>Powered by Quintet Solutions</footer>
    </div>

    <script>
        fetch("https://ipapi.co/json/")
            .then(resp => resp.json())
            .then(data => {
                document.getElementById("public_ip").textContent = data.ip || "Unknown";
                document.getElementById("org").textContent = data.org || "Unknown";
                document.getElementById("country").textContent = data.country_name || "Unknown";
            })
            .catch(err => {
                document.getElementById("public_ip").textContent = "Error";
                document.getElementById("org").textContent = "Error";
                document.getElementById("country").textContent = "Error";
            });
    </script>
</body>
</html>
"""
    return render_template_string(template, lan_ip=lan_ip)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
