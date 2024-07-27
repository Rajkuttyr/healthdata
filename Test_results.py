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

if "mdf2" not in st.session_state:
    st.session_state.mdf2 = pd.DataFrame(columns=['Date', 'Time', 'Doctor_Id','Patient_Id','Tests','Results'])
with st.form("myform",clear_on_submit=True):

    idx= st.text_input('SNO')
    location = st.date_input('date')#date
    x = st.time_input('Time',value="now" )#time
    y = st.text_input('Doctor Id' )#doctor id
    

    demand = st.text_input('Patient_Id' )#patient id
    z=st.selectbox("Tests",("Gulcose",'Creatine','Hemoglobin'))
    results=st.text_input("Values")
    


    run = st.form_submit_button('Submit')

    df_new1 = pd.DataFrame({'Date': location, 
                            'Time': x, 
                            'Doctor_Id': y, 
                            
                            'Patient_Id': demand,
                            'Tests':z, 
                            'Results': results, 
                             
                            }, index=[idx])    
        
    if run:

        st.session_state.mdf2 = pd.concat([st.session_state.mdf2, df_new1], axis=0)
        st.session_state.mdf2.to_csv("df5.csv")
        st.dataframe(st.session_state.mdf2)
        st.session_state.mdf2.to_sql('test_result',mycon,index=False,if_exists='replace')
        
        my=("insert into test_result values(%s,%s,%s,%s,%s,%s);")
        data=(location,x,y,demand,z,results)
        mycursor.execute(my,data)
        mydb.commit()
