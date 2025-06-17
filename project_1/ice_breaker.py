from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


from app_settings import *
from prompts.section2_prompts import *
from third_party.linkedin import scraoe_linkedin
from agents.linkedin_lookup_agent import lookup
# from project_1.output_parser import summary_parser





from typing import List, Dict, Any

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field



class Summary (BaseModel):
    summary: str = Field (description="summary")
    facts: List[str] = Field (description="interesting facts about them")
    
    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts}

summary_parser = PydanticOutputParser (pydantic_object=Summary)


def ice_break_with(name:str)->str:
    linked_user_name = lookup(name)
    linkedin_data = scraoe_linkedin(linkedin_profile_url=linked_user_name, mock=True)

    summary_template_prompt = PromptTemplate(input_variables=["information"], 
                                             template=summary_template, 
                                             partial_variables={"format_instructions":summary_parser.get_format_instructions()})
    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo") 
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini") 

    chain = summary_template_prompt | llm | summary_parser
    


    linkedin_data = scraoe_linkedin("casper is a ghost", mock=True)
    result = chain.invoke(input={"information":linkedin_data})

    print(result)




if __name__== "__main__":
    print("ice break with world")

    print(ice_break_with("shudhanshu pandey"))
    
  
    
  

