from langgraph.graph import StateGraph, START, END
from src.components.states.chat_state import State
from src.components.nodes.basic_chatbot_node import BasicChatbotNode

from src.components.tools.tools import Tools
from langgraph.prebuilt import tools_condition

from src.components.nodes.chatbot_with_tool_node import ChatbotWithToolNode

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

    def chatbot_with_tools_build_graph(self):

        # Defining the tool and tool node
        tools = Tools()
        tool_node = tools.create_tools_node()

        # Define the chatbot with tool node
        obj_chatbot_with_tools_node = ChatbotWithToolNode(self.llm)
        self.chatbot_with_tools_node = obj_chatbot_with_tools_node.create_chatbot(tools.get_tools())
        

        # Adding the Node to Graph
        self.grah_builder.add_node("chatbot", self.chatbot_with_tools_node)
        self.grah_builder.add_node("tools", tool_node)

        ## Adding the Edges
        self.grah_builder.add_edge(START, "chatbot")
        self.grah_builder.add_conditional_edges("chatbot", tools_condition)
        self.grah_builder.add_edge("tools", "chatbot")
        self.grah_builder.add_edge("chatbot", END)


    def setup_graph(self, usecase: str):
        """
            Sets up the specfic Graph for each usecase
        """

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Chatbot with Tool":
            self.chatbot_with_tools_build_graph()
        
        return self.grah_builder.compile()
            