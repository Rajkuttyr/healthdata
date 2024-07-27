import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
from sqlalchemy import create_engine
import pymysql
import csvtosql as cs
engine=create_engine('mysql+pymysql://root:mysql@localhost/doctor')
mycon=engine.connect()
with st.form("doc"):







    date=st.date_input("Enter date")
    time=st.time_input("TIME",value="now")
    docid=st.text_input("Doctor id")
    paid=st.text_input("Patient UHID")
    option=st.selectbox("Department",("Oncologist","pediatrician","Gastroenterologist","Allergist","Anesthesiology","Psychartist","Dermatologist","Radiologist","Gynaecologist","cardiologist"))
    mp=st.text_area("Medicine prescriptions")
    test=st.text_area("Test precriptions")
    cs=st.text_area("Case studies")
    nc=st.date_input("Next Consultancy date") 
    dict1={"Date":[date],"Time":[time],"Dotor_id":[docid],"Patient_id":[paid],"Department":[option],"Medical_prescription":[mp],"Test_prescription":[test],"case_study":[cs],"Next_consultancy":[nc]}
    df1=pd.DataFrame(dict1)
    
    
    submit=st.form_submit_button("submit")
    if submit:
        df1.to_csv("ABC.csv")
        






