from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import urllib.parse
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load dataset
df = pd.read_pickle("df.pkl")
if 'combined_features' not in df.columns:
    df['combined_features'] = df['text']

# In-memory user session (simple, not secure)
user_sessions = {}

# Function to get YouTube search link
def get_youtube_link(song_title):
    query = urllib.parse.quote_plus(f"{song_title} song")
    return f"https://www.youtube.com/results?search_query={query}"

# Recommender function
def recommend(song):
    song = song.lower()
    song_matches = df[df['song'].str.lower() == song]
    if song_matches.empty:
        return []

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['combined_features'])

    idx = song_matches.index[0]
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()

    similar_indices = cosine_sim.argsort()[-6:-1][::-1]
    results = []

    for i in similar_indices:
        title = df.iloc[i]['song']
        results.append({
            "title": title,
            "youtube_link": get_youtube_link(title)
        })
    return results

# Helper to log user search
def log_search(username, song_name):
    log_entry = {"username": username, "searched_song": song_name}
    log_path = "logs.json"
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            data = json.load(f)
    else:
        data = []
    data.append(log_entry)
    with open(log_path, "w") as f:
        json.dump(data, f, indent=4)

@app.get("/", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login_page.html", {"request": request})

@app.post("/login", response_class=RedirectResponse)
async def login_user(request: Request, username: str = Form(...)):
    user_sessions["current_user"] = username
    return RedirectResponse(url="/input", status_code=302)

@app.get("/input", response_class=HTMLResponse)
async def main_page(request: Request):
    username = user_sessions.get("current_user")
    if not username:
        return RedirectResponse(url="/")
    return templates.TemplateResponse("song_input_page.html", {"request": request, "username": username})

@app.post("/recommend", response_class=HTMLResponse)
async def recommend_songs(request: Request, song_name: str = Form(...)):
    username = user_sessions.get("current_user")
    if not username:
        return RedirectResponse(url="/")
    log_search(username, song_name)
    recommendations = recommend(song_name)
    return templates.TemplateResponse("song_output_page.html", {
        "request": request,
        "results": recommendations,
        "song_name": song_name,
        "username": username
    })
