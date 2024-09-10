# AI-Powered CSE Subject Bot

This project is an AI-driven chatbot trained on theoretical Computer Science subjects like DBMS, CN, OS, Blockchain and OOP. The bot answers questions based on content fed through pre-embedded PDFs using ChromaDB. The project offers both a command-line interface (CLI) and a user interface (UI) built using Streamlit.

## Features
- **Pre-fed PDFs**: The chatbot has been pre-trained with PDFs covering theoretical Computer Science subjects.
- **LangChain Integration**: Uses LangChain to generate relevant prompts and responses.
- **Gemini AI**: Powered by Google Gemini AI for generating intelligent answers.
- **ChromaDB**: Stores and retrieves document embeddings to provide accurate responses.
- **Two Interfaces**:
  - **Streamlit UI**: A user-friendly interface (`app.py`) where users can ask questions.
  - **CLI**: A terminal-based interface (`rag.py`) for command-line interactions.

## Tech Stack

| Technology  | Purpose  |
|-------------|----------|
| ![Python](https://www.vectorlogo.zone/logos/python/python-icon.svg) Python | Core programming language |
| ![LangChain](https://api.nuget.org/v3-flatcontainer/langchain/0.15.0/icon) LangChain  | Question-answer framework |
| ![Gemini AI](https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Google_G_icon.svg/512px-Google_G_icon.svg.png) Gemini AI  | AI-driven responses |
| ![ChromaDB](https://chromadb.org/static/chromadb-mark-blue-500px.png) ChromaDB | Vector store for embedding storage |
| ![Streamlit](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg) Streamlit | User interface for the application |

## Running the Project

### Streamlit UI Version
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/project-name.git
   cd project-name
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### CLI Version
1. After cloning the repository and installing dependencies (as shown above), run:
   ```bash
   python rag.py
   ```

## How It Works
- **PDF Embedding**: The pre-embedded PDFs (stored in `generate_embeddings.py`) are processed and stored in ChromaDB. This allows the bot to answer questions related to the content from those PDFs.
- **Streamlit UI**: Users can interact with the bot using the UI, asking questions that will be answered using the AI-powered bot.
- **CLI Version**: Similar functionality but using a terminal interface.
