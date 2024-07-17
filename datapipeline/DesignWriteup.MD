# Data Ingestion Pipeline

This package provides a scalable and modular data ingestion pipeline designed to handle various text datasets with different complexities. The pipeline performs three main steps: loading, chunking, and embedding documents. The design is intended to be easily extendable to new datasets and offers flexibility in processing large volumes of text data.

## Design Writeup

### Key Design Decisions

1. **Modularity**:
   - **Class-based Design**: Each step of the pipeline (loading, chunking, embedding) is encapsulated in its own class. This ensures each component is independently testable, maintainable, and extendable.

2. **Document Representation**:
   - **Document and Chunk Classes**: These classes provide a standard structure for handling data across different datasets, ensuring consistency and ease of manipulation.

3. **Text/Data Cleaning**:
   - **Text Cleaning**: The pipeline includes mechanisms to clean and handle text properly, ensuring non-ASCII characters are managed appropriately to avoid corruption during processing.

### Classes and Interactions

1. **Document and Chunk Classes**:
   - `Document`: Represents a document with an ID, dataset name, title, and text.
   - `Chunk`: Represents a chunk of a document with an ID, document ID, text, and embedding.

2. **Loader Classes**:
   - **Base Loader (`Loader`)**: An abstract class that defines the `load` method.
   - **FinancialNewsLoader and FootballNewsLoader**: Implementations of the `Loader` class for specific datasets, converting raw data into `Document` objects.

3. **Chunker Class**:
   - **AdaptiveChunker**: Chunks documents into smaller components, ensuring text is cleaned and split appropriately.

4. **Embedder Class**:
   - **SimpleCharEmbedder**: Converts cleaned text chunks into ASCII value embeddings.

5. **IngestionPipeline Class (in main.py)**:
   - Combines all three stages: loading, chunking, and embedding.

### Adding More Datasets

To add a new dataset:
1. **Create a New Loader Class**: Implement a new loader class that extends the `Loader` base class and overrides the `load` method to handle the specific dataset format.
2. **Update the IngestionPipeline**: Add logic to initialize the new loader in the `IngestionPipeline` class.

### Application Logic

To use this code in application logic:
1. **Initialize the Pipeline**: Create an instance of the `IngestionPipeline` class with the dataset name and data path.
2. **Run the Pipeline**: Call the `run` method to process the data.

### Testing the Code

- **Unit Testing**: Write unit tests for each class to ensure they perform their intended functionality.
- **Integration Testing**: Test the entire pipeline with mock datasets to ensure it can handle the complete process from loading to embedding.