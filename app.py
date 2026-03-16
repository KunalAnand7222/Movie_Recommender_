# api="6182f9fab5aeff6bf2cb039e7f949108"
import streamlit as st
# from auth import login_page
from recommender import recommend_movies
from ui_components import movie_row
import pickle

st.set_page_config(layout="wide",page_title="MovieFlix")

movies = pickle.load(open("movies.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

st.sidebar.title("🔎 Search Movies")

search = st.sidebar.text_input("Search")

if search:
    movie_list = movies[movies["title"].str.contains(search,case=False)]
else:
    movie_list = movies.sample(10)

st.title("🎬 MovieFlix AI Recommender")

selected = st.sidebar.selectbox("Choose Movie",movie_list["title"])

if st.sidebar.button("Recommend"):
    recs = recommend_movies(selected,movies,similarity)
    movie_row("Recommended",recs)


movie_row("Trending Movies",movie_list.head(10).to_dict("records"))
