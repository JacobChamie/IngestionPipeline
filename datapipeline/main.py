import logging
from loader import FinancialNewsLoader, FootballNewsLoader
from chunker import AdaptiveChunker
from embedder import SimpleCharEmbedder

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IngestionPipeline:
    def __init__(self, dataset_name: str, data_path: str):
        if dataset_name == "financial_news":
            self.loader = FinancialNewsLoader(data_path)
        elif dataset_name == "football_news":
            self.loader = FootballNewsLoader(data_path)
        else:
            raise ValueError(f"Unsupported dataset: {dataset_name}")

        self.chunker = AdaptiveChunker(max_chunks=5)
        self.embedder = SimpleCharEmbedder()

    def run(self):
        documents = self.loader.load()
        logging.info(f"Loaded {len(documents)} documents from dataset.")
        
        all_chunks = []
        for document in documents:
            chunks = self.chunker.chunk(document)
            logging.info(f"Chunked document {document.id} into {len(chunks)} chunks.")
            
            for chunk in chunks:
                chunk.embedding = self.embedder.embed(chunk)
                logging.debug(f"Chunk {chunk.id} embedded with character embeddings: {chunk.embedding[:10]}...")  # Show first 10 embeddings for brevity
            
            all_chunks.extend(chunks)

        return all_chunks
    
if __name__ == "__main__":
    football_news_data_path = "FootballNewsArticles/allfootball.csv" # All of the football news articles .csv
    financial_news_data_path = "FinNewsArticles/2018_01_112b52537b67659ad3609a234388c50a"  # Currently on the first folder within the FinNewsArticles
	
	# Process Financial News Articles
    pipeline = IngestionPipeline("financial_news", financial_news_data_path)
    financial_chunks = pipeline.run()
    logging.info(f"Processed {len(financial_chunks)} chunks from financial news articles.")
    
    # Process Football News Articles
    pipeline = IngestionPipeline("football_news", football_news_data_path)
    football_chunks = pipeline.run()
    logging.info(f"Processed {len(football_chunks)} chunks from football news articles.")
    
    # Print out a few example chunks from both datasets
    print("Financial News Chunks:")
    for i, chunk in enumerate(financial_chunks[:5]):
        print(f"Chunk {i + 1}:")
        print(f"ID: {chunk.id}")
        print(f"Document ID: {chunk.doc_id}")
        print(f"Text: {chunk.text[:100]}...")  # Print the first 100 characters of the chunk text
        print(f"Embedding (first 10 ASCII values): {chunk.embedding[:10]}...")  # Print the first 10 ASCII values of the embedding
        print()

    print("Football News Chunks:")
    for i, chunk in enumerate(football_chunks[:5]):
        print(f"Chunk {i + 1}:")
        print(f"ID: {chunk.id}")
        print(f"Document ID: {chunk.doc_id}")
        print(f"Text: {chunk.text[:100]}...")  # Print the first 100 characters of the chunk text
        print(f"Embedding (first 10 ASCII values): {chunk.embedding[:10]}...")  # Print the first 10 ASCII values of the embedding
        print()