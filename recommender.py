# import requests

# API_KEY="6182f9fab5aeff6bf2cb039e7f949108"

import requests
import streamlit as st

API_KEY = "6182f9fab5aeff6bf2cb039e7f949108"

@st.cache_data
def fetch_details(movie_id):

    try:

        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

        response = requests.get(url, timeout=5)

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            poster = "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            poster = "https://via.placeholder.com/500x750?text=No+Image"

        rating = data.get("vote_average", "N/A")
        overview = data.get("overview", "No description available")

        return poster, rating, overview

    except:

        return (
            "https://via.placeholder.com/500x750?text=No+Image",
            "N/A",
            "No description available"
        )

# import requests

def fetch_trailer(movie_id):

    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}"

        response = requests.get(url, timeout=5)

        data = response.json()

        for v in data.get("results", []):
            if v.get("type") == "Trailer":
                return "https://youtube.com/watch?v=" + v.get("key")

        return None

    except requests.exceptions.RequestException:
        return None

def recommend_movies(title,movies,similarity):

    idx=movies[movies["title"]==title].index[0]
    distances=similarity[idx]

    movie_list=sorted(list(enumerate(distances)),
                      reverse=True,
                      key=lambda x:x[1])[1:10]

    results=[]

    for i in movie_list:

        movie_id=movies.iloc[i[0]].id

        poster,rating,overview=fetch_details(movie_id)
        trailer=fetch_trailer(movie_id)

        results.append({
        "title":movies.iloc[i[0]].title,
        "poster":poster,
        "rating":rating,
        "overview":overview,
        "trailer":trailer
        })

    return results