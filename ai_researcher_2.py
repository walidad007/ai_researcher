# step1: Define state
from pyexpat.errors import messages
import stat
import typing
from urllib import response
from typing_extensions import TypedDict
from typing  import Annotated, Literal
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

from asyncio import tools

import read_pdf

load_dotenv()

class State(TypedDict):
    messages: Annotated[list, add_messages]


# step2: Define ToolNode & Tools
from arxiv_tool importarxiv_search,  =
from read_pdf import =
from write_pdf importrender_latex_pdf,  =
from langgraph.prebuilt import ToolNode

tools = (arxiv_search, read_pdf, render_latex_pdf)
tool_node = ToolNode(tools)

# step3: Setup LLM
import os
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model = "gemini-2.5-pro", api_key=os.getenv("GOOGLE_API_KEY")).bind_tools(tools)
model = model.bind_tools(tools)

 

# step4: Setup Graph 

#from langrapg.prebuilt import ToolNode
from langgraph.graph import END, START, StateGraph

def call_model(state: State):
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}

def should_continue(state: State) -> Literal["tools", END]:
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END


workflow = StateGraph(State)
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)
workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", should_continue)
workflow.add_edge("tools", "agent")

from langgraph.checkpoint.memory import MemorySaver
checkpointer = MemorySaver()
config = ("configurable": {"thread_id": 1})

graph = workflow.compile(checkpointer=checkpointer)  





# step5: Testing 