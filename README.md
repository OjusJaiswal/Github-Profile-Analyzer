# 🔍 GitHub Profile Analyzer

A web-based tool that analyzes a GitHub user's public repositories and visualizes their most-used programming languages and repo statistics.

---

## 🚀 Features

- View a user's most-used programming languages
- Interactive pie chart using Plotly
- Tabular stats: stars, forks, repo sizes
- Built with FastAPI + Jinja2 + Plotly

---

## 🛠️ Tech Stack

- Backend: FastAPI
- Frontend: Jinja2 Templates + CSS
- Charts: Plotly
- Deployment: Render / Replit / Localhost

---

## 📦 Setup Instructions

```bash
git clone https://github.com/OjusJaiswal/github-profile-analyzer.git
cd github-profile-analyzer
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
Then open your browser at:
👉 http://127.0.0.1:8000