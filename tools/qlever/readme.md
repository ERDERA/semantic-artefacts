# QLever for HOOM-Orphanet RDF Querying

[![QLever](https://img.shields.io/badge/SPARQL-QLever-blue)](https://github.com/ad-freiburg/qlever)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-enabled-blue)](https://hub.docker.com/r/adfreiburg/qlever)

QLever is an open-source, high-performance SPARQL engine for querying RDF data.  
This repository includes a local RDF dataset (e.g., **HOOM-Orphanet**) and a preconfigured `QLeverfile` to allow quick setup and querying.

> 💡 For more information, visit the [official QLever GitHub](https://github.com/ad-freiburg/qlever).

---

## What's Included

- `QLeverfile` — defines indexing and runtime settings
- `.ttl`, `.nt`, or `.rdf` RDF files — local dataset (e.g., `hoom_orphanet_2.3.ttl`)
- Optional NGINX reverse proxy config

---

## Quick Setup (Localhost)

### 1. Install Dependencies

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv \
  ca-certificates curl gnupg lsb-release \
  docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin nginx
```

<details>
<summary>🛠️ If Docker isn't installed yet, click to expand</summary>

```bash
# Add Docker GPG key and repository
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
```
</details>

---

### 2. Set Up Python Environment and QLever Control

```bash
python3 -m venv qlever-venv
source qlever-venv/bin/activate
pip install --upgrade pip
pip install qlever
```

---

### 3. Index and Run QLever

From the directory that contains the `QLeverfile` and RDF files:

```bash
source qlever-venv/bin/activate

qlever get-data
qlever index
qlever start
qlever ui
```

---

### 4. Access QLever

| Type         | URL                                                                 |
|--------------|----------------------------------------------------------------------|
| SPARQL       | [http://localhost:7025](http://localhost:7025)                      |
| Web UI       | [http://localhost:9000/ui/?index=hoom_orphanet](http://localhost:9000/ui/?index=hoom_orphanet) |

---

## 🔐 Optional: Enable HTTPS with Let’s Encrypt

If you're using a domain (e.g., `qlever.yourdomain.org`), set up HTTPS with:

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d qlever.yourdomain.org
```

---

## 📁 Example Folder Structure

```
.
├── QLeverfile
├── hoom_orphanet_2.3.ttl
└── README.md
```

---

## 🧠 Tips

- Use `/ui/?index=hoom_orphanet` to directly open the UI with the correct dataset
- SPARQL queries must use prefixes defined in your RDF or in `*.prefix-definitions`
- Docker is required to run QLever backend and UI containers

---

## 📝 License

This project is provided under the [MIT License](LICENSE).

---

