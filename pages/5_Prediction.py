
# Libraries
######################
import streamlit as st
import pandas as pd
import numpy as np
import joblib
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
    page_title="Movie Revenue Prediction"
)
######################

# Image, Title
######################
st.image('./assets/eda/eda_movies.png', use_column_width=True)
st.title('Movie Revenue Prediction')
######################

# Model
######################
def load_model():
    regressor = joblib.load('model_regressor.joblib')
    preprocessor = joblib.load('preprocessor.joblib')
    scaler = joblib.load('scaler.joblib')
    return regressor, preprocessor, scaler

regressor, preprocessor, scaler = load_model()
######################



# Movie Prediction
######################
genres = [
    'Crime, Drama', 'Biography, Crime, Drama', 'Crime, Drama, Mystery',
    'Drama, Mystery, War', 'Drama', 'Biography, Drama, History',
    'Crime, Thriller', 'Adventure, Mystery, Thriller',
    'Adventure, Comedy, Sci-Fi', 'Action, Crime, Drama'
]

st.write("""### Information required to predict the revenue""")

genre = st.selectbox("Genre", genres)
rating = st.slider("Rating", 0.0, 10.0, 5.0)
run_time = st.slider("Run Time (minutes)", 60, 240, 120)
budget = st.slider("Budget (Millions)", 10, 300, 100)

if st.button("Calculate Revenue"):
        X = pd.DataFrame([[genre, rating, run_time, budget]], columns=['genre', 'rating', 'run_time', 'budget'])
        X_encoded = preprocessor.transform(X)
        X_scaled = scaler.transform(X_encoded)

        revenue = regressor.predict(X_scaled)
        st.subheader(f"The estimated revenue is ${revenue[0]:,.2f}")
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
    # Select
    df = df[['genre', 'rating', 'run_time', 'budget', 'revenue']]
    """
    st.code(code_snippet, language='python')

    code_snippet = "df['run_time'] = pd.to_numeric(df['run_time'].str.replace(' min', ''))"
    st.code(code_snippet, language='python')

    code_snippet = "df.isnull().sum()"
    st.code(code_snippet, language='python')
    st.image('./assets/pred/pred_null.png', width=300)

    code_snippet = """
    # Encode
    categorical_features = ['genre']
    preprocessor = ColumnTransformer(transformers=[('cat', OneHotEncoder(), categorical_features)], remainder='passthrough')
    X_encoded = preprocessor.fit_transform(X)
    """
    st.code(code_snippet, language='python')

    code_snippet = """
    # Scale
    numerical_features = ['rating', 'run_time', 'budget']
    scaler = StandardScaler(with_mean=False)
    X_scaled = scaler.fit_transform(X_encoded)
    """
    st.code(code_snippet, language='python')
    ######################


    # Linear Regression Model
    ######################
    code_snippet = """
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Create and train the Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    """
    st.code(code_snippet, language='python')


    code_snippet = """
    # Evaluate the model
    y_pred = model.predict(X_test)
    from sklearn.metrics import mean_squared_error, r2_score

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")
    """
    st.code(code_snippet, language='python')
    ######################
######################