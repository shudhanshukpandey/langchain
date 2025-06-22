from app_settings import *

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from langchain_pinecone import PineconeVectorStore

from langchain import hub

from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain_core.runnables import RunnablePassthrough

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


if __name__=="__main__":
    print("Rag retrival")

    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI()

    query = "what is pinecone in machine learning?"

    chain = PromptTemplate.from_template(template=query) | llm
    result = chain.invoke(input={})

    # print(result) # llm gives the answer from random data
    vectorstore = PineconeVectorStore(
        index_name=INDEX_NAME,embedding= embeddings
    )

    retrival_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    combine_docs_chain = create_stuff_documents_chain(llm, retrival_qa_chat_prompt)
    retrival_chain = create_retrieval_chain(
        retriever=vectorstore.as_retriever(), combine_docs_chain=combine_docs_chain
    )

    result = retrival_chain.invoke(input={"input":query})

    # print(result) # we get data from our give information


    template = """
        use the following piece of context to answer the question at the end.
        If you don't know the answerjust say thatyou don;t know don't try to make up answer.
        Always say 'thank for asking' at the end of answer.

        {context}
        Question:{question}
        helpful answer: 

"""
    custom_rag_prompt = PromptTemplate.from_template(template)

    rag_chain = (
        {"context":vectorstore.as_retriever() | format_docs, "question":RunnablePassthrough()}
        | custom_rag_prompt
        | llm
    )

    result = rag_chain.invoke(query)

    print(result)