from joblib import load
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.subplots as sp
import os
from PIL import Image
import pymysql
from pymysql import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay,accuracy_score, classification_report
from sklearn import metrics
from sklearn.metrics import confusion_matrix



st.set_page_config(page_title="Real time Analytic dashboard",page_icon="🌐")


st.sidebar.image("C:/ML projects/real_time_dashboard/NewFolder/t20.jpg",use_column_width=True)
with st.sidebar:
    st.header("🏡Home")
    st.subheader("About")
    st.write(" The celebration of cricket's infinite capacity to produce magic, where every ball could be the beginning of something extraordinary and every match could birth a story that will be told for generations")



st.title("ICC Mens T20 Worldcup DASHBOARD")
image = Image.open("C:/ML projects/real_time_dashboard/Newfolder/i1.jpg")
st.image(image)
st.write("   ")
st.write("  A symphony of willow and leather of prestigious tournament orchestrates a magnificent dance of power-hitting and tactical genius, where each delivery could spark a revolution of fortunes. The trophy itself gleams like a beacon of immortality, promising eternal glory to those brave enough to seize their moment in cricket's most exhilarating. ")


#############---------------database--------------------------------------------------------------------
conn=pymysql.connect(host='localhost',user='dharshini',password='Dnn',database='myDb')
c=conn.cursor()
def view_data():
    c.execute('SELECT * FROM icct20 ')
    data=c.fetchall()
    return data

result=view_data()
df = pd.DataFrame(result, columns=["Match_No", "Date", "Venue", "1st_Team", "2nd_Team", "Stage", "Toss_Winning", "Toss_Decision", "First_Innings_Score", "Fall_of_wickets_First_Innings", "Second_Innings_Score", "Fall_of_wickets_Second_Innings", "Winners", "Won_by", "Winning_Margin", "Top_Scorer", "Highest_Score", "Best_Bowler", "Player_Of_The_Match"])
st.header("Dataset")
# Display the dataframe in Streamlit
st.dataframe(df, use_container_width=True)



categorical_columns = ['1st_Team', '2nd_Team', 'Stage','Top_Scorer','Best_Bowler']
numerical_columns = ['First_Innings_Score', 'Second_Innings_Score']

X = df[categorical_columns + numerical_columns]
y = df['Winners']

rf_classifier= load("rf_classifier_model.joblib")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)


#############-------------------------------------------------------------------------------

def metrics():
    col1, col2, col3=st.columns(3)
    with col1:
        st.metric(label="ALL Match", value=df['Match_No'].count(), delta="ALL Match", delta_color="normal")

    with col2:
        st.metric(label="HIGHEST SCORE", value=df['Highest_Score'].min(), delta="Low Score", delta_color="inverse")

    with col3:
        st.metric(label="WICKETS", value=df['Fall_of_wickets_Second_Innings'].min(), delta="wicket", delta_color="normal")


metrics()


