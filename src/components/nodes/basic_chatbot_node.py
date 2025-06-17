from src.components.states.chat_state import State

class BasicChatbotNode:
    def __init__(self, model):
        self.llm = model

    def process(self, state:State):
        return {"messages": self.llm.invoke(state["messages"])}
