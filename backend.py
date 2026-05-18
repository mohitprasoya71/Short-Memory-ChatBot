from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import AIMessage, BaseMessage,HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, AIMessageChunk

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=GOOGLE_API_KEY,
    max_tokens=2000,  # increased
    temperature=0.7
)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)

    if isinstance(response.content, list):
        text = " ".join(
            block["text"] for block in response.content
            if isinstance(block, dict) and "text" in block
        )
    else:
        text = response.content

    return {"messages": [AIMessage(content=text)]}

checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)

      
        