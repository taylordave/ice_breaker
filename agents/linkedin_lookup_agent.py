import os
from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain import hub


load_dotenv()


def lookup(name: str) -> str:
    return "https://www.linkedin.com/in/eden-marco/"
