from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


from app_settings import *
from prompts.section2_prompts import *
from third_party.linkedin import scraoe_linkedin
from agents.linkedin_lookup_agent import lookup

def ice_break_with(name:str)->str:
    linked_user_name = lookup("name")
    linkedin_data = scraoe_linkedin(linkedin_profile_url=linked_user_name)

    summary_template_prompt = PromptTemplate(input_variables=["information"], template=summary_template)
    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo") 
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini") 

    chain = summary_template_prompt | llm


    linkedin_data = scraoe_linkedin("casper is a ghost", mock=True)
    result = chain.invoke(input={"information":linkedin_data})




if __name__== "__main__":
    print("ice break with world")

    ice_break_with("shudhanshu pandey")
    
  
    
  

