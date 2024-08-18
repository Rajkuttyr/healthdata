import streamlit as st


create_page = st.Page("stm.py", title="Doctors page", icon=":material/add_circle:")
Pharma = st.Page("Pharmacy.py", title="Pharmacy", icon=":material/delete:")
Test=st.Page("test.py",title='Labouratory')
result=st.Page("Test_results.py",title='Test Resuls')
rad=st.Page("RandD.py",title='R&D')
pg = st.navigation([create_page, Pharma,Test,result,rad])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()
