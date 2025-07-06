import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
#from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain_community.llms import HuggingFaceHub
from typing import List, Optional
import os


class PDFChatApp:
    
    def __init__(self, 
                 embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
                 llm_repo_id: str = "google/flan-t5-xxl",
                 chunk_size: int = 1000,
                 chunk_overlap: int = 200,
                 temperature: float = 0.7,
                 max_length: int = 512):
        self.embedding_model = embedding_model
        self.llm_repo_id = llm_repo_id
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.temperature = temperature
        self.max_length = max_length
        
        # Initialize components
        self.embeddings = None
        self.vectorstore = None
        self.conversation_chain = None
        self.chat_history = None
        
        # Load environment variables
        load_dotenv()
        
        # Initialize Streamlit session state
        self._initialize_session_state()
    
    def _initialize_session_state(self):
        if "conversation" not in st.session_state:
            st.session_state.conversation = None
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = None
    
    def extract_pdf_text(self, pdf_docs: List) -> str:
        text = ""
        for pdf in pdf_docs:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    
    def create_text_chunks(self, text: str) -> List[str]:
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        return chunks
    
    def create_vectorstore(self, text_chunks: List[str]) -> FAISS:
        self.embeddings = HuggingFaceEmbeddings(model_name=self.embedding_model)
        self.vectorstore = FAISS.from_texts(texts=text_chunks, embedding=self.embeddings)
        return self.vectorstore
    
    def create_conversation_chain(self, vectorstore: FAISS) -> ConversationalRetrievalChain:
        llm = HuggingFaceHub(
            repo_id=self.llm_repo_id, 
            model_kwargs={
                "temperature": self.temperature, 
                "max_length": self.max_length
            }
        )
        
        memory = ConversationBufferMemory(
            memory_key='chat_history', 
            return_messages=True
        )
        
        self.conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            memory=memory
        )
        return self.conversation_chain
    
    def process_pdfs(self, pdf_docs: List) -> bool:
        try:
            with st.spinner("Processing PDFs..."):
                # Extract text from PDFs
                raw_text = self.extract_pdf_text(pdf_docs)
                if not raw_text.strip():
                    st.error("No text could be extracted from the uploaded PDFs.")
                    return False
                
                st.success("PDF text extraction completed!")
                
                # Create text chunks
                text_chunks = self.create_text_chunks(raw_text)
                #st.success(f"Created {len(text_chunks)} text chunks!")
                
                # Create vector store
                vectorstore = self.create_vectorstore(text_chunks)
                #st.success("Vector store created successfully!")
                
                # Create conversation chain
                self.conversation_chain = self.create_conversation_chain(vectorstore)
                st.session_state.conversation = self.conversation_chain
                st.success("Conversation chain ready! You can now ask questions.")
                
                return True
                
        except Exception as e:
            st.error(f"Error processing PDFs: {str(e)}")
            return False
    
    def handle_user_input(self, user_question: str) -> None:
        if st.session_state.conversation is None:
            st.error("Please upload and process your PDF documents first before asking questions.")
            return
        
        try:
            response = st.session_state.conversation({'question': user_question})
            st.session_state.chat_history = response['chat_history']
            
            # Display chat history
            for i, message in enumerate(st.session_state.chat_history):
                if i % 2 == 0:
                    st.write(user_template.replace(
                        "{{MSG}}", message.content), unsafe_allow_html=True)
                else:
                    st.write(bot_template.replace(
                        "{{MSG}}", message.content), unsafe_allow_html=True)
                        
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
    
    def setup_ui(self) -> None:
        st.set_page_config(
            page_title="Chat with PDFs",
            page_icon=":books:"
        )
        st.write(css, unsafe_allow_html=True)
        st.header("Chat with PDFs :books:")
    
    def render_sidebar(self) -> List:
        with st.sidebar:
            st.subheader("Your documents")
            pdf_docs = st.file_uploader(
                "Upload your PDFs here and click on 'Process'", 
                accept_multiple_files=True,
                type=['pdf']
            )
            
            if st.button("Process PDFs"):
                if pdf_docs:
                    self.process_pdfs(pdf_docs)
                else:
                    st.warning("Please upload at least one PDF file.")
            
            # Display processing status
            if st.session_state.conversation is not None:
                st.success("✅ PDFs processed and ready for questions!")
            
        return pdf_docs
    
    def render_chat_interface(self) -> None:
        user_question = st.text_input("Ask a question about your documents")
        if user_question:
            self.handle_user_input(user_question)
    
    def run(self) -> None:
        # Setup UI
        self.setup_ui()
        
        # Initialize session state
        self._initialize_session_state()
        
        # Render sidebar
        self.render_sidebar()
        
        # Render chat interface
        self.render_chat_interface()


def main():
    app = PDFChatApp()
    app.run()


if __name__ == '__main__':
    main()
