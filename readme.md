# Legal Case Retrieval App with Llama 3 and Sentence Transformer

This project is a Streamlit-based web application that leverages the Llama 3 model, hosted locally via Ollama, to retrieve knowledge from a legal cases dataset. The application uses Sentence Transformer embeddings to create a searchable vector store, allowing users to query the dataset in natural language and retrieve relevant legal case information.

## Features

- **Llama 3 Model Integration**: Utilizes the powerful Llama 3 language model hosted locally via Ollama for natural language processing tasks.
- **Sentence Transformer Embeddings**: Employs the `all-MiniLM-L6-v2` model from Sentence Transformers to generate embeddings for legal documents.
- **Vector Store with Chroma**: Legal documents are stored in a Chroma vector store for efficient retrieval.
- **Streamlit Interface**: User-friendly web interface for querying the legal cases dataset and viewing the results.

## Getting Started

### Prerequisites

- Python 3.8+
- Streamlit
- Ollama
- Sentence Transformers
- Chroma

### Installation

1. **Clone the repository**:
   - ```bash
     git clone https://github.com/your-username/legal-case-retrieval-app.git
     cd legal-case-retrieval-app
     ```

2. **Install dependencies**:
   - ```bash
     pip install -r requirements.txt
     ```

3. **Set up Ollama**:
   - Install Ollama:
     - ```bash
       curl -fsSL https://ollama.com/install.sh | sh
       ```
   - Start the Ollama server:
     - ```bash
       ollama serve
       ```
   - Pull the Llama 3 model:
     - ```bash
       ollama pull llama3
       ```

4. **Prepare the Dataset**:
   - Place your legal case documents in the specified directory (`<path to Object_casedocs>`).

### Running the Application

1. **Run the Jupyter Notebook**:
   - Open and run `starting.ipynb` to set up the environment and test the connection to the Llama 3 model.

2. **Deploy the Streamlit App**:
   - Run the Streamlit app with the following command:
     - ```bash
       streamlit run app.py
       ```
   - Expose the local server using `localtunnel`:
     - ```bash
       npx localtunnel --port 8501
       ```

3. **Access the Application**:
   - The app will be available at the URL provided by `localtunnel`.

### Usage

- Enter your question in the text input field and submit it to retrieve relevant legal case information.
- The results will be displayed on the Streamlit interface.

## Project Structure

- **`starting.ipynb`**: Jupyter Notebook for setting up and testing the environment.
- **`app.py`**: Main application script for the Streamlit interface.
- **`requirements.txt`**: List of Python dependencies.
- **`README.md`**: Project documentation (this file).
- **`Object_casedocs`**: Dataset for this app (https://www.kaggle.com/datasets/ananyapam7/legalai)

## Acknowledgments

- [Ollama](https://ollama.com) for hosting Llama 3.
- [Streamlit](https://streamlit.io) for providing an easy-to-use interface for web apps.
- [Sentence Transformers](https://www.sbert.net) for their efficient embedding models.
