# 🎬 Movie Recommendation System

A **content-based movie recommender system** built using **Machine Learning** and **Streamlit**.  
It recommends movies similar to the selected one using **cosine similarity**.

## 🔧 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- TMDB API

## 📊 How it works
- Movies are vectorized using CountVectorizer
- Cosine similarity is used to find similar movies
- Posters are fetched using TMDB API

## ▶️ Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
