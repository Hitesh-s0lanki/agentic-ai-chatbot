from src.components.tools.search_tool import SearchTool
from src.components.tools.arxiv_tool import ArxivTool
from src.components.tools.wikipedia_tool import WikipediaTool
from langgraph.prebuilt import ToolNode

class Tools:

    def __init__(self):
        self.tools = []

    def get_tools(self):

        # Using the Search tool
        search_tool = SearchTool()
        self.tools.append(search_tool.get_tool())

        # Research Paper tool
        arxiv_tool = ArxivTool()
        self.tools.append(arxiv_tool.get_tool())

        # Wikipedia
        wikipedia_tool = WikipediaTool()
        self.tools.append(wikipedia_tool.get_tool())

        return self.tools
    
    def create_tools_node(self):
        """
            Creating and returning a tools node for the graph
        """

        # Load all the tools 
        self.get_tools()

        return ToolNode(tools=self.tools)
    