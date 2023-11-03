import streamlit as st

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
