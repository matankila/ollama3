from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
import os

def main():

    dir_path = "./vector"
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )
    
    # if embedding does not exists load the pdf and turn it into vector
    if not os.path.isdir(dir_path):
        # Define the text to split
        print("load pdf file...")
        loader = PyPDFLoader("z.pdf")
        pages = loader.load()

        # Split the text into chunks
        print("split pdf into documents")
        splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=100)
        texts = splitter.split_documents(pages)

        # Create the vector store using FAISS
        print("create vectorstore...")
        docsearch = FAISS.from_documents(texts, embeddings)
        docsearch.save_local("vector")
    else:
        # else load the vector
        docsearch = FAISS.load_local("vector", embeddings=embeddings, allow_dangerous_deserialization=True)
    

    template = """
    Answer the question in your own words from the context given to you.
    If questions are asked where there is no relevant context available, please answer from 
    what you know.

    Context: {context}

    Human: {question}
    Assistant:
    """

    prompt = PromptTemplate(
        input_variables=["context",  "question"], 
        template=template
    )

    llm = ChatOllama(
        model="llama3:8b", 
        temperature=0
    )

    # retrive the data using RAG technique, embed query search for similarity in vector and than take context and question together and ask the model
    qa = RetrievalQA.from_chain_type(llm, retriever=docsearch.as_retriever(), chain_type_kwargs={'prompt': prompt})
    result1 = qa({"query": "what is proxy pattern?"})
    print(result1)
    
    

if __name__ == '__main__':
    main()