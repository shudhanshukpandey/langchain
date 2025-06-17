import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# from agent_tools.tools import get_profile_url_tavily


import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PROXYCURL_API_KEY = os.environ.get("PROXYCURL_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
LANGCHAIN_TRACING_V2 = os.environ.get("LANGCHAIN_TRACING_V2", False)


from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name):
    """Search for linkedIn profile URL"""

    search = TavilySearchResults()
    res = search.run(f'{name}')

    return res







def lookup(name:str)->str:

    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini",
    )

    template = """fiven the full name {name_of_person} I want you to get it me a link to their LinkedIn profile page.
                your answer should only contain the url."""
    
    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])

    tools_for_agent = [
        Tool(
            name="crawl google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the linkedinpage url"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)


    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent,verbose=True)

    result = agent_executor.invoke(input={"input":prompt_template.format_prompt(name_of_person=name)})

    linkedin_profile_url = result["output"]

    return linkedin_profile_url


    

    # return "https://www.linkedin.com/in/anshul131/"

# data = lookup("ansul mishra")

# print(data)