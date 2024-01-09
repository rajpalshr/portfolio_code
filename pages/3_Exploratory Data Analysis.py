
# Libraries
######################
import streamlit as st
import pandas as pd
import numpy as np
import os
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
######################

# Load custom CSS file - Github
######################
custom_css = '''
<link rel="stylesheet" href="./custom.css">
'''
st.markdown(custom_css, unsafe_allow_html=True)
######################


# Page
######################
st.set_page_config(
    page_title="Exploratory Data Analysis"
)
######################

# Image, Title
######################
st.image('./assets/eda/eda_movies.png', use_column_width=True)
st.title('Exploratory Data Analysis')
######################


# Data Frame
######################
df = pd.read_csv("./movies.csv")
######################

# Head, Shape, Info
######################
code_snippet = "df.head()"
st.code(code_snippet, language='python')
st.dataframe(df.head())

code_snippet = "df.shape"
st.code(code_snippet, language='python')
st.write("Shape:", df.shape)

code_snippet = "df.info()"
st.code(code_snippet, language='python')
st.image('./assets/eda/eda_info.png', width=400)
######################

# Transformation and Construction
######################
df = pd.read_csv('./movies_new.csv')
code_snippet = """
# feature transformation
df['release_date'] = pd.to_datetime(df['release_date'])
df['run_time'] = df['run_time'].str.replace(' min', '').astype(int)

# feature construction
df.insert(2, 'release_year', df['release_date'].dt.year)
df.insert(3, 'release_month', df['release_date'].dt.month_name())
df.insert(4, 'release_day', df['release_date'].dt.day_name())
"""
st.code(code_snippet, language='python')
st.dataframe(df.head())
######################


# Numerical and Categorical
######################
code_snippet = """
# Numerical, Categorical
num = df.select_dtypes(include=['float64', 'int64'])
cat = df.select_dtypes(include=['object', 'bool'])

numerical = len(num.columns)
categorical = len(cat.columns)

num_per = (numerical / (categorical + numerical)) * 100
cat_per = (categorical / (categorical + numerical)) * 100

labels = ['Numerical', 'Categorical']
values = [num_per, cat_per]
colors = ['#ff9999', '#66b3ff']

fig, ax = plt.subplots(figsize=(4,4))
ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal') 

plt.show();
"""
st.code(code_snippet, language='python')

num = df.select_dtypes(include=['float64', 'int64'])
cat = df.select_dtypes(include=['object', 'bool'])

numerical = len(num.columns)
categorical = len(cat.columns)

num_per = (numerical / (categorical + numerical)) * 100
cat_per = (categorical / (categorical + numerical)) * 100

labels = ['Numerical', 'Categorical']
values = [num_per, cat_per]
colors = ['#636efa', '#2F58CD']

fig, ax = plt.subplots(figsize=(3,3))
ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax.axis('equal')  

plt.show();
st.pyplot(fig)
######################


# Describe, Duplicate, Null
######################
code_snippet = "df.describe()"
st.code(code_snippet, language='python')
st.dataframe(df.describe())

code_snippet = "df.duplicated().sum()"
st.code(code_snippet, language='python')
st.write("Duplicated:", df.duplicated().sum())

code_snippet = "df.isnull().sum()"
st.code(code_snippet, language='python')
st.image('./assets/eda/eda_null.png', width=300)
######################

# Analysis - Features
######################
st.info('''
### Release Year
- Release Year is a **numeric column**
- The data consists of movies from **1926 to 2023**
- Thus, we can visualize the distribution of release year using a histogram
''')
code_snippet = """
fig = px.histogram(df, 
                   x='release_year', 
                   marginal='box', 
                   title='Distribution of Release Year')
fig.update_layout(bargap=0.1)
fig.show()
"""
st.code(code_snippet, language='python')
st.image('./assets/eda/eda_release_year.png')



st.info('''
### Rating 
- Rating is a **numeric column**
- The minimum rating in the dataset is **5.3** and the maximum rating is **9.3**
- Thus, we can visualize the distribution of rating using a histogram
''')
code_snippet = """
fig = px.histogram(df, 
                   x='rating', 
                   marginal='box', 
                   title='Distribution of Rating')
fig.update_layout(bargap=0.1)
fig.show()
"""
st.code(code_snippet, language='python')
st.image('./assets/eda/eda_rating.png')



