import numpy as np
import pandas as pd

movies = pd.read_csv("D:\\Machine-Learning-A-Z-Codes-Datasets\\Movie Recommendation System\\tmdb_5000_movies.csv")
credits = pd.read_csv("D:\\Machine-Learning-A-Z-Codes-Datasets\\Movie Recommendation System\\tmdb_5000_credits.csv")

#print(credits.head(2))
#print()
#print(movies.head(2))
#print()

# DATA PREPROCESSING 

movies = movies.merge(credits,on='title')
#print(movies.head(1))

# columns required for analysis:
    # genres,id,keywords,title,overview,cast,crew
    
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]
print(movies.head())

# remove null
movies.dropna(inplace=True)

# now we have to convert all these columns to lists for easier data access
import ast
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

#print(movies[['genres']])
movies['genres'] = movies['genres'].apply(convert)
#print(movies[['genres']])


# print(movies[['keywords]])
movies['keywords'] = movies['keywords'].apply(convert)
# print(movies[['keywords']])

import ast
# print(ast.literal_eval('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]'))
def convert_cast(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3 :
            L.append(i['name'])
        counter += 1
    return L

# print(movies[['cast]])
movies['cast'] = movies['cast'].apply(convert_cast)
#print(movies[['cast']])

def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director' :
            L.append(i['name'])
    return L

movies['crew'] = movies['crew'].apply(fetch_director)
# print(movies[['crew']])

movies['overview'] = movies['overview'].apply(lambda x : x.split())
#print(movies[['overview']])

def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1

movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)
movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)

# combine all columns
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

new = movies.drop(columns=['overview','genres','keywords','cast','crew'])
new['tags'] = new['tags'].apply(lambda x: " ".join(x))
# print(new.head(2))


# VECTORIZATION

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')

vector = cv.fit_transform(new['tags']).toarray()
print(vector.shape)

from sklearn.metrics.pairwise import cosine_similarity
cs = cosine_similarity(vector)
#print(cs)

# print(new[new['title'] == 'The Lego Movie'].index[0])

# main function
def recommend(movie):
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(cs[index])),reverse = True,key=lambda x : x[1]) # sorting is done on the basis of cosine similarities 
    for i in distances[1:6]:
        print(new.iloc[i[0]].title)
        
recommend('Avatar')

import pickle
pickle.dump(new,open('movies.pkl','wb'))

pickle.dump(cs,open('cs.pkl','wb'))