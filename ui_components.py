import streamlit as st

def movie_row(title, movies):

    st.markdown(f"""
        <h3 style='color:white;margin-top:30px;'>{title}</h3>
    """, unsafe_allow_html=True)

    # horizontal scroll container
    st.markdown("""
        <style>
        .scroll-container {
            display: flex;
            overflow-x: auto;
            gap: 20px;
            padding: 10px;
        }
        .movie-card {
            min-width: 180px;
            transition: transform 0.3s;
        }
        .movie-card:hover {
            transform: scale(1.08);
        }
        .movie-title {
            color: white;
            font-size: 14px;
            margin-top: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    container = "<div class='scroll-container'>"

    for movie in movies:

        poster = movie.get("poster")

        if not poster:
            poster = "https://via.placeholder.com/300x450?text=Movie"

        container += f"""
            <div class='movie-card'>
                <img src="{poster}" width="180"/>
                <div class='movie-title'>{movie.get("title","")}</div>
            </div>
        """

    container += "</div>"

    st.markdown(container, unsafe_allow_html=True)