st.info('''
### Run Time
- Runtime is a **numeric column**
- The minimum runtime in the dataset for the movie is **67 mins** and the maximum runtime is **334 mins**
- Thus, we can visualize the distribution of runtime using a histogram
''')
code_snippet = """
# runtime
fig = px.histogram(df, 
                   x='run_time', 
                   marginal='box', 
                   title='Distribution of Runtime')
fig.update_layout(bargap=0.1)
fig.show()
"""
st.code(code_snippet, language='python')
st.image('./assets/eda/eda_runtime.png')



st.info('''
### Budget
- Budget is a **numeric column**
- The minimum budget in the dataset is **12K** and the maximum rating is **300M**
- Thus, we can visualize the distribution of budget using a histogram
''')
code_snippet = """
# budget
fig = px.histogram(df, 
                   x='budget', 
                   marginal='box', 
                   title='Distribution of Budget')
fig.update_layout(bargap=0.1)
fig.show()
"""
st.code(code_snippet, language='python')
st.image('./assets/eda/eda_budget.png')


st.info('''
### Revenue
- Revenue is a **numeric column**
- The minimum budget in the dataset is **10K** and the maximum rating is **2.9B** 
- Thus, we can visualize the distribution of revenue using a histogram
''')
code_snippet = """
# revenue 
fig = px.histogram(df, 
                   x='revenue', 
                   marginal='box', 
                   title='Distribution of Revenue')
fig.update_layout(bargap=0.1)
fig.show()
"""
st.code(code_snippet, language='python')
st.image('./assets/eda/eda_revenue.png')


st.info('''
### Budget vs Revenue
- One can see, most of the datapoints lie where **the budget is between 0 to 50M** and **revenue is between 0 to 500M**
- Also, with increasing budget more revenue is generated when the movies releases
''')
code_snippet = """
# budget vs bevenue
fig = px.scatter(df, 
                 title='Budget vs Revenue',
                 x='budget', 
                 y='revenue')
fig.update_layout(bargap=0.1)
fig.show()
"""
st.code(code_snippet, language='python')
st.image('./assets/eda/eda_budget_revenue.png')

 
st.info('''
### Release Month
- Release Month is a **categorical column** 
- In the month of **December**, maximum number of movies are released
- Thus, we can visualize the number of movies released for each month using a countplot
''')
code_snippet = """
# release month
monthly_counts = df['release_month'].value_counts().sort_index()

plt.figure(figsize=(8, 4))
monthly_counts.plot(kind='bar', color='#636efa')
plt.xlabel('Month')
plt.ylabel('Number of Movies')
plt.title('Number of Movies Released by Month')
plt.xticks(rotation=45)
plt.show()
"""
st.code(code_snippet, language='python')
st.image('./assets/eda/eda_release_month.png')



st.info('''
### Release Day
- Release Day is a **categorical column** 
- Maximum number of movies are released on **Friday**
- Thus, we can visualize the number of movies released by the day of the week using a countplot
''')
code_snippet = """
# release day
daily_counts = df['release_day'].value_counts().sort_index()

plt.figure(figsize=(8, 4))
daily_counts.plot(kind='bar', color='#636efa')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Movies')
plt.title('Number of Movies Released by Day of the Week')
plt.xticks(rotation=45)
plt.show()
"""
st.code(code_snippet, language='python')
st.image('./assets/eda/eda_release_day.png')



st.info('''
### Genre
- Genre is a **categorical column** 
- Maximum number of movies are released in **Drama - Genre**
- Thus, we can visualize the number of movies released for each genre using a countplot
''')
code_snippet = """
# genre
df['genre'] = df['genre'].str.split(',')
df_exploded = df.explode('genre')
genre_counts = df_exploded['genre'].str.strip().value_counts()

df_exploded['genre'] = df_exploded['genre'].str.strip()

plt.figure(figsize=(10, 6))
sns.countplot(data=df_exploded, y='genre')
plt.title('Frequency of Genres')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()
"""
st.code(code_snippet, language='python')
st.image('./assets/eda/eda_genre.png')



st.info('''
### Director
- Director is a **categorical column** 
- **Martin Scorsese** directed maximum number of movies
- Thus, we can visualize the top 10 directors with the maximum number of movies using a countplot
''')
code_snippet = """
# director
director_counts = df['director'].value_counts().head(10)

plt.figure(figsize=(8, 4))
director_counts.plot(kind='barh', color='#636efa')
plt.xlabel('Number of Movies')
plt.ylabel('Director')
plt.title('Top 10 Directors with the Maximum Number of Movies')
plt.show()
"""
st.code(code_snippet, language='python')
st.image('./assets/eda/eda_director.png')



