import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls):
        self.api_key = user_controls.get("api_key", "")
        self.model_name = user_controls.get("model", "") 

    def get_llm_model(self):
        """
            Calls the Groq API with the given prompt and returns the model's response.
            If no API key is provided, an error is shown in Streamlit and an empty string is returned.
        """

        api_key = self.api_key or os.getenv("GROQ_API_KEY", "")
        if not api_key:
            st.error("Error: API key is required to call OpenAI.")
            raise ValueError("API key is required to call OpenAI.")

        # Ensure environment variable is set
        os.environ["GROQ_API_KEY"] = api_key

        try:
            # Instantiate the ChatGroq model
            llm = ChatGroq(
                model=self.model_name,
                api_key=api_key,
            )


            # AIMessageChunk has .content attribute
            return llm

        except Exception as e:
            raise ValueError(f"Error Occured With Exception : {e}")
        