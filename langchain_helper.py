
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

import os
from dotenv import load_dotenv
load_dotenv() # take environment variables from .env (especially openai api key)

# Create Google LLM model
llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        google_api_key=os.environ["GOOGLE_API_KEY"],
        temperature=0.1
)

# Initialize instructor embeddings using the Hugging Face model
instructor_embeddings = HuggingFaceInstructEmbeddings(
    model_name="hkunlp/instructor-large",
    query_instruction="Represent the query for retrieval: "
)
vectordb_file_path="faiss_index"

def create_vector_db():
    # Load data from FAQ sheet
    loader = CSVLoader(file_path='codebasics_faqs.csv', encoding="ISO-8859-1", source_column='prompt')
    docs = loader.load()

    # Create a FAISS instance for vector database from 'data'
    vectordb = FAISS.from_documents(documents=docs, embedding=instructor_embeddings)

    # Save vector database locally
    vectordb.save_local("faiss_index")


def get_qa_chain():
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings, allow_dangerous_deserialization=True)

    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold = 0.7)

    prompt_template = """Given the following context and a question, generate an answer based on the following pieces of context only.
    In the answer try to provide as much text as possible from "response" section in the source document context.
    If you can't find the answer in the context, please kindly state "I don't know."

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )


    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        input_key="query",
        return_source_documents=True,
        chain_type_kwargs = {"prompt": PROMPT}
    )

    return chain


if __name__ == "__main__":
    chain = get_qa_chain()
    print(chain.invoke("Do you have javascript course?"))
