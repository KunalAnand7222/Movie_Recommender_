import streamlit as st
import streamlit.components.v1 as components

def movie_row(title, movies):

    st.markdown(f"<h3 style='color:white;margin-top:30px;'>{title}</h3>", unsafe_allow_html=True)

    html = """
    <style>
    body {
        background-color: #0b0f19;
    }

    .scroll-container {
        display: flex;
        overflow-x: auto;
        gap: 20px;
        padding: 15px;
        scroll-behavior: smooth;
    }

    .scroll-container::-webkit-scrollbar {
        height: 8px;
    }

    .scroll-container::-webkit-scrollbar-thumb {
        background: #444;
        border-radius: 10px;
    }

    .movie-card {
        min-width: 180px;
        flex: 0 0 auto;
        transition: transform 0.3s ease;
        cursor: pointer;
    }

    .movie-card:hover {
        transform: scale(1.1);
    }

    .movie-card img {
        width: 180px;
        border-radius: 10px;
    }

    .movie-title {
        color: white;
        font-size: 14px;
        margin-top: 8px;
        text-align: center;
    }
    </style>

    <div class="scroll-container">
    """

    for movie in movies:

        poster = movie.get("poster")
        if not poster:
            poster = "https://via.placeholder.com/300x450?text=Movie"

        title = movie.get("title", "")

        html += f"""
        <div class="movie-card">
            <img src="{poster}">
            <div class="movie-title">{title}</div>
        </div>
        """

    html += "</div>"

    components.html(html, height=350, scrolling=True)
