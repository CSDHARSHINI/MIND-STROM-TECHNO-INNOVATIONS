import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pymysql
from pymysql import *



st.set_page_config(page_title="Healthcare Appointment System",page_icon="🌐")


st.sidebar.image("C:/ML projects/hospital appointment system/logo1.jpg", use_column_width=True)
st.sidebar.header("Home")
st.sidebar.subheader("About")
st.sidebar.write("We connects people to the resources they need each customer with an employee of most qualified to serve them")


st.title("Healthcare Appointment System      👩‍⚕️")
st.write("This is a personal guide of booking medical visits and connecting patients with doctors effortlessly. With just a few clicks you can schedule, reschedule or cancel appointments, saving time and reducing stress. This system ensures that patients receive timely care while doctors can efficiently manage their schedules.")





###########-------------------------------------------------------------------
class health:
    @staticmethod
    def connection():
        conn=pymysql.connect(host='127.0.0.1',user='root',password='',database='appoitment')
        return conn
    @staticmethod
    def appoint_data(hospital, hospital_name, doctor, doctor_name, name, date, time, issue, address, reschedule, date1, time1, issue1):
        conn=health.connection()
        try:
            cursor=conn.cursor()
            query = """INSERT INTO patient (hospital, hospital_name, doctor, doctor_name, name, date, time, issue, address, reschedule, date1, time1, issue1) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(query, (hospital, hospital_name, doctor, doctor_name, name, date, time, issue, address, reschedule, date1, time1, issue1))  # Replace with actual data
            conn.commit()
            st.success("Your Appointment saved successfully!")


        except Exception as e:
            st.error(f"An error occurred: {e}")
    
        finally:
            conn.close()

    @staticmethod
    def doctor_appoint_data(hospital1, hospital_name1, doctor1, doctor_name1, d_name, d_date, d_time, d_address, d_reschedule, d_date1, d_time1):
        conn=health.connection()
        try:
            cursor=conn.cursor()
            query = """INSERT INTO doctor (hospital1, hospital_name1, doctor1, doctor_name1, d_name, d_date, d_time, d_address, d_reschedule, d_date1, d_time1) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(query, (hospital1, hospital_name1, doctor1, doctor_name1, d_name, d_date, d_time, d_address, d_reschedule, d_date1, d_time1))  # Replace with actual data
            conn.commit()
            st.success("Your Appointment saved successfully!")

  

        except Exception as e:
            st.error(f"An error occurred: {e}")
    
        finally:
            conn.close()



df=pd.read_excel("C:/ML projects/hospital appointment system/appointmentdata.xlsx")

        

############------------------------------------------------------------------------------
tab1,tab2=st.tabs(["Patient Appointment", "Doctors Appointment"])

with tab1:
    st.subheader("Schedule your Appointment")

    columns = df.columns.tolist() 
    hospital = st.selectbox("choose the Hospital ", columns)

    unique_value =df[hospital].unique()
    hospital_name = st.selectbox("Select Hospital", unique_value)

    columns = df.columns.tolist() 
    doctor= st.selectbox("choose the Doctor ", columns)
    unique_value =df[doctor].unique()
    doctor_name= st.selectbox("Select Doctor", unique_value)
   
    name=st.text_input("Name", " ")

    date=st.date_input("Select the Date", datetime.date.today())

    time=st.time_input("Select the Time", datetime.time(8, 45))

    issue=st.text_input("Health Issue", " ",key="issue1")

    address=st.text_input("Address","  ",key="address1")

    reschedule=st.radio("Reschedule the Date?", ("YES", "NO"))

    date1 = None
    time1 = None
    issue1 = None 

    if reschedule == "YES":
        date1=st.date_input("Select the Date", datetime.date.today(),key="date2")
        time1=st.time_input("Select the Time", datetime.time(8, 45),key="time2")
        issue1=st.text_input("Health Issue", " ",key="issue2")


    if st.button(label="Submit"):
        if all([hospital , hospital_name, doctor, doctor_name, name, date, time, issue, address]):
            health.appoint_data(hospital, hospital_name, doctor, doctor_name, name, date, time, issue, address, reschedule, date1, time1, issue1)
        else:
            st.warning("Please fill out all required fields.")


    
##########-------------------------------------------------
with tab2:
    st.subheader("Schedule your Appointment")

    columns = df.columns.tolist()
    hospital1= st.selectbox("choose Hospital ", columns,key='unique_key_1')

    unique_value =df[hospital1].unique()
    hospital_name1 = st.selectbox("select the Hospital", unique_value,key='unique_key_2')
    
    columns = df.columns.tolist() 
    doctor1= st.selectbox("choose  Doctor ", columns,key='unique_key_3')
    unique_value =df[doctor1].unique()
    doctor_name1= st.selectbox("Select Doctor", unique_value,key='unique_key_4')

    d_name=st.text_input("Name", " ",key='name1')

    d_date=st.date_input("Select the Date", datetime.date.today(),key='unique_key_5')

    d_time=st.time_input("Select the Time", datetime.time(8, 45),key='unique_key_6')

    d_address=st.text_input("Address","  ",key="Address2")

    d_reschedule=st.radio("Reschedule the Date?", ("YES", "NO"),key='unique_key_7')

    d_date1 = None
    d_time1 = None

    if d_reschedule == "YES":
        d_date1=st.date_input("Select the Date", datetime.date.today(),key='unique_key_8')
        d_time1=st.time_input("Select the Time", datetime.time(8, 45),key='unique_key_9')
    
    if st.button(label="Submit",key='doctor_submit'):
        if all([hospital1 , hospital_name1, doctor1, doctor_name1, d_name, d_date, d_time, d_address]):
            health.doctor_appoint_data(hospital1, hospital_name1, doctor1, doctor_name1, d_name, d_date, d_time, d_address, d_reschedule, d_date1, d_time1)
        else:
            st.warning("Please fill out all required fields.")
