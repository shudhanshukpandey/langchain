
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PROXYCURL_API_KEY = os.environ.get("PROXYCURL_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
LANGCHAIN_TRACING_V2 = os.environ.get("LANGCHAIN_TRACING_V2", False)

EDEN_MARCO_GIST_URL = "https://gist.githubusercontent.com/shudhanshukpandey/f7454183754dfbc8fa56c56e947c86b6/raw/36a2ce86f39853720e7eef1a680d5c05f8aa1ba4/eden_marco"


