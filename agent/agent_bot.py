from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langchain_mistralai import ChatMistralAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages: List[HumanMessage]

llm = ChatMistralAI(model="mistral-small-2603")

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    print(f"\nAI: {response.content}")
    return state

graph = StateGraph(AgentState)

graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile()

user_input = input("Enter: ")
agent.invoke({"messages": [HumanMessage(content=user_input)]})
