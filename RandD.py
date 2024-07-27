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

with st.form("R AND D",clear_on_submit=True):
    dpt=st.selectbox("Department",("cardiologist",'pediatricts','oncology','orthopedics','gynacology','Dermatologist','Neprologist','Radiologist'))
    qry="select distinct(Diagonisation),count(*) as No_of_affectors from doctorss where Department='%s' group by Diagonisation;"%(dpt,)
    mydf=pd.read_sql(qry,mydb)
    st.dataframe(mydf)
    a=st.form_submit_button("submit")
    if a:
        x=mydf.Diagonisation
        y=mydf.No_of_affectors
        fig,ax=plt.subplots()
        ax.bar(x,y,color=['r','b'])
        plt.xlabel("Diagonisation")
        plt.ylabel("No_of_affectors")
        plt.legend()
        plt.grid()
        st.pyplot(fig)
