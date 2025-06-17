import streamlit as st
import os

from src.components.config.configfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get("DEFAULT", "PAGE_TITLE", ""), layout="wide")
        st.header("🤖 " + self.config.get("DEFAULT", "PAGE_TITLE", ""))

        with st.sidebar:
            # Get option from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            llm_choice = st.selectbox("Select LLM", llm_options)
            usecase_choice = st.selectbox("Select Use Case", usecase_options)

            # Dynamically load model options based on LLM choice
            if llm_choice.lower() == "groq":
                model_options = self.config.get_groq_model_options()
                model_choice = st.selectbox("Select Groq Model", model_options)
            else:
                model_options = self.config.get_openai_model_options()
                model_choice = st.selectbox("Select OpenAI Model", model_options)

            # API Key input
            api_key = st.text_input("Enter API Key", type="password")

            # Taily API key for tool bot
            tavily_api_key = ''
            if usecase_choice == "Chatbot with Tool":
                tavily_api_key = st.text_input("Enter Tavily API Key", type="password")

                if not tavily_api_key:
                    st.warning("⚠️ Please Provide Your tavily API key")

            # Store user selections
            self.user_controls = {
                "llm": llm_choice,
                "usecase": usecase_choice,
                "model": model_choice,
                "api_key": api_key,
                "tavily_api_key":tavily_api_key
            }

        # Main area input
        user_input = st.chat_input("What on Your Mind ?")

        return self.user_controls, user_input

