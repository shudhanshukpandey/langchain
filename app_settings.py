
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PROXYCURL_API_KEY = os.environ.get("PROXYCURL_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
LANGCHAIN_TRACING_V2 = os.environ.get("LANGCHAIN_TRACING_V2", False)
