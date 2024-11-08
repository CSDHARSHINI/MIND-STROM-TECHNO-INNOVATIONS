from joblib import load
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.subplots as sp
import pymysql
from pymysql import *
import streamlit as st
import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay,accuracy_score, classification_report
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import scipy as skplt
from wordcloud import WordCloud

st.set_page_config(page_title="Analytic dashboard",page_icon="🌐")

st.sidebar.header("Query")
#############---------------database--------------------------------------------------------------------
conn=pymysql.connect(host='localhost',user='dharshini',password='Dnn',database='myDb')
c=conn.cursor()
def view_data():
    c.execute('SELECT * FROM icct20 ')
    data=c.fetchall()
    return data

result=view_data()
df = pd.DataFrame(result, columns=["Match_No", "Date", "Venue", "1st_Team", "2nd_Team", "Stage", "Toss_Winning", "Toss_Decision", "First_Innings_Score", "Fall_of_wickets_First_Innings", "Second_Innings_Score", "Fall_of_wickets_Second_Innings", "Winners", "Won_by", "Winning_Margin", "Top_Scorer", "Highest_Score", "Best_Bowler", "Player_Of_The_Match"])

categorical_columns = ['1st_Team', '2nd_Team', 'Stage','Top_Scorer','Best_Bowler']
numerical_columns = ['First_Innings_Score', 'Second_Innings_Score']

X = df[categorical_columns + numerical_columns]
y = df['Winners']

rf_classifier= load("rf_classifier_model.joblib")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)
#------------------------------------------------
st.header("Query Database")
st.write("     ")


st.sidebar.header("Select the Match")
spot=st.sidebar.multiselect(label="filter the data",options=df["Match_No"].unique(),default=df["Match_No"].unique())
match1=df[df["Match_No"].isin(spot)]
st.write("Select the Match")
st.dataframe(match1)

st.sidebar.header("Select the Team1")
root=st.sidebar.multiselect(label="filter the data",options=df["1st_Team"].unique(),default=df["1st_Team"].unique())
matches=df[df["1st_Team"].isin(root)]
st.write("Team-1")
st.dataframe(matches)

st.sidebar.header("Select the Team2")
t2=st.sidebar.multiselect(label="filter the data",options=df["2nd_Team"].unique(),default=df["2nd_Team"].unique())
matches1=df[df["2nd_Team"].isin(t2)]
st.write("Team-2")
st.dataframe(matches1)

 
st.sidebar.header("Select the Stages")
d1=st.sidebar.multiselect(label="filter the data ",options=df["Stage"].unique(),default=df["Stage"].unique())
mt=df[df["Stage"].isin(d1)]
st.write("Stages")
st.dataframe(mt)
 
st.sidebar.header("Select the Winners")
td2=st.sidebar.multiselect(label="filter the data",options=df["Winners"].unique(),default=df["Winners"].unique())
mat1=df[df["Winners"].isin(td2)]
st.write("Winners")
st.dataframe(mat1)

st.sidebar.header("Select the Bowlers")
ted=st.sidebar.multiselect(label="filter the data",options=df["Best_Bowler"].unique(),default=df["Best_Bowler"].unique())
bow=df[df["Best_Bowler"].isin(ted)]
st.write("Bowlers")
st.dataframe(bow)


st.sidebar.header("Select the Highest score")
hs=st.sidebar.multiselect(label="filter the data",options=df["Highest_Score"].unique(),default=df["Highest_Score"].unique())
score=df[df["Highest_Score"].isin(hs)]
st.write("Highest score")
st.dataframe(score)


#######-----------------------------------------------------------------------
st.sidebar.header("Select the winning score diff")
option1= st.sidebar.multiselect(
    label="filter the data",
    options= df['Winning_Margin'].unique(),default=df['Winning_Margin'].unique())
win_diff_df = df[df['Winning_Margin'].isin(option1)]

st.write("select the stage:", win_diff_df)
