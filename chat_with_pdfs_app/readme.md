# 📚 Chat with PDFs - AI-Powered Document Q&A

A modern, interactive web application that allows you to chat with your PDF documents using advanced AI technology. Built with Streamlit, LangChain, and HuggingFace models.

## ✨ Features

- **📄 Multi-PDF Support**: Upload and process multiple PDF documents simultaneously
- **🤖 AI-Powered Q&A**: Ask questions about your documents and get intelligent responses
- **💬 Conversational Memory**: The AI remembers your conversation context
- **🎨 Modern UI**: Beautiful, responsive interface with smooth animations
- **⚡ Fast Processing**: Efficient text extraction and vectorization
- **🔒 Privacy-Focused**: Uses local HuggingFace models (no data sent to external APIs)

## 🏗️ Architecture

The application is built using a clean, object-oriented architecture:

### Core Components

- **PDFChatApp Class**: Main application class that orchestrates all functionality
- **Text Processing**: PDF text extraction and chunking for optimal AI processing
- **Vector Database**: FAISS vector store for efficient similarity search
- **AI Models**: HuggingFace embeddings and language models
- **Conversation Chain**: LangChain-powered conversational AI with memory

### Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **AI/ML**: LangChain, HuggingFace Transformers
- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **PDF Processing**: PyPDF2
- **Styling**: Custom CSS with modern design

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ask-multiple-pdfs-main
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (optional)
   ```bash
   # Create a .env file if you want to use HuggingFace models with API access
   echo "HUGGINGFACE_API_TOKEN=your_token_here" > .env
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 📖 How to Use

### 1. Upload PDFs
- Click "Browse files" in the sidebar
- Select one or more PDF documents
- Click "Process PDFs" to extract and analyze the content

### 2. Ask Questions
- Once processing is complete, you'll see a success message
- Type your question in the text input field
- Press Enter or click to get an AI-generated response

### 3. Continue Conversation
- The AI remembers your conversation context
- Ask follow-up questions based on previous responses
- Chat naturally about your documents

## ⚙️ Configuration

The application is highly configurable through the `PDFChatApp` constructor:

```python
app = PDFChatApp(
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",  # Embedding model
    llm_repo_id="google/flan-t5-xxl",                         # Language model
    chunk_size=1000,                                          # Text chunk size
    chunk_overlap=200,                                        # Chunk overlap
    temperature=0.7,                                          # AI creativity (0-1)
    max_length=512                                            # Max response length
)
```

### Available Models

- **Embedding Models**: `sentence-transformers/all-MiniLM-L6-v2` (default)
- **Language Models**: `google/flan-t5-xxl` (default)

### HuggingFace Integration

The application uses HuggingFace models for both text embeddings and language generation:

- **Text Embeddings**: Converts text chunks into numerical vectors for similarity search
- **Language Models**: Generates human-like responses based on retrieved context
- **Model Hosting**: Models are downloaded and cached locally for faster subsequent runs
- **Offline Capability**: Works without internet connection after initial model download

## 🔧 Dependencies

### Core Dependencies
- `streamlit==1.18.1` - Web framework
- `PyPDF2==3.0.1` - PDF text extraction
- `langchain==0.0.184` - AI framework
- `langchain-community` - Community integrations
- `huggingface-hub==0.14.1` - HuggingFace model hosting and API
- `sentence-transformers==2.2.2` - HuggingFace text embeddings
- `faiss-cpu==1.7.4` - Vector similarity search

### AI/ML Dependencies
- `torch>=1.9.0` - PyTorch for deep learning
- `transformers>=4.21.0` - HuggingFace transformers library
- `numpy>=1.21.0` - Numerical computing
- `scikit-learn>=1.0.0` - Machine learning utilities


## 🔍 How It Works

### 1. PDF Processing
```
PDF Upload → Text Extraction → Text Chunking → Vector Embeddings → FAISS Storage
```

### 2. Question Answering
```
User Question → Vector Search → Context Retrieval → AI Generation → Response
```

### 3. Memory Management
- Conversation history is maintained in session state
- Context is preserved across multiple questions
- Memory is cleared when the session ends


---

**Happy Document Chatting! 📚✨**
