import streamlit as st


create_page = st.Page(r"C:\Users\admin\OneDrive\Desktop\streamlit\stm.py", title="Doctors page", icon=":material/add_circle:")
Pharma = st.Page(r"C:\Users\admin\OneDrive\Desktop\streamlit\Pharmacy.py", title="Pharmacy", icon=":material/delete:")
Test=st.Page(r"C:\Users\admin\OneDrive\Desktop\streamlit\test.py",title='Labouratory')
result=st.Page(r"C:\Users\admin\OneDrive\Desktop\streamlit\Test_results.py",title='Test Resuls')
rad=st.Page(r"C:\Users\admin\OneDrive\Desktop\streamlit\RandD.py",title='R&D')
pg = st.navigation([create_page, Pharma,Test,result,rad])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()