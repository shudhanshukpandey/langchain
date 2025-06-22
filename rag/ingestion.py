from app_settings import *

from langchain_community.document_loaders.text import TextLoader
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

from langchain_pinecone import PineconeVectorStore






if __name__=="__main__":
    print("Rag ingestion")
    file_path = r"/Users/shudhanshu/Desktop/GitHub_Projects/langchain/rag/mediumblog1.txt"
    loader = TextLoader(file_path)
    document = loader.load()

    print("loading....")

    # print("document :\n",document)

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    # chunkoverlap will take 'n' chars from last chunk and overlap with current chunk with n chars, 0 means no overlap

    text = text_splitter.split_documents(document)

    print(f"created {len(text)} chunks")
    # print(text)

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    print("ingesting...")

    PineconeVectorStore.from_documents(text,embeddings,index_name=INDEX_NAME)

    print("finish...")

