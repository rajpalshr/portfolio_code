# Libraries
######################
import streamlit as st
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import warnings
warnings.filterwarnings('ignore')
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
    page_title="Analysis Using SQL"
)
######################


# Image, Title
######################
st.image('./assets/sql/sql_movies.png', use_column_width=True)
st.title('Analysis Using SQL')
######################

# Dataframe
######################
df = pd.read_csv("./movies.csv")
######################


# Engine
######################
engine = create_engine('sqlite:///:memory:')
df.to_sql('movies', con=engine, index=False, if_exists='replace')
######################



# Query 0
######################
query0 = "SELECT * FROM movies LIMIT 5"
result_df0 = pd.read_sql(query0, con=engine)
st.code(query0)
st.write(result_df0)
######################

# Query 1
######################
query1 = "SELECT COUNT(*) AS num_rows, (SELECT COUNT() FROM pragma_table_info('movies')) AS num_columns FROM movies"
result_df1 = pd.read_sql(query1, con=engine)
st.code(query1)
st.write(result_df1)
######################

# Query 2
######################
query2 = "SELECT title, genre, rating FROM movies WHERE rating > 8.5"
result_df2 = pd.read_sql(query2, con=engine)
st.code(query2)
st.write(result_df2)
######################

# Query 3
######################
query3 = "SELECT director, COUNT(*) as num_movies FROM movies GROUP BY director ORDER BY num_movies DESC LIMIT 10"
result_df3 = pd.read_sql(query3, con=engine)
st.code(query3)
st.write(result_df3)
######################

# Query 4
######################
query4 = "SELECT title, release_date FROM movies WHERE release_date BETWEEN '1990-01-01' AND '1999-12-31'"
result_df4 = pd.read_sql(query4, con=engine)
st.code(query4)
st.write(result_df4)
######################

# Query 5
######################
query5 = "SELECT genre, AVG(rating) as avg_rating FROM movies GROUP BY genre ORDER BY avg_rating DESC"
result_df5 = pd.read_sql(query5, con=engine)
st.code(query5)
st.write(result_df5)
######################

# Query 6
######################
query6 = "SELECT title, actors FROM movies WHERE actors LIKE '%Al Pacino%'"
result_df6 = pd.read_sql(query6, con=engine)
st.code(query6)
st.write(result_df6)
######################

# Query 7
######################
query7 = "SELECT director, COUNT(*) as num_movies FROM movies GROUP BY director HAVING num_movies > 5"
result_df7 = pd.read_sql(query7, con=engine)
st.code(query7)
st.write(result_df7)
######################

# Query 8
######################
query8 = "SELECT title, budget, revenue FROM movies WHERE revenue > budget ORDER BY (revenue - budget) DESC LIMIT 10"
result_df8 = pd.read_sql(query8, con=engine)
st.code(query8)
st.write(result_df8)
######################

# Query 9
######################
query9 = "SELECT genre, COUNT(*) as num_movies FROM movies GROUP BY genre ORDER BY num_movies DESC LIMIT 5"
result_df9 = pd.read_sql(query9, con=engine)
st.code(query9)
st.write(result_df9)
######################

# Query 10
######################
query10 = "SELECT director, AVG(rating) as avg_rating FROM movies GROUP BY director ORDER BY avg_rating DESC LIMIT 5"
result_df10 = pd.read_sql(query10, con=engine)
st.code(query10)
st.write(result_df10)
######################

# Query 11
######################
query11 = "SELECT title, run_time FROM movies ORDER BY run_time DESC LIMIT 10"
result_df11 = pd.read_sql(query11, con=engine)
st.code(query11)
st.write(result_df11)
######################

# Query 12
######################
query12 = "SELECT genre, SUM(revenue) as total_revenue FROM movies GROUP BY genre ORDER BY total_revenue DESC"
result_df12 = pd.read_sql(query12, con=engine)
st.code(query12)
st.write(result_df12)
######################

# Query 13
######################
query13 = "SELECT release_date, COUNT(*) as num_movies FROM movies GROUP BY release_date ORDER BY release_date"
result_df13 = pd.read_sql(query13, con=engine)
st.code(query13)
st.write(result_df13)
######################

# Query 14
######################
query14 = "SELECT title, director FROM movies WHERE director LIKE '%Spielberg%'"
result_df14 = pd.read_sql(query14, con=engine)
st.code(query14)
st.write(result_df14)
######################

# Query 15
######################
query15 = "SELECT title, genre, rating FROM movies WHERE genre LIKE '%Crime%' AND rating > 8.0"
result_df15 = pd.read_sql(query15, con=engine)
st.code(query15)
st.write(result_df15)
######################

# Query 16
######################
query16 = "SELECT DISTINCT genre FROM movies"
result_df16 = pd.read_sql(query16, con=engine)
st.code(query16)
st.write(result_df16)
######################

# Query 17
######################
query17 = "SELECT director, AVG(revenue) as avg_revenue FROM movies GROUP BY director HAVING COUNT(*) > 5 ORDER BY avg_revenue DESC"
result_df17 = pd.read_sql(query17, con=engine)
st.code(query17)
st.write(result_df17)
######################

# Query 18
######################
query18 = "SELECT title, genre FROM movies WHERE genre LIKE '%Drama%' AND genre NOT LIKE '%Crime%'"
result_df18 = pd.read_sql(query18, con=engine)
st.code(query18)
st.write(result_df18)
######################

# Query 19
######################
query19 = "SELECT title, release_date FROM movies WHERE release_date > '2000-01-01' ORDER BY release_date LIMIT 5"
result_df19 = pd.read_sql(query19, con=engine)
st.code(query19)
st.write(result_df19)
######################

# Query 20
######################
query20 = "SELECT director, COUNT(*) as num_movies FROM movies WHERE rating > 9.0 GROUP BY director ORDER BY num_movies DESC LIMIT 3"
result_df20 = pd.read_sql(query20, con=engine)
st.code(query20)
st.write(result_df20)
######################