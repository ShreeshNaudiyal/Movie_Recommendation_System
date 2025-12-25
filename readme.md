# 🎬 Movie Recommendation System (ML Project)

A **content-based movie recommendation system** built using **Machine Learning** and **Python**, with a simple **Streamlit web interface**.  
The system recommends movies similar to a selected movie based on textual features like genres, keywords, cast, and crew.

---

## 🚀 Project Overview

This project uses **Natural Language Processing (NLP)** techniques and **cosine similarity** to recommend movies.  
It demonstrates the **complete ML pipeline** — from data preprocessing to model building and deployment-ready UI.

---

## 🧠 How It Works

1. Movie metadata (genres, overview, keywords, cast, crew) is preprocessed
2. Text features are combined into a single tag column
3. **CountVectorizer** converts text into numerical vectors
4. **Cosine similarity** measures similarity between movies
5. Top 5 most similar movies are recommended
6. Movie posters are fetched using the **TMDB API**

---

## 🛠 Tech Stack

- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn  
- **Data Processing:** Pandas, NumPy  
- **NLP:** CountVectorizer  
- **Web App:** Streamlit  
- **API:** TMDB API  

---
