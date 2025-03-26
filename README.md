# Medical Chatbot - RAG Application

## Overview
This is a Retrieval-Augmented Generation (RAG) chatbot designed to provide medical information and answer user queries using a medical textbook as its primary knowledge base. The application leverages the following technologies:

- **Pinecone** for efficient vector search and indexing
- **OpenAI API** for natural language processing and conversational abilities
- **AWS** (EC2, ECR, S3) for hosting and deployment
- **LangChain** for building and orchestrating the RAG pipeline

## Features
- Accurate medical information retrieval
- Conversational interface powered by OpenAI API
- Scalable architecture using AWS services
- Fast and efficient search and storage via Pinecone

## Architecture
1. **Data Ingestion**: The medical textbook is processed into chunks for vector embedding generation.
2. **Embedding Generation**: Embeddings are created using OpenAI's text embedding models.
3. **Indexing**: Embeddings are stored and indexed in Pinecone for fast retrieval.
4. **Query Handling**: User queries are processed using LangChain, which retrieves relevant content from Pinecone and generates appropriate responses using the OpenAI API.
5. **Deployment**: The application is hosted using AWS EC2, with containerized images stored in ECR and static data in S3.

## Setup Instructions
### Prerequisites
- Python 3.10+
- AWS Account with EC2, ECR, and S3 permissions
- Pinecone Account
- OpenAI API Key

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/natek-1/Medical-Chatbot.git
   cd Medical-Chatbot
   ```
2. Create and activate a virtual environment:
   ```bash
   conda create python=3.10 -y -n medical_chatbot
   conda activate medical_chatbot
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your environment variables to a `.env` file:
   ```env
   OPENAI_API_KEY=<your-openai-api-key>
   PINECONE_API_KEY=<your-pinecone-api-key>
   AWS_ACCESS_KEY_ID=<your-aws-access-key>
   AWS_SECRET_ACCESS_KEY=<your-aws-secret-key>
   ```
5. Make sure to download a medical text book you will need and save it to 'data/medical_book.pdf'
    I personally use The GALE ENCYCLOPEDIA of M EDICINE SECOND EDITION

### Data Preparation
1. Process the medical textbook into text chunks.
2. Generate embeddings using the OpenAI API.
3. Index the embeddings in Pinecone.

### Indexing
make sure the run the following to index (You should onlny need to do it once)
```bash
python store_index.py
```

### Running the Application
1. Start the server:
   ```bash
   python app.py
   ```
2. Access the chatbot endpoint at `http://localhost:8080` (or your EC2 instance URL when deployed).

### Deployment
1. Build the Docker image:
   ```bash
   docker build -t medical-chatbot .
   ```
2. Push the image to AWS ECR:
   ```bash
   aws ecr create-repository --repository-name medical-chatbot
   aws ecr get-login-password | docker login --username AWS --password-stdin <aws-account-id>.dkr.ecr.<region>.amazonaws.com
   docker tag medical-chatbot:latest <aws-account-id>.dkr.ecr.<region>.amazonaws.com/medical-chatbot:latest
   docker push <aws-account-id>.dkr.ecr.<region>.amazonaws.com/medical-chatbot:latest
   ```
3. Deploy the container on EC2 and configure the load balancer for scalability.

## Future Improvements
- Implement multi-turn conversation flow
- Add user authentication and authorization
- Improve response accuracy with more advanced fine-tuning
- Integrate monitoring tools for improved performance tracking

## License
This project is licensed under the MIT License.

## Contact
For questions or contributions, please reach out via [GitHub Issues](https://github.com/your-username/medical-chatbot/issues).

