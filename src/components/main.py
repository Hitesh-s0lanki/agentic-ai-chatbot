import streamlit as st
from src.components.ui.load_ui import LoadStreamlitUI
from src.components.llm.groq_llm import GroqLLM
from src.components.llm.openai_llm import OpenAILLM

from src.components.graph.graph_builder import GraphBuilder
from src.components.ui.display_result import DisplayResult

def load_langgraph_agentic_ai_app():
    """
        Loads and run the langgraph agentic ai application with streamlit UI.
        This function initializes the UI, handles user input, configures the LLM model,
        sets up the graph based on the selected use case, and displays the output while 
        implementing exception handling for robustness
    """

    # load Ui 
    ui = LoadStreamlitUI()
    user_controls, user_input = ui.load_streamlit_ui()

    if st.session_state.get("is_fetch_button_clicked", False):
        user_input = user_controls['time_frame']

    # Only proceed if user has entered a prompt and clicked Submit
    if user_input:
        try:
            # Determine which LLM to use
            llm_choice = user_controls.get("llm", "").lower()
            if llm_choice == "groq":
                llm_wrapper = GroqLLM(user_controls)
            elif llm_choice in ("openai", "openai gpt", "gpt-3.5-turbo", "gpt-4", "gpt-4o", "gpt-4o-mini"):  # adjust as needed
                llm_wrapper = OpenAILLM(user_controls)
            else:
                st.error(f"Unsupported LLM choice: {user_controls.get('llm')}")
                return

            # Instantiate the LLM model
            llm_model = llm_wrapper.get_llm_model()

            usecase = user_controls.get("usecase", "")
            if not usecase:
                raise ValueError("Use Case is not define")

            graph_builder = GraphBuilder(model=llm_model)

            graph = graph_builder.setup_graph(usecase)
            DisplayResult(usecase=usecase, graph=graph, user_message=user_input).display_result_on_ui()
            

        except ValueError as ve:
            # LLM initialization or validation error
            st.error(str(ve))
        except Exception as e:
            # Catch-all for unexpected exceptions
            st.error(f"Unexpected error: {e}")