import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine

engine=create_engine('mysql+pymysql://root:mysql@localhost/do')
mycon=engine.connect()
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql"
)

mycursor = mydb.cursor()

mycursor.execute("use do ;")


if "mdf" not in st.session_state:
    st.session_state.mdf = pd.DataFrame(columns=['Date', 'Time', 'Doctor_Id', 'Department','Patient_Id', 'Medicine_prescription', 'Test_prescription', 'case_study','Diagonisation' ,'Next_consultancy_date'])
with st.form("myform",clear_on_submit=True):

    idx= st.text_input('SNO')
    location = st.date_input('date')#date
    x = st.time_input('Time',value="now" )#time
    y = st.text_input('Doctor Id' )#doctor id
    z=st.selectbox("Department",("cardiologist",'pediatricts','oncology','orthopedics','gynacology','Dermatologist','Neprologist','Radiologist'))

    demand = st.text_input('Patient_Id' )#patient id
    from_ = st.text_area('Medicine Precription')#medicine prescription
    to = st.text_area('Test Prescription' )#test prescription
    service = st.text_area('Case_study' )#case study
    diag=st.text_input("Diagonisation")
    vehicle = st.date_input('Next_consultancy_date' )#next consultancy date


    run = st.form_submit_button('Submit')

    df_new = pd.DataFrame({'Date': location, 
                            'Time': x, 
                            'Doctor_Id': y, 
                            'Department':z,
                            'Patient_Id': demand, 
                            'Medicine_prescription': from_, 
                            'Test_prescription': to,
                            'case_study': service, 
                            "Diagonisation":diag,
                            'Next_consultancy_date': vehicle, 
                            }, index=[idx])    
        
    if run:

        st.session_state.mdf = pd.concat([st.session_state.mdf, df_new], axis=0)
        st.session_state.mdf.to_csv("df.csv")
        
        my=("insert into doctorss values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data=(location,x,y,z,demand,from_,to,service,diag,vehicle)
        mycursor.execute(my,data)
        mydb.commit()

        
        
