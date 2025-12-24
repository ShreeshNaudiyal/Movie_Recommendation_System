import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url, timeout=5)  # Added timeout
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750.png?text=No+Image"  # fallback image
    except Exception as e:
        print(f"Failed to fetch poster: {e}")
        return "https://via.placeholder.com/500x750.png?text=Error"

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
cs = pickle.load(open('cs.pkl', 'rb'))

movies_list = movies['title'].values

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = cs[movie_index]
    movie_scores = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_posters = []

    for i in movie_scores:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_posters.append(fetch_poster(movie_id))

    return recommend_movies, recommend_posters

# Streamlit UI
st.title('Movie Recommender System')

movie_selected = st.selectbox('Select a movie:', movies_list)

if st.button('Show Recommendation'):
    names, posters = recommend(movie_selected)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