st.info('''
### Actors
- Actors is a **categorical column** 
- **Robert De Niro** acted in maximum number of movies
- Thus, we can visualize the top 10 actors with the maximum number of movies using a countplot
''')
code_snippet = """
# actors
actor_counts = df['actors'].str.split(', ').explode().value_counts().head(10)

# Plot the horizontal bar chart for top 10 actors
plt.figure(figsize=(8, 4))
actor_counts.plot(kind='barh', color='#636efa')
plt.xlabel('Number of Movies')
plt.ylabel('Actor')
plt.title('Top 10 Actors with the Maximum Number of Movies')
plt.show()
"""
st.code(code_snippet, language='python')
st.image('./assets/eda/eda_actor.png')
######################


# Correlation
###################### 
code_snippet = """
df_corr = df[['release_year', 'rating', 'run_time', 'budget', 'revenue']] 
df_corr.head()
"""
st.code(code_snippet, language='python')
df_corr = df[['release_year', 'rating', 'run_time', 'budget', 'revenue']]
st.dataframe(df_corr.head())

code_snippet = """
plt.subplots(figsize=(4,3))
sns.heatmap(df_corr.corr(), cmap='Blues')
plt.title('Correlation Matrix');
"""
st.code(code_snippet, language='python')
plt.subplots(figsize=(4,3))
sns.heatmap(df_corr.corr(), cmap='Blues')
plt.title('Correlation Matrix')
st.pyplot(plt)

code_snippet = """
# Correlation of Revenue with Release Year
df['revenue'].corr(df['release_year'])
"""
st.code(code_snippet, language='python')
st.write('Revenue with Release Year: ', df['revenue'].corr(df['release_year']))

code_snippet = """
# Correlation of Revenue with Rating
df['revenue'].corr(df['rating'])
"""
st.code(code_snippet, language='python')
st.write('Revenue with Rating: ', df['revenue'].corr(df['rating']))

code_snippet = """
# Correlation of Revenue with Run Time
df['revenue'].corr(df['run_time'])
"""
st.code(code_snippet, language='python')
st.write('Revenue with Run Time: ', df['revenue'].corr(df['run_time']))

code_snippet = """
# Correlation of Revenue with Budget
df['revenue'].corr(df['budget'])
"""
st.code(code_snippet, language='python')
st.write('Revenue with Budget: ', df['revenue'].corr(df['budget']))
######################



######################
st.markdown('''**Q.** Which movie has the highest rating?''')
code_snippet = """
highest_rating_movie = df.loc[df['rating'].idxmax()]
df.loc[df['title'] == highest_rating_movie['title']]
"""
st.code(code_snippet, language='python')
highest_rating_movie = df.loc[df['rating'].idxmax()]
st.dataframe(df.loc[df['title'] == highest_rating_movie['title']])

st.markdown('''**Q.** Which movie has the longest runtime?''')
code_snippet = """
longest_runtime_movie = df.loc[df['run_time'].idxmax()]
df.loc[df['title'] == longest_runtime_movie['title']]
"""
st.code(code_snippet, language='python')
longest_runtime_movie = df.loc[df['run_time'].idxmax()]
st.dataframe(df.loc[df['title'] == longest_runtime_movie['title']])

st.markdown('''**Q.** What is the average rating of the movies?''')
code_snippet = """
average_rating = df['rating'].mean()
average_rating
"""
st.code(code_snippet, language='python')
average_rating = df['rating'].mean()
st.write('**Average Rating:** ', average_rating)


st.markdown('''**Q.** What is the average budget of the movies?''')
code_snippet = """
average_budget = df['budget'].mean()
average_budget
"""
st.code(code_snippet, language='python')
average_budget = df['budget'].mean()
st.write('**Average Budget:** ', average_budget)


st.markdown('''**Q.** What is the average revenue of the movies?''')
code_snippet = """
average_revenue = df['revenue'].mean()
average_revenue
"""
st.code(code_snippet, language='python')
average_revenue = df['revenue'].mean()
st.write('**Average Revenue:** ', average_revenue)
######################