from app_settings import *
from prompts.react_prompt import *

from langchain.agents import tool
from langchain.tools import Tool
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.tools.render import render_text_description
from langchain.agents.output_parsers.react_single_input import ReActSingleInputOutputParser

from typing import Union, List
from langchain_core.agents import AgentAction, AgentFinish

# from langchain.schema import AgentAction,AgentFinish





@tool
def get_len_text(text:str)->int:
    """Returns length of text by character"""
    print(f"get_len_text enter with {text}")
    text = text.strip("'\n").strip('"')
    return len(text)



def find_tool_by_name(tools:List[Tool],tool_name:str)->Tool:
    for tool in tools:
        if tool.name == tool_name:
            return tool
    raise ValueError(f"tool with too_name {tool_name} not found")


if __name__=="__main__":
    print("ReAct Deepdive")
    
    # print(get_len_text("casper"))
    # print(get_len_text.invoke(input={"text":"casper"}))

    tools = [get_len_text]

    # prompt = PromptTemplate(template=react_template).partial(tools=tools, tool_names = ", ".join([t.name for t in tools]))

    prompt = PromptTemplate(template=react_template).partial(tools=render_text_description(tools), tool_names = ", ".join([t.name for t in tools]))
    
    llm = ChatOpenAI(temperature=0, stop="\nObservation",model="gpt-4o-mini") 
    agent = {"input":lambda x:x ["input"]} | prompt | llm | ReActSingleInputOutputParser()

    # input will take input dynamically, will pass it in prompt, 
    # and in end final prompt will be in llm

    # result = agent.invoke({"input":"what is the lenght of 'casper' in characters"})

    agent_step:Union[AgentAction,AgentFinish] = agent.invoke({"input":"what is the lenght of 'casper' in characters"})
    print("agent_step taken: ", agent_step)

    if isinstance(agent_step, AgentAction):
        tool_name = agent_step.tool
        tool_to_use = find_tool_by_name(tools, tool_name)
        tool_input = agent_step.tool_input

        observaation = tool_to_use.func(str(tool_input))

        print(observaation)
# 9500870704