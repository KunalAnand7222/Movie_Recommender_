import pickle
import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from ui_components import movie_row

movies = pickle.load(open("movies.pkl","rb"))

text_col = 'tags' if 'tags' in movies.columns else 'tag'

@st.cache_data
def get_similarity(movies, text_col):
    try:
        return pickle.load(open("similarity.pkl","rb"))
    except:
        cv = CountVectorizer(max_features=5000, stop_words='english')
        vectors = cv.fit_transform(movies[text_col].fillna("")).toarray()
        return cosine_similarity(vectors)

similarity = get_similarity(movies, text_col)

def recommend_movies(movie_name, movies, similarity):
    movie_name = movie_name.lower()
    if movie_name not in movies['title'].str.lower().values:
        return []
    idx = movies[movies['title'].str.lower() == movie_name].index[0]
    distances = similarity[idx]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    results = []
    for i in movie_indices:
        movie = movies.iloc[i[0]]
        results.append({
            "title": movie["title"],
            "id": movie.get("id", i[0])
        })
    return results

st.sidebar.title("🔎 Search Movies")

search = st.sidebar.text_input("Search movie")

if search:
    filtered = movies[movies["title"].str.contains(search, case=False, na=False)]
    movie_list = filtered if not filtered.empty else movies.sample(10)
else:
    movie_list = movies.sample(10)

selected = st.sidebar.selectbox("Choose Movie", movie_list["title"])

st.title("🎬 MovieFlix AI Recommender")
st.caption("Discover similar movies using AI")

if "recs" not in st.session_state:
    st.session_state.recs = []

if st.sidebar.button("Recommend"):
    st.session_state.recs = recommend_movies(selected, movies, similarity)

if st.session_state.recs:
    movie_row("🎯 Recommended Movies", st.session_state.recs)

movie_row("🔥 Trending Movies", movies.sample(10).to_dict("records"))
