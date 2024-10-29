import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from joblib import load
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import streamlit_option_menu as op
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay,accuracy_score, classification_report
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import scipy as skplt
from wordcloud import WordCloud
import datetime
import pymysql




st.set_page_config(page_title="hospital information System",page_icon="🌐")
st.title("👨‍⚕️HOSPITAL MANAGEMENT SYSTEM👩‍⚕️🚑")
st.write(" Connecting Care, Optimizing Outcomes ")


st.sidebar.image("G:/data science work/intern 1/logo1.jpg", use_column_width=True )
with st.sidebar:
    st.write("🏡Home")
  




###### loaded model-----------------------
rf_classifier=load("rf_classify_model1.joblib")

df=pd.read_excel("healthcaredataa.xlsx")
Categorical_columns = ['Gender','Medical Condition', 'Doctor', 'Insurance Provider','Test Results','Hospital']
numerical_columns = ['Age']

X = df[Categorical_columns + numerical_columns]
y = df['Medical Condition']

required_columns = Categorical_columns + numerical_columns
###########-----------------------------------------------------------------------------------------

###########-------------------------------------------------------------------
class hospital:
    @staticmethod
    def connection():
        conn=pymysql.connect(host='127.0.0.1',user='root',password='',database='hospital_management')
        return conn
    ###---------------------------------
    @staticmethod
    def appoint_data(date, time, name, age, medical_issue, gender, phone_no, address):
        conn=hospital.connection()
        try:
            cursor=conn.cursor()
            query = """INSERT INTO patient (date, time, name, age, medical_issue, gender, phone_no, address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(query, (date, time, name, age, medical_issue, gender, phone_no, address))  
            conn.commit()
            st.success("Your Appointment saved successfully!")
            


        except Exception as e:
            st.error(f"An error occurred: {e}")
    
        finally:
            conn.close()
    ###--------------------------------------
    @staticmethod
    def patient_appoint_data(doctor, doctor_name, name, date, time, issue, address, reschedule, date1, time1, issue1):
        conn=hospital.connection()
        try:
            cursor=conn.cursor()
            query = """INSERT INTO patient_appointment (doctor, doctor_name, name, date, time, issue, address, reschedule, date1, time1, issue1) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(query, (doctor, doctor_name, name, date, time, issue, address, reschedule, date1, time1, issue1))  # Replace with actual data
            conn.commit()
            st.success("Your online Appointment saved successfully!")


        except Exception as e:
            st.error(f"An error occurred: {e}")
    
        finally:
            conn.close()
    ###------------------------------------------------
    @staticmethod
    def doctor_appoint_data( doctor1, doctor_name1, d_name, d_date, d_time, d_address, d_reschedule, d_date1, d_time1):
        conn=hospital.connection()
        try:
            cursor=conn.cursor()
            query = """INSERT INTO doctor_appointment (doctor1, doctor_name1, d_name, d_date, d_time, d_address, d_reschedule, d_date1, d_time1) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(query, (doctor1, doctor_name1, d_name, d_date, d_time, d_address, d_reschedule, d_date1, d_time1))  # Replace with actual data
            conn.commit()
            st.success("Your Online Doctor Appointment saved successfully!")

  

        except Exception as e:
            st.error(f"An error occurred: {e}")
    
        finally:
            conn.close()
#######--------------------------------------------------------------
    @staticmethod
    def new_doctor_appoint_data(name, age, gender, department, bloodgrp, phone_no, address, aadhaar, pan_no):
        conn=hospital.connection()
        try:
            cursor=conn.cursor()
            query = """INSERT INTO add_doctors (n_name, n_age, n_gender, n_department, bloodgrp, n_phone_no, n_address, n_aadhaar, n_pan_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (name, age, gender, department, bloodgrp, phone_no, address, aadhaar, pan_no))  
            conn.commit()
            st.success(" New Doctor attendances saved successfully!")

  

        except Exception as e:
            st.error(f"An error occurred: {e}")
    
        finally:
            conn.close()
