from document import Document, Chunk
from typing import List
import re

class Chunker:
    def chunk(self, document: Document) -> List[Chunk]:
        raise NotImplementedError


# Remove non-ASCII characters, additionally dynamically chunks documents based off of text size
class AdaptiveChunker(Chunker):
    def __init__(self, max_chunks: int = 5):
        self.max_chunks = max_chunks

    def clean_text(self, text: str) -> str:
        return re.sub(r'[^\x00-\x7F]+', ' ', text)

    def chunk(self, document: Document) -> List[Chunk]:
        cleaned_text = self.clean_text(document.text)
        chunks = []
        chunk_size = max(len(cleaned_text) // self.max_chunks, 1)  # Ensure chunk_size is at least 1
        for i in range(0, len(cleaned_text), chunk_size):
            chunk_text = cleaned_text[i:i+chunk_size]
            chunk_id = f"{i // chunk_size + 1}"  # Sequential number for chunk ID
            chunks.append(Chunk(id=chunk_id, doc_id=document.id, text=chunk_text))
        return chunks
