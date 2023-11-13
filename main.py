# Z tego co rozumiem, pandas bierze dane CSV, tworzy z tego Data Frame, czyli dict type object który zawiera x rowów i y kolumn.
import streamlit as st
import pandas  # Third party library to read CSV data. It's already installed with streamlit.

st.set_page_config(layout="wide")
project_image_width = 500

empty_col_intro_left, col1, col2, empty_col_intro_right = st.columns(4)

with col1:
    st.image("images/photo.jpeg", width=450)

with col2:
    st.title('Marcin Karbowniczyn')
    content = """
    Hi, my name is Marcin. I try to become a full time programmer. I mainly focus on backend/software development using Python and Node.js. 
    This website was built in Python with an usage of Streamlit web framework.
    Below you can find some of the apps I have built in Python. Feel free to contact me!
    """
    st.info(content)

# empty_left_col_projects, centered_col, empty_right_col_projects = st.columns(3)
# with centered_col:
#     st.title('My projects')


df = pandas.read_csv('data.csv', sep=';')

empty_col_projects_left, col3, col4, empty_col_projects_right = st.columns(4)
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

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
