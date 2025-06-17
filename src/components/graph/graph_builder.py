from langgraph.graph import StateGraph, START, END
from src.components.states.chat_state import State
from src.components.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.grah_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
            Builds a basic chatbot graph using Langgraph.
            This method initializes a chatbot node using the 'BasicChatbotNode' class
            and intergates it into the grap. The Chatbot node is set as both the 
            entry and exit pont of the graph
        """

        ## Using the basic chatbot 
        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        # Adding the Node to Graph
        self.grah_builder.add_node("chatbot", self.basic_chatbot_node.process)

        ## Adding the Edges
        self.grah_builder.add_edge(START, "chatbot")
        self.grah_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase: str):
        """
            Sets up the specfic Graph for each usecase
        """

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        
        return self.grah_builder.compile()
            