import streamlit as st


class SessionManager:

    @staticmethod
    def initialize():
        if "messages" not in st.session_state:
            st.session_state.messages = []

        if "knowledge_base" not in st.session_state:
            st.session_state.knowledge_base = "heat_exchangers"