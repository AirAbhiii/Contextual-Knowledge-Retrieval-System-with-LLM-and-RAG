"""
ReAct agent setup for document retrieval and question answering.
"""

import os

from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

from src.config.settings import Config
from src.llms.openai import llm
from src.rag.retriever_setup import get_retriever

config = Config()

# Initialize tools
tools = [get_retriever()]

# Load document description if available
if os.path.exists("description.txt"):
    with open("description.txt", "r", encoding="utf-8") as f:
        description = f.read()
else:
    description = None

# Create ReAct agent prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", config.prompt("system_prompt")),
    ("human", "{input}"),
    ("ai", "{agent_scratchpad}")
])

def get_agent_executor():
    """
    Create a fresh agent executor with the latest tools.
    This ensures that newly uploaded documents are available to the agent.
    """
    current_tools = [get_retriever()]
    
    # Initialize the ReAct agent and executor
    react_agent = create_react_agent(llm, current_tools, prompt)
    
    return AgentExecutor(
        agent=react_agent,
        tools=current_tools,
        handle_parsing_errors=True,
        max_iterations=10,  # Increased from 2 to allow more reasoning steps
        verbose=True,
        return_intermediate_steps=True
    )