#############--------------------------------------------------------------
    @staticmethod
    def new_nurse_appoint_data(name, age, gender, department, bloodgrp, phone_no, address, aadhaar, pan_no):
        conn=hospital.connection()
        try:
            cursor=conn.cursor()
            query = """INSERT INTO add_nurse (name, age, gender, department, bloodgrp, phone_no, address, aadhaar, pan_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (name, age, gender, department, bloodgrp, phone_no, address, aadhaar, pan_no))  
            conn.commit()
            st.success(" New Nurse data saved successfully!")

  

        except Exception as e:
            st.error(f"An error occurred: {e}")
    
        finally:
            conn.close()

    
    #############--------------------------------------------------------------
    @staticmethod
    def Insurance_data(name, age, gender, phone_no, address, Insurance, Insurance1, medicine, medicine1, tablet, Amount):
        conn=hospital.connection()
        try:
            cursor=conn.cursor()
            query = """INSERT INTO medicine_data (name, age, gender, phone_no, address, Insurance, Insurance1, medicine, medicine1, tablet, Amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (name, age, gender, phone_no, address, Insurance, Insurance1, medicine, medicine1, tablet, Amount))  
            conn.commit()
            st.success(" Your Medicine saved successfully!")

  

        except Exception as e:
            st.error(f"An error occurred: {e}")
    
        finally:
            conn.close()



############------------------------------------------------------------------------------------------------------
option=st.sidebar.selectbox("Main Menu",("Patient","Doctor","Nurse","Pharmacy"))
st.sidebar.subheader("ABOUT")

if option=="Patient":
##--------------------------------------------------------------
    tab1,tab2,tab3,tab4=st.tabs(["🌡️💉Reception👩‍⚕️","🏥 Patient Appointment","👨‍⚕️👩‍⚕️ Doctor Appointment","Dashboard"])
    
    with tab1:
    

        st.header(" Patient Admission")

        date=st.date_input("Select the Date", datetime.date.today())

        time=st.time_input("Select the Time", datetime.time(8, 45))

        name=st.text_input("Name", " ")

        age=st.text_input("Age",key="Age1")

        medical_issue=st.text_input("Health Issue", " ",key="issue1")

        gender=st.text_input("Gender",key= "gender1")

        phone_no=st.text_input("Phone Number",key="number1")

        address=st.text_input("Address",key="address1")

        if st.button(label="Submit",key='npatientdata_submit'):
            if all([date, time, name, age, medical_issue, gender,phone_no, address]):
                hospital.appoint_data(date, time, name, age, medical_issue, gender,phone_no, address)
            else:
                st.warning("Please fill out all required fields.")


    with tab2:   
        st.header("Online Patient Appointment")
        columns = df.columns.tolist() 
        doctor= st.selectbox("choose the Doctor ", columns)
        unique_value =df[doctor].unique()
        doctor_name= st.selectbox("Select Doctor", unique_value)
   
        name=st.text_input("Name",key= "name1 ")

        date=st.date_input("Select the Date", datetime.date.today(),key="date_input1")

        time=st.time_input("Select the Time", datetime.time(8, 45),key="time_input1")

        issue=st.text_input("Health Issue", " ",key="healthissue1")

        address=st.text_input("Address","  ",key="patientaddress1")

        reschedule=st.radio("Reschedule the Date?", ("YES", "NO"))

        date1 = None
        time1 = None
        issue1 = None 

        if reschedule == "YES":
            date1=st.date_input("Select the Date", datetime.date.today(),key="date2")
            time1=st.time_input("Select the Time", datetime.time(8, 45),key="time2")
            issue1=st.text_input("Health Issue", " ",key="issue2")


        if st.button(label="Submit",key='patient_submit'):
            if all([doctor, doctor_name, name, date, time, issue, address]):
                hospital.patient_appoint_data(doctor, doctor_name, name, date, time, issue, address, reschedule, date1, time1, issue1)
            else:
                st.warning("Please fill out all required fields.")

        st.write("")

    with tab3:
         columns = df.columns.tolist() 
         doctor1= st.selectbox("choose  Doctor ", columns,key='unique_key_3')
         unique_value =df[doctor1].unique()
         doctor_name1= st.selectbox("Select Doctor", unique_value,key='unique_key_4')

         d_name=st.text_input("Name", " ",key='d_name1')

         d_date=st.date_input("Select the Date", datetime.date.today(),key='d_unique_key_5')

         d_time=st.time_input("Select the Time", datetime.time(8, 45),key='unique_key_6')

         d_address=st.text_input("Address","  ",key="Address2")

         d_reschedule=st.radio("Reschedule the Date?", ("YES", "NO"),key='unique_key_7')

         d_date1 = None
         d_time1 = None

         if d_reschedule == "YES":
             d_date1=st.date_input("Select the Date", datetime.date.today(),key='unique_key_8')
             d_time1=st.time_input("Select the Time", datetime.time(8, 45),key='unique_key_9')
    
         if st.button(label="Submit",key='doctor_submit'):
            if all([doctor1, doctor_name1, d_name, d_date, d_time, d_address]):
                hospital.doctor_appoint_data(doctor1, doctor_name1, d_name, d_date, d_time, d_address, d_reschedule, d_date1, d_time1)
         else:
             st.warning("Please fill out all required fields.")
         st.write("")
    
   
