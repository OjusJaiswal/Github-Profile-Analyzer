import requests
from collections import Counter
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import plotly.graph_objs as go
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

GITHUB_API = "https://api.github.com/users/{}/repos"

# ---------- GitHub API Functions ----------
def fetch_repos(username):
    url = GITHUB_API.format(username)
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

def analyze_repos(repos):
    language_counter = Counter()
    repo_stats = []

    for repo in repos:
        language = repo.get("language")
        if language:
            language_counter[language] += 1

        repo_stats.append({
            "name": repo.get("name"),
            "stars": repo.get("stargazers_count"),
            "forks": repo.get("forks_count"),
            "size": repo.get("size")
        })

    return {
        "languages": language_counter,
        "repos": repo_stats
    }

# ---------- Plotly Chart Function ----------
def generate_language_chart(language_counter):
    labels = list(language_counter.keys())
    values = list(language_counter.values())

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.4)])
    fig.update_layout(title="Top Languages Used")
    return fig.to_html(full_html=False)

# ---------- FastAPI Routes ----------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, username: str = Form(...)):
    repos = fetch_repos(username)
    if repos is None:
        return templates.TemplateResponse("error.html", {"request": request, "message": "GitHub user not found."})

    analysis = analyze_repos(repos)
    chart_html = generate_language_chart(analysis["languages"])

    return templates.TemplateResponse("result.html", {
        "request": request,
        "username": username,
        "repos": analysis["repos"],
        "chart": chart_html
    })