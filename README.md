# 🎵 Song Recommender System

A professional, interactive, and fully functional **Song Recommender Web Application** built with **FastAPI**, powered by **TF-IDF + Cosine Similarity**, and enriched with features like:
- ✅ Clean login system
- 🔍 Real-time song-based recommendations
- 🔗 YouTube link integration for direct listening
- 📝 User-based search logging (stored as JSON)
- 🌐 Stylish responsive UI (HTML/CSS)
- 🐳 Fully Dockerized setup

---

## 🚀 Features

- 🔐 **Login Page** to access the app by username  
- 🎶 **Search Page** to input song titles  
- 💡 **Output Page** showing top 5 similar songs with YouTube links  
- 🧠 **Text-based Recommendation System** using TF-IDF + Cosine Similarity  
- 📁 Logs each search per user into a `logs.json` file  
- 💅 Enhanced UI using modern HTML + CSS styles  

---

## 🧰 Tech Stack

- **Backend**: Python, FastAPI  
- **Frontend**: HTML, CSS, Jinja2 templates  
- **ML**: Scikit-learn (TF-IDF, Cosine Similarity)  
- **Data**: `songdata.csv` (sampled to 5000 songs)  
- **Deployment**: Docker  

---

## 🐳 Run With Docker

### 1. Build the image
```bash
docker build -t song-recommender .
2. Run the container
bash
Copy
Edit
docker run -p 8000:8000 song-recommender
Visit: http://localhost:8000

💻 Run Locally (Without Docker)
1. Install requirements
bash
Copy
Edit
pip install -r requirements.txt
Note: Ensure python-multipart is included for form data support in FastAPI.

2. Start the app
bash
Copy
Edit
uvicorn app:app --reload
📁 Project Structure
pgsql
Copy
Edit
.
├── app.py
├── df.pkl
├── templates
│   ├── login.html
│   ├── index.html
│   └── song_output_page.html
├── static
│   └── style.css
├── songdata.csv
├── logs.json
├── Dockerfile
└── requirements.txt
✍️ Author
Vivek Chaudhari
GitHub Profile (← replace with your actual link)

📜 License
This project is licensed under the MIT License.

📝 Future Improvements
Add user signup with password (authentication)

Store logs in database (e.g., SQLite or PostgreSQL)

Add search history per user UI

Real-time search suggestions

Screenshots of pages:
![image](https://github.com/user-attachments/assets/440031eb-0b93-4e79-9b57-ea50a12d7cdc)

![image](https://github.com/user-attachments/assets/b0834117-552f-4f01-96a1-3d5bbb73c438)

![image](https://github.com/user-attachments/assets/f38c5bee-9679-41a8-9990-9e955c5e72cd)


