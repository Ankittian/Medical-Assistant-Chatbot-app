# Medical Assistant Chatbot

A Flask-based conversational AI application that provides medical assistance using Retrieval-Augmented Generation (RAG). The chatbot leverages Google's Generative AI models with Pinecone vector database for intelligent medical query responses.

## Features

- 🏥 **Medical Knowledge Base**: Retrieves relevant medical information using similarity search
- 🤖 **AI-Powered Responses**: Uses Google's Gemini 2.5 Flash model for intelligent answers
- 🔍 **Vector Search**: Powered by Pinecone for semantic similarity matching
- 💬 **Web Interface**: Clean and intuitive chat interface built with Flask
- ⚡ **Real-time Processing**: Fast response generation with RAG pipeline

## Tech Stack

- **Backend**: Flask
- **LLM**: Google Generative AI (Gemini 2.5 Flash)
- **Vector Database**: Pinecone
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Framework**: LangChain
- **Frontend**: HTML/CSS

## Prerequisites

Before running this project, ensure you have:

- Python 3.8+
- Pinecone API key
- Google API key


## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Medical-Assistant-Chatbot-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   PINECONE_API_KEY=your_pinecone_api_key
   GOOGLE_API_KEY=your_google_api_key
   ```

## Project Structure

```
Medical-Assistant-Chatbot-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── setup.py              # Package setup configuration
├── store_index.py        # Vector index management
├── .env                  # Environment variables (not versioned)
├── src/
│   ├── helper.py         # Helper functions for embeddings
│   ├── prompt.py         # System prompts and templates
│   └── __init__.py
├── templates/
│   └── chatbot.html      # Web interface
├── static/
│   └── style.css         # Styling
├── Data/                 # Medical data files
├── research/
│   └── trials.ipynb      # Research notebooks for trial
└── README.md
```

## Usage

1. **Run the application**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8080
   ```

3. **Chat with the assistant**
   - Type your medical questions in the chat interface
   - The assistant will retrieve relevant medical information and provide answers

## API Endpoints

### GET `/`
Returns the main chatbot HTML interface.

### POST `/chat`
Processes user messages and returns AI-generated responses.

**Request:**
```json
{
  "message": "Your medical question here"
}
```

**Response:**
```json
{
  "reply": "AI-generated answer"
}
```

## Configuration

The chatbot uses the following key configurations:

- **Model**: `gemini-2.5-flash`
- **Temperature**: 1.0 (for consistent responses)
- **Search Type**: Similarity search
- **Top K Results**: 5 documents

## Development

### Running Tests
```bash
python -m pytest
```

### Building the Package
```bash
python setup.py build
```

### Creating Vector Index
```bash
python store_index.py
```

## Important Notes

⚠️ **API Keys**: Never commit your `.env` file with API keys to version control. Use the provided `.gitignore` to exclude it.

⚠️ **Medical Disclaimer**: This chatbot is an AI assistant and should not be used as a substitute for professional medical advice. Always consult qualified healthcare professionals for medical concerns.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For issues, questions, or suggestions, please open an issue in the repository.

---

**Built with ❤️ using LangChain, Pinecone, and Google Generative AI**
