from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper

class ArxivTool:

    def __init__(self):
        api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=2, doc_content_chars_max=500)
        self.tool = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

    def get_tool(self):
        return self.tool