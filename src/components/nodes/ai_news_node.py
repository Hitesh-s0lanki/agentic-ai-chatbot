from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:
    def __init__(self, model):
        """
            Initialize the AI news node with API keys for Tavily and OpenAI
        """
        self.tavily = TavilyClient()
        self.llm = model
        self.state = {}

    def fetch_news(self, state:dict) -> dict:
        """
            Fetch AI news based on the specified frequency

            Args:
                state (dict): the state dictinonary containing 'frequency'

            Returns: 
                dict: Updated state with 'news_date'key containing fetched news.
        """

        frequency = state['messages'][0].content.lower()
        self.state['frequency'] = frequency
        time_range_map = {'daily':'d', 'weekly': 'w', 'monthly': 'm', 'year':'y'}
        days_map = {'daily': 1, 'weekly': 7, 'monthly': 30, 'year': 366}

        response = self.tavily.search(
            query="Top Artifical Intelligence (AI) technology news India and globally",
            topic="news",
            time_range=time_range_map[frequency],
            include_answer="advanced",
            max_results=20,
            days=days_map[frequency]
        )

        self.state['news_data'] = response.get('results', [])
        
        return state
    
    def summarize_news(self, state:dict) -> dict:
        """
            Summarize the fetched news using an LLM.

            Args:
                state (dict): the state dictionary containing 'news_data'.

            Returns:
                dict: Updated state with 'summary' key containing the summarized news.
        """

        news_items = self.state['news_data']

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """
                Summarize AI news articles into markdown format. For each item include:
             
                - Date in **YYYY-MM-DD** format in IST timezone
                - Concise sentences summary from latest news 
                - Sort news by the date wise (latest first)
                - Source URL as link

                Usformat:
                ### [Date]
                - [Summary].(URL) 
            """),
            ("user", "Articles:\n{articles}")
        ])

        article_str = "\n\n".join([
            f"Content: {item.get('content', '')}\nURL: {item.get('url', "")}\nDate: {item.get('published_date', '')}" for item in news_items
        ])

        response = self.llm.invoke(prompt_template.format(articles=article_str))

        state['summary'] = response.content
        self.state['summary'] = state['summary']
        return self.state

    def save_result(self, state):
        frequency = self.state['frequency']
        summary = self.state['summary']
        filename = f"./news/{frequency}_summary.md"
        with open(filename, 'w') as f:
            f.write(f"# {frequency.capitalize()} AI news Summary\n\n")
            f.write(summary)
        
        self.state['filename'] = filename
        return self.state