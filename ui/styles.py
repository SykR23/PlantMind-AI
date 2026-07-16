import streamlit as st


class Styles:

    @staticmethod
    def load():

        st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

.stChatMessage{
    border-radius:12px;
    padding:10px;
}

.stExpander{
    border-radius:12px;
}

div[data-testid="stMetric"]{
    text-align:center;
}

section[data-testid="stSidebar"]{
    border-right:1px solid #303030;
}

</style>
""", unsafe_allow_html=True)