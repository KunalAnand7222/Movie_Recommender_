# api="6182f9fab5aeff6bf2cb039e7f949108"
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

movies = pickle.load(open("movies.pkl","rb"))

try:
    similarity = pickle.load(open("similarity.pkl","rb"))
except:
    cv = CountVectorizer(max_features=5000,stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()
    similarity = cosine_similarity(vectors)

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
