
---

# 🌍 IP & Network Info Viewer

A lightweight Flask-based web app that displays:

* **Local (LAN) IP**
* **Public IP**
* **ISP / Organization**
* **Country**

It provides a clean UI in the browser and automatically returns JSON output when accessed via `curl`.

---

## 🚀 Features

* 📡 Shows your **local network IP**
* 🌐 Fetches **public IP, ISP/Org & country** using `ipapi.co`
* 🖥️ Smooth, animated UI built with **Vibe Code**
* 🧩 Auto JSON output when using `curl`
* 🐳 Fully Dockerized — no manual Python setup needed
* ⚡ Lightweight & fast

---

## 📁 Project Structure

```
├── app.py               # Main Flask application
├── local_ip_app.py      # Alternate UI-focused version
├── requirements.txt     # Dependencies
├── Dockerfile           # Docker build instructions
```

---

## 🐳 Running with Docker (Recommended)

### 1️⃣ Build the Docker image

```sh
docker build -t ip-info-app .
```

### 2️⃣ Run the container

```sh
docker run -p 8080:8080 -e HOST_IP=$(hostname -I | awk '{print $1}') ip-info-app
```

Open in browser:

```
http://localhost:8080
```

---

## 📡 JSON Output (for curl)

```sh
curl http://localhost:8080
```

Example response:

```json
{
  "local_ip": "192.168.x.x",
  "public_ip": "xx.xx.xx.xx",
  "org": "Your ISP",
  "country": "Your Country"
}
```

---

## 🤝 Credits

* UI inspired & crafted using **Vibe Code**
* Built with **Flask**
* Public network data powered by **ipapi.co**

---
