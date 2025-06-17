from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

class WikipediaTool:

    def __init__(self):
        api_wrapper_wikipedia = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
        self.tool = WikipediaQueryRun(api_wrapper=api_wrapper_wikipedia)

    def get_tool(self):
        return self.tool