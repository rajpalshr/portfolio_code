# Libraries
######################
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from pathlib import Path
######################

# Page
######################
st.set_page_config(
    page_title="Dataset Creation"
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
st.title('Dataset Creation')
######################


# Info
#####################
st.info('''
The dataset has been created by scraping data from IMDB site. 10 csv's were created then concatenated to build the final dataframe.
''')
#####################


# Data Frame
######################
df = pd.read_csv('./movies.csv')
st.dataframe(df)
######################

# Code
######################
st.markdown("<p style='font-size:1.5rem'>Code</p>", unsafe_allow_html=True)

code_snippet = """ 
import pandas as pd
import csv
import re
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup as bs

from tmdbv3api import TMDb
from tmdbv3api import Movie

tmdb = TMDb()
tmdb.api_key = 'Your API Key'

search = Movie()

pages = ['https://www.imdb.com/list/ls006266261/', 'https://www.imdb.com/list/ls006266261/?sort=list_order,asc&st_dt=&mode=detail&page=2', 
              'https://www.imdb.com/list/ls006266261/?sort=list_order,asc&st_dt=&mode=detail&page=3', 'https://www.imdb.com/list/ls006266261/?sort=list_order,asc&st_dt=&mode=detail&page=4',
              'https://www.imdb.com/list/ls006266261/?sort=list_order,asc&st_dt=&mode=detail&page=5', 'https://www.imdb.com/list/ls006266261/?sort=list_order,asc&st_dt=&mode=detail&page=6',
              'https://www.imdb.com/list/ls006266261/?sort=list_order,asc&st_dt=&mode=detail&page=7', 'https://www.imdb.com/list/ls006266261/?sort=list_order,asc&st_dt=&mode=detail&page=8',
              'https://www.imdb.com/list/ls006266261/?sort=list_order,asc&st_dt=&mode=detail&page=9', 'https://www.imdb.com/list/ls006266261/?sort=list_order,asc&st_dt=&mode=detail&page=10'
             ]

num_pages = len(pages)

# all csv files
for i in range(num_pages):
    # csv
    file_csv = f'movie{i+1}.csv'
    csv_file = open(file_csv, "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["title", "release_date", "genre", "rating", "run_time", "director", "actors", "budget", "revenue"])
    
    # bs4
    url = str(pages[i])
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    
    movies = soup.find_all("div", class_="lister-item mode-detail")

    for movie in movies:
        # Headers 
        title = movie.h3.a.text
        genre = movie.find("span", class_="genre").text.strip()
        rating = movie.find('div', class_='ipl-rating-star').text.strip()
        run_time = movie.find('span', class_='runtime').text
        director = movie.find_all("p")[2].find_all("a")[0].text
        actors = movie.find_all("p")[2].find_all("a")[1:]
        actor_names = ", ".join([actor.text for actor in actors])

        movies_list = search.search(title)

        for movie_item in movies_list:
            if movie_item.title == title:
                movie_info = search.details(movie_item.id)
                budget = movie_info.budget
                revenue = movie_info.revenue
                release_date = movie_item.release_date
                print()
                break
            else:
                pass

        csv_writer.writerow([title, release_date, genre, rating, run_time, director, actor_names, budget, revenue])

    csv_file.close()

# concatenate all csv files into one
df1  = pd.read_csv('movie1.csv')
df2  = pd.read_csv('movie2.csv')
df3  = pd.read_csv('movie3.csv')
df4  = pd.read_csv('movie4.csv')
df5  = pd.read_csv('movie5.csv')
df6  = pd.read_csv('movie6.csv')
df7  = pd.read_csv('movie7.csv')
df8  = pd.read_csv('movie8.csv')
df9  = pd.read_csv('movie9.csv')
df10 = pd.read_csv('movie10.csv')

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], ignore_index=True)

df['budget'] = df['budget'].replace(0, np.nan)
df['revenue'] = df['revenue'].replace(0, np.nan)

# final csv
df.to_csv('movies.csv')
"""
st.code(code_snippet, language='python')
######################