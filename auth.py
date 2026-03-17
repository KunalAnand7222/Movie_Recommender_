import streamlit as st
import pickle
from recommender import recommend_movies
from ui_components import movie_row, movie_popup
from ui_components import movie_row

st.set_page_config(layout="wide",page_title="MovieFlix")

movies = pickle.load(open("movies.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

st.sidebar.title("🔎 Search Movies")

search = st.sidebar.text_input("Search movie")

if search:
    movie_list = movies[movies["title"].str.contains(search,case=False)]
else:
    movie_list = movies.sample(10)

st.title("🎬 MovieFlix AI Recommender")

selected = st.sidebar.selectbox("Choose Movie",movie_list["title"])

if st.sidebar.button("Recommend"):
    recs = recommend_movies(selected,movies,similarity)
    movie_row("Recommended Movies",recs)

if "watchlist" not in st.session_state:
    st.session_state.watchlist=[]

st.sidebar.title("⭐ Watchlist")

for m in st.session_state.watchlist:
    st.sidebar.write(m)

movie_row("Trending Movies",movie_list.head(10).to_dict("records"))

if "popup_movie" in st.session_state:
    movie_popup(st.session_state.popup_movie)