##--------------------------------------------------------------

    with tab4:
        if option=="Patient":
            health=st.sidebar.multiselect(
            label="select data",
            options=df.columns.unique(),
            default=df.columns.unique())
            match1=df.columns.isin(health)
            filter_df = df[health]

            if all(col in health for col in required_columns):
                X = filter_df[Categorical_columns + numerical_columns]
                y = filter_df['Medical Condition'] 
    
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)
    
                X_encoded = pd.get_dummies(X_test, columns=Categorical_columns, drop_first=True)
    

                missing_cols = set(rf_classifier.feature_names_in_) - set(X_encoded.columns)
                for col in missing_cols:
                  X_encoded[col] = 0  

   
                X_encoded = X_encoded[rf_classifier.feature_names_in_]
    
                y_pred = rf_classifier.predict(X_encoded)
##--------------------------------------------------------------
        st.header("Dashboard")
        col1,col2=st.columns(2)
        with col1:
            fig1 = px.bar(df, y='Age', x='Blood Type',color_discrete_sequence=['#b3ff66'], title='Blood Group')

            st.plotly_chart(fig1, use_container_width=True)
            plt.close()
            
        with col2:
            fig = px.pie(df, names='Medical Condition',title='Diseases')
            st.plotly_chart(fig)

            st.write("")

        col3,col4=st.columns(2)
        with col3:
            st.write("")
            plt.figure(figsize=(7, 7))
            plt.hist(df['Admission Type'], bins=5, color='LightCyan', edgecolor='red')
            plt.xticks(rotation=70)
            plt.title('Admission',color='red', fontsize=30)
            st.write("")
            st.pyplot(plt,use_container_width=True)
            plt.close()

        with col4:
              st.write("")
              plt.figure(figsize=(7, 7))
              df['Insurance Provider'].value_counts().sort_values().plot(color='red')
              plt.title("Insurance Provider",color='green', fontsize=30)
              st.write("")
              st.pyplot(plt,use_container_width=True)
              plt.close()


        st.write("")
        from wordcloud import WordCloud
        text = " ".join(title for title in df.Doctor) 
        word =WordCloud(collocations = False, background_color = 'lightyellow', width=3048, height=2080).generate(text)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(word, interpolation='bilinear')
        ax.set_title("Doctors", fontsize=20, color ='red')
        ax.axis("off")
        st.pyplot(fig,use_container_width=True)
        plt.close()



   






