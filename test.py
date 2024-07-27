import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql"
)

mycursor = mydb.cursor()

mycursor.execute("use do ;")

with st.form("Pharmacy",clear_on_submit=True):
    ptid=st.text_input("Patient_Id")
    qry="select Test_prescription from doctorss where Patient_Id='%s';"%(ptid,)
    mydf2=pd.read_sql(qry,mydb)
    
    b=st.form_submit_button("submit")
    if b:
        st.dataframe(mydf2)

        