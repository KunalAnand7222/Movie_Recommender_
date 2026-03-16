import streamlit as st
from recommender import fetch_details

st.markdown("""
<style>

body{
background-color:#0b0f0b;
}

.movie-title{
font-size:16px;
font-weight:600;
text-align:center;
margin-top:8px;
color:white;
}

.movie-rating{
text-align:center;
color:#22c55e;
font-weight:600;
margin-bottom:10px;
}

.movie-row-title{
font-size:28px;
font-weight:700;
margin-top:30px;
margin-bottom:10px;
color:#22c55e;
}

</style>
""", unsafe_allow_html=True)


def movie_row(title, movies):
    st.markdown(f"<div class='movie-row-title'>{title}</div>", unsafe_allow_html=True)

    valid_movies = []

    for movie in movies:
        poster = movie.get("poster")
        rating = movie.get("rating")
        
        if not poster:
            poster, rating, overview = fetch_details(movie["id"])

        if poster and str(poster) != "None" and "null" not in str(poster):
            movie["poster"] = poster
            movie["rating"] = rating if rating else "N/A"
            valid_movies.append(movie)

        if len(valid_movies) == 5:
            break

    if valid_movies:
        cols = st.columns(len(valid_movies))
        for i, movie in enumerate(valid_movies):
            with cols[i]:
                st.image(movie["poster"], use_container_width=True)
                st.markdown(
                    f"<div class='movie-title'>{movie['title']}</div>",
                    unsafe_allow_html=True
                )
                st.markdown(
                    f"<div class='movie-rating'>⭐ {movie['rating']}</div>",
                    unsafe_allow_html=True
                )