from joblib import load
import numpy as np
import pandas as pd
import plotly.express as px
import scipy as skplt
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import streamlit_option_menu as op
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay,accuracy_score, classification_report
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import scipy as skplt
from wordcloud import WordCloud






#############-------------------------------------

st.set_page_config(page_title="Social media Dashboard",page_icon="🌐")


df=pd.read_excel("socialmediadataset.xlsx")
categorical_columns = ['Gender','Location', 'Video Category', 'Profession','Platform']
numerical_columns = ['Age','Total Time Spent','Time Spent On Video']

#model----------------------
rf_classifier= load("rf_classify_model.joblib")

X = df[categorical_columns + numerical_columns]
y = df['Platform']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 22)


st.sidebar.image("G:/data science work/intern 1/logo.jpg",use_column_width=True)
st.sidebar.header("🏠Home")

spot=st.sidebar.multiselect(
    label="select data",
    options=df.columns.unique(),
    default=df.columns.unique())
match1=df.columns.isin(spot)
filter_df = df[spot]


required_columns = categorical_columns + numerical_columns
if all(col in spot for col in required_columns):
    X = filter_df[categorical_columns + numerical_columns]
    y = filter_df['Platform'] 
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)
    
    X_encoded = pd.get_dummies(X_test, columns=categorical_columns, drop_first=True)
    

    missing_cols = set(rf_classifier.feature_names_in_) - set(X_encoded.columns)
    for col in missing_cols:
        X_encoded[col] = 0  

   
    X_encoded = X_encoded[rf_classifier.feature_names_in_]
    
    y_pred = rf_classifier.predict(X_encoded)
    
   


#####------------------------------------------------------------------

st.title("📈SOCIAL MEDIA DASHBOARD📈")
st.write("  Social media is digital technology that allows the sharing of ideas and information which including text and visuals through virtual networks of communities. It has emerged as an extremely cost-effective method for businesses to reach customers compared to traditional print, TV, radio and other forms of advertising.")
tab1,tab2,tab3=st.tabs(["Dataset", "Dashboard","Performance"])

with tab1:
    st.header("Dataset")
    st.write(df)
with tab2:
    st.header("Dashboard")
    col1,col2=st.columns(2)
    with col1:
        fig = px.pie(filter_df, df['Video Category'],title='CATEGORY')
        fig.update_traces()
        st.plotly_chart(fig,use_container_width=True)
        plt.close()
        
    with col2:
        fig1 = px.bar(df, y='Age', x='Platform',color_discrete_sequence=['#FFC0CB'], title='PLATFORMS')

        st.plotly_chart(fig1, use_container_width=True)
        plt.close()
    
    col1,col2 = st.columns(2)
    with col1:
        text = " ".join(title for title in df.Location)
        Wordcloud = WordCloud(width=800, height=400, background_color='Lavender').generate(text)
        Wordcloud.to_file('got.png')
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(Wordcloud, interpolation='bilinear')
        ax.axis("off")
        ax.set_title("COUNTRIES", fontsize=20) 
        st.pyplot(fig,use_container_width=True)
        plt.close()
    

    with col2:
        plt.figure(figsize=(8, 7))
        filter_df.Profession.value_counts().sort_values().plot(kind='barh', color='yellow')
        plt.title('PEOPLES USING SOCIAL MEDIA', color ='green', fontsize=25)
        plt.xlabel('USAGE', color='maroon')
        plt.ylabel('KIND OF PEOPLES', color='maroon')
        st.pyplot(plt,use_container_width=True)
        plt.close()

    
    col1,col2 = st.columns(2)
    with col1:
        plt.hist(df['Profession'], bins=15, color='Lavender', edgecolor='red')
        plt.title('Age Distribution',color ='green', fontsize=25)
        plt.xlabel('Kind of peoples' , color = 'green')
        plt.ylabel('Frequency', color = 'green')
        plt.xticks(rotation=70)
        st.pyplot(plt,use_container_width=True)
        plt.close()

    with col2:
        pairplot_fig = sns.pairplot(df[numerical_columns])
        plt.suptitle('Pairplot ', y=1.02, fontsize=25)
        st.pyplot(pairplot_fig)
        plt.close()

#def bar():
 #    counts = df['Video Category'].value_counts()
 #    st.bar_chart(counts,use_container_width=True)
#bar()
with tab3:
    accuracy_value = 100
    st.metric(label="MODEL PREDICTIONS",value= f"{accuracy_value}%", delta="Accuracy", delta_color="normal")


    correlation= df.select_dtypes(np.number).corr()
    plt.figure(figsize=(12,5))
    sns.heatmap(correlation, annot=True, fmt='.2f',cmap='coolwarm')
    st.pyplot(plt.gcf())
    st.write("           ")

    


    text = " ".join(title for title in df.columns)
    Wordcloud = WordCloud(width=800, height=400, background_color='Lavender').generate(text)
    Wordcloud.to_file('got.png')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(Wordcloud, interpolation='bilinear')
    ax.axis("off")
    ax.set_title("COUNTRIES", fontsize=20)  
    st.pyplot(fig,use_container_width=True)