elif option =="Doctor":
    tab1,tab2=st.tabs(["👩‍⚕️Doctors List", "👨‍⚕️👩‍⚕️Add Doctors"])
    with tab1:
        st.subheader("Doctors")
        df=pd.read_excel("healthcaredataa.xlsx")
        st.dataframe(df[["Doctor", "Gender"]], use_container_width=True)

    with tab2:
        st.subheader("New Doctors Admission")

        name=st.text_input("Name",key="unique_name12")

        age=st.text_input("Age",key="n_age")

        gender=st.text_input("Gender",key="n_gender")
        
        department=st.text_input("Specialization",key="specify")

        bloodgrp=st.text_input("Blood Group",key="blood")

        phone_no=st.text_input("Phone Number",key="phone1")

        address=st.text_input("Address",key="newd_Address")

        aadhaar=st.text_input("AADHAAR NO",key="aadhar_no")

        pan_no=st.text_input("Pan_number",key="pan_no1")

        
        if st.button(label="Submit",key='n_doctor_submit'):
            if all([name, age, gender, department, bloodgrp, phone_no, address, aadhaar, pan_no ]):
                hospital.new_doctor_appoint_data(name, age, gender, department, bloodgrp, phone_no, address, aadhaar, pan_no)
        else:
             st.warning("Please fill out all required fields.")
        st.write("")




elif option=="Nurse":
    st.subheader("Nurse")
    name=st.text_input("Name",key="unique_name123")

    age=st.text_input("Age",key="ns_age")

    gender=st.text_input("Gender",key="ns_gender")
        
    department=st.text_input("Specialization",key="ns_specify")

    bloodgrp=st.text_input("Blood Group",key="ns_blood")

    phone_no=st.text_input("Phone Number",key="ns_phone1")

    address=st.text_input("Address",key="ns_newd_Address")

    aadhaar=st.text_input("AADHAAR NO",key="ns_aadhar_no")

    pan_no=st.text_input("Pan_number",key="ns_pan_no1")

        
    if st.button(label="Submit",key='nurse_doctor_submit'):
        if all([name, age, gender, department, bloodgrp, phone_no, address, aadhaar, pan_no ]):
            hospital.new_nurse_appoint_data(name, age, gender, department, bloodgrp, phone_no, address, aadhaar, pan_no)
    else:
        st.warning("Please fill out all required fields.")
        st.write("")




elif option=="Pharmacy":
    st.header("👩‍⚕️Bill Payment")

    name=st.text_input("Name", " ",key="pat_name")

    age=st.text_input("Age",key="pat_age")

    gender=st.text_input("Gender",key="pat_gender")

    phone_no=st.text_input("Phone Number",key="pat_phone1")

    address=st.text_input("Address",key="pat_Address")


    columns = df.columns.tolist() 
    Insurance= st.selectbox("choose Insurance Provider ", columns)
    unique_value =df[Insurance].unique()
    Insurance1= st.selectbox("Select Insurance Provider", unique_value)

    columns = df.columns.tolist() 
    medicine= st.selectbox("choose medication ", columns,key='unique_key_31')
    unique_value =df[medicine].unique()
    medicine1= st.selectbox("Select Medicine", unique_value,key='unique_key_41')
        
    tablet=st.text_input("Additional tablets",key="tablet1")
        
    Amount=st.text_input("Total Amount",key="amount")

    if st.button(label="Submit",key='Insurance_submit'):
        if all([name, age, gender, phone_no, address, Insurance, Insurance1, medicine, medicine1, tablet, Amount]):
            hospital.Insurance_data(name, age, gender, phone_no, address, Insurance, Insurance1, medicine, medicine1, tablet, Amount)
    else:
        st.warning("Please fill out all required fields.")
        st.write("")



