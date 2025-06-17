import os
import streamlit as st
from langchain_openai import ChatOpenAI

class OpenAILLM:
    """
    Wrapper around OpenAI's ChatOpenAI model for Streamlit applications.
    """
    def __init__(self, user_controls: dict[str, str]):
        """
        user_controls should contain:
          - api_key: Your OpenAI API key
          - model: The OpenAI model name to use
        """
        self.api_key = user_controls.get("api_key", "")
        self.model_name = user_controls.get("model", "")

    def get_llm_model(self) -> ChatOpenAI:
        """
        Instantiates and returns the ChatOpenAI model.
        Raises a ValueError with Streamlit error if API key is missing.
        """
        api_key = self.api_key or os.getenv("OPENAI_API_KEY", "")
        if not api_key:
            st.error("Error: API key is required to call OpenAI.")
            raise ValueError("API key is required to call OpenAI.")

        # Ensure environment variable is set
        os.environ["OPENAI_API_KEY"] = api_key

        try:
            llm = ChatOpenAI(
                model=self.model_name,
                openai_api_key=api_key,
                temperature=0.7  # adjust as needed
            )
            return llm
        except Exception as e:
            error_msg = f"OpenAI initialization error: {e}"
            st.error(error_msg)
            raise ValueError(error_msg)