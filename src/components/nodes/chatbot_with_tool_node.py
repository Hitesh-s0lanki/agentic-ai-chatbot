from src.components.states.chat_state import State

class ChatbotWithToolNode:
    """Chatbot logic enchanced with tools"""
    def __init__(self, model):
        self.llm = model

    def process(self, state:State, tools):
        """
            Process the input state and generate a response with tool integration.
        """

        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        # Stimulate tool-specfic 
        tools_response = f"Tools integration for: '{user_input}'"

        return {"messages": [llm_response, tools_response]}
    
    def create_chatbot(self, tools):
        """
            Returns a chatbot with binded tools
        """

        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
                Chatbot logic for processing the input state and returning a response
            """

            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node
