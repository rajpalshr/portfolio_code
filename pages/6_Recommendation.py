
# Libraries
######################
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
import warnings
warnings.filterwarnings('ignore')
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
######################

# Page
######################
st.set_page_config(
    page_title="Movie Recommendation"
)
######################


# Load custom CSS file - Github
######################
custom_css = '''
<link rel="stylesheet" href="./custom.css">
'''
st.markdown(custom_css, unsafe_allow_html=True)
######################


# Title
######################
st.title('Movie Recommendation')
######################


# Movie Recommendation
######################
def fetch_poster(movie_title):
    url = "https://api.themoviedb.org/3/search/movie?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&query={}".format(movie_title)
    data = requests.get(url)
    data = data.json()
    if data['results']:
        movie_data = data['results'][0]
        poster_path = movie_data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        return None

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster using the movie title
        recommended_movie_posters.append(fetch_poster(movies.iloc[i[0]].title))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

movies = joblib.load(open('movie_list.joblib', 'rb'))
similarity = joblib.load(open('similarity.joblib', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
######################


# Show Code
######################
with st.expander("Show Code"):
    # Data Frame
    ######################
    df = pd.read_csv("./movies.csv")
    ######################

    # Head
    ######################
    code_snippet = "df.head()"
    st.code(code_snippet, language='python')
    st.dataframe(df.head())
    ######################

    # Feature Engineering
    ######################
    code_snippet = """
    df.insert(0, 'movie_id', range(1, len(df) + 1))
    df = df[['movie_id', 'title', 'genre', 'director', 'actors']]
    """
    st.code(code_snippet, language='python')
    df.insert(0, 'movie_id', range(1, len(df) + 1))
    df = df[['movie_id', 'title', 'genre', 'director', 'actors']]

    code_snippet = "df.head()"
    st.code(code_snippet, language='python')
    st.dataframe(df.head())

    code_snippet = """
    df['genre'] = df['genre'].apply(lambda x: [genre.strip() for genre in x.split(',')])
    df['director'] = df['director'].apply(lambda x: [x.strip().replace(" ", "")])
    df['actors'] = df['actors'].apply(lambda x: [actor.strip().replace(" ", "") for actor in x.split(',')])

    df['tags'] = df['genre'] + df['director'] + df['actors']
    df.drop(columns=['genre', 'director', 'actors'], inplace=True)
    df['tags'] = df['tags'].apply(lambda x: " ".join(x))
    """
    st.code(code_snippet, language='python')
    df['genre'] = df['genre'].apply(lambda x: [genre.strip() for genre in x.split(',')])
    df['director'] = df['director'].apply(lambda x: [x.strip().replace(" ", "")])
    df['actors'] = df['actors'].apply(lambda x: [actor.strip().replace(" ", "") for actor in x.split(',')])

    df['tags'] = df['genre'] + df['director'] + df['actors']
    df.drop(columns=['genre', 'director', 'actors'], inplace=True)
    df['tags'] = df['tags'].apply(lambda x: " ".join(x))


    code_snippet = "df.head()"
    st.code(code_snippet, language='python')
    st.dataframe(df.head())
    
    
    code_snippet = """
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(max_features=5000,stop_words='english')
    vector = cv.fit_transform(df['tags']).toarray()

    from sklearn.metrics.pairwise import cosine_similarity
    similarity = cosine_similarity(vector)

    def recommend(movie):
    index = df[df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(df.iloc[i[0]].title)
    """
    st.code(code_snippet, language='python')

    code_snippet = "recommend('GoodFellas')"
    st.code(code_snippet, language='python')
    st.image('./assets/rec/rec_out.png', width=300)
######################
