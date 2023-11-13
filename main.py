import streamlit as st
import pandas  # Third party library to read CSV data. It's already installed with streamlit.

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg", width=500)

with col2:
    st.title('Marcin Karbowniczyn')
    content = """
    Hi, my name is Marcin. I try to become a full time programmer. I mainly focus on backend/software development using Python and Node.js. 
    This website was built in Python with an usage of Streamlit web framework.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

df = pandas.read_csv('data.csv', sep=';')

col3, col4 = st.columns(2)
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])

# import streamlit as st
#
# st.set_page_config(layout="wide")
#
# col1, col2, col3 = st.columns([0.3, 0.3, 0.7])
#
# with col1:
#     pass
#
# with col2:
#     st.image("images/photo.jpeg", width=500)
#
# with col3:
#     st.title('Marcin Karbowniczyn')
#     content = """
#     Hi, my name is Marcin. I try to become a full time programmer. I mainly focus on backend/software development using Python and Node.js.
#     This website was built in Python with an usage of Streamlit
#     web framework.
#     """
#     st.info(content)
# st.write('Below you can find some of the apps I have built in Python. Feel free to contact me!')
