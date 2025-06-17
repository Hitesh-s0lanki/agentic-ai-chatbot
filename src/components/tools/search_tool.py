from langchain_community.tools.tavily_search import TavilySearchResults

class SearchTool:

    def __init__(self):
        self.tool = TavilySearchResults(max_results = 2)

    def get_tool(self):
        return self.tool