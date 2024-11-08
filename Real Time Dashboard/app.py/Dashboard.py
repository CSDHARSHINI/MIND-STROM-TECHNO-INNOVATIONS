from joblib import load
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.subplots as sp
import pymysql
from pymysql import *
import streamlit as st
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay,accuracy_score, classification_report
from sklearn import metrics
from sklearn.metrics import confusion_matrix



st.set_page_config(page_title="Analytic dashboard",page_icon="🌐")

st.sidebar.header("Dashboard")
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
encoder = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
    

X_train_cat = encoder.fit_transform(X_train[categorical_columns])
X_train_encoded = pd.DataFrame(
    np.hstack([X_train_cat, X_train[numerical_columns].values]),
    columns=list(encoder.get_feature_names_out(categorical_columns)) + numerical_columns
)

X_test_cat = encoder.transform(X_test[categorical_columns])
X_test_encoded = pd.DataFrame(
    np.hstack([X_test_cat, X_test[numerical_columns].values]),
    columns=list(encoder.get_feature_names_out(categorical_columns)) + numerical_columns
)


train_columns = X_train_encoded.columns

missing_cols = set(train_columns) - set(X_test_encoded.columns)
for col in missing_cols:
    X_test_encoded[col] = 0

X_test_encoded = X_test_encoded[train_columns]

y_pred = rf_classifier.predict(X_test_encoded)


################-----------------------------------------------------
def metrics():
    col1, col2, col3=st.columns(3)
    with col1:
        st.metric(label="ALL Match", value=df['Match_No'].count(), delta="ALL Match", delta_color="normal",)

    # Column 2 - Sales Metric
    with col2:
        st.metric(label="HIGHEST SCORE", value=df['Highest_Score'].min(), delta="Low Score", delta_color="inverse")

    # Column 3 - Customers Metric
    with col3:
        st.metric(label="WICKETS", value=df['Fall_of_wickets_Second_Innings'].min(), delta="wicket", delta_color="normal")

metrics()


##########---------------------------------------------------------------------


st.sidebar.header("Select the Match")
option1= st.sidebar.multiselect(
    label="Filter the Data",
    options= df['Match_No'].unique(),default=df['Match_No'].unique())


############---------------------------------------
st.sidebar.header("Select the Stage")
option1= st.sidebar.multiselect(
    label="Filter the Data",
    options= df['Stage'].unique(),default=df['Stage'].unique())

####------------------------------------------
def bar():
    plt.figure(figsize=(8, 7))
    df['Stage'].value_counts().sort_values().plot(kind='barh', color='pink')
    plt.title('DIFFERENT STAGES', color ='orange')
    plt.xlabel('USAGE', color='maroon')
    plt.ylabel('STAGES', color='maroon')
    st.pyplot(plt,use_container_width=True)
    plt.close()
bar()

col1,col2=st.columns(2)
with col1:
    fig = px.pie(df, df['2nd_Team'],title='TEAMS')
    fig.update_traces()
    st.plotly_chart(fig,use_container_width=True)
    
with col2:
    fig = px.pie(df, names='Toss_Decision',title='TOSS DECISION')
    st.plotly_chart(fig)

def line():
    plt.figure(figsize=(14, 8))
    df_sorted = df.sort_values(by='First_Innings_Score')
    plt.plot(df['Date'], df_sorted['First_Innings_Score'], marker='o', color='m', label='First Innings Score')
    plt.title('First Innings Score', fontsize=30)
    plt.xlabel('Date')
    plt.xticks(rotation=70)
    plt.yticks(rotation=20)
    plt.ylabel('First Innings Score')
    st.pyplot(plt,use_container_width=True)
    plt.close()

line()

def linegraph1():
    st.write(" ")
    df_sorted = df.sort_values(by='Second_Innings_Score')
    plt.figure(figsize=(15, 6))
    plt.plot(df['Date'], df_sorted['Second_Innings_Score'], marker='o', color='r', label='Second Innings Score')
    plt.title('Second Innings Score', fontsize=30) 
    plt.xlabel('Date')
    plt.xticks(rotation=70)
    plt.yticks(rotation=10)
    plt.ylabel('Second Innings Score')
    plt.legend()
    st.pyplot(plt,use_container_width=True)
    plt.close()

linegraph1()


def word():
    st.write(" ")
    from wordcloud import WordCloud
    text = " ".join(title for title in df['Player_Of_The_Match'])
    wordcloud = WordCloud(background_color = 'lightblue',width=800, height=400).generate(text)
    plt.figure(figsize=(10,8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.title("BEST PLAYERS",color='maroon', fontsize=25)
    plt.axis("off")
    st.pyplot(plt,use_container_width=True)
    plt.close()

word()

def bow():
    st.write(" ")
    from wordcloud import WordCloud
    text = " ".join(title for title in df['Best_Bowler'])
    wordcloud = WordCloud(background_color = 'lightgreen',width=800, height=400).generate(text)
    plt.figure(figsize=(10,8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.title("BEST BOWLERS",color='blue', fontsize=25)
    plt.axis("off")
    st.pyplot(plt,use_container_width=True)
    plt.close()

bow()

def confusion(y_test, y_pred):
    conf_matrix = confusion_matrix(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)

# Display in Streamlit
    st.subheader("Confusion Matrix")
    st.text(conf_matrix)

    st.subheader("Accuracy Score")
    st.text(f"Accuracy: {accuracy*100:.2f}%")


    st.subheader("Classification Report")
    st.text(class_report)

confusion(y_test, y_pred)

def heatmp(y_test, y_pred):
    conf_matrix = confusion_matrix(y_test, y_pred)
    st.subheader("Confusion Matrix Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', ax=ax)
    st.pyplot(fig)

heatmp(y_test, y_pred)



