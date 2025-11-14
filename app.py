from flask import Flask, request, jsonify, render_template_string
import requests
import os

app = Flask(__name__)

def get_local_ip():
    """
    Get the host machine's LAN IP passed via environment variable.
    Fallbacks to 'Unknown' if not set.
    """
    return os.environ.get("HOST_IP", "Unknown")

def get_public_info():
    """
    Get public IP, Org, and Country from ipapi.co
    """
    try:
        resp = requests.get("https://ipapi.co/json/", timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return {
                "ip": data.get("ip", "Unknown"),
                "org": data.get("org", "Unknown"),
                "country": data.get("country_name", "Unknown")
            }
        else:
            return {"ip": "Unknown", "org": "Unknown", "country": "Unknown"}
    except Exception as e:
        return {"ip": "Unknown", "org": "Error", "country": str(e)}

@app.route("/")
def index():
    local_ip = get_local_ip()
    public_info = get_public_info()

    result = {
        "local_ip": local_ip,
        "public_ip": public_info["ip"],
        "org": public_info["org"],
        "country": public_info["country"]
    }

    # JSON output for curl
    if "curl" in request.headers.get("User-Agent", "").lower():
        return jsonify(result)

    # HTML output
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>IP & ISP Info</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: #fff;
                text-align: center;
                padding: 40px;
            }
            .card {
                background: rgba(255,255,255,0.1);
                border-radius: 16px;
                padding: 20px;
                max-width: 400px;
                margin: auto;
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            }
            h1 { margin-bottom: 20px; font-size: 2em; }
            .info { text-align: left; font-size: 1.2em; }
            .info div {
                background: rgba(0,0,0,0.2);
                padding: 12px;
                border-radius: 10px;
                margin-bottom: 10px;
            }
            footer { margin-top: 20px; font-size: 0.9em; opacity: 0.8; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🌍 Your Connection Details</h1>
            <div class="info">
                <div><b>Local IP:</b> {{ details.local_ip }}</div>
                <div><b>Public IP:</b> {{ details.public_ip }}</div>
                <div><b>Org:</b> {{ details.org }}</div>
                <div><b>Country:</b> {{ details.country }}</div>
            </div>
        </div>
        <footer>Powered by Flask + ipapi.co</footer>
    </body>
    </html>
    """
    return render_template_string(template, details=result)

if __name__ == "__main__":
    # Default Flask port 8080, listen on all interfaces
    app.run(host="0.0.0.0", port=8080)
