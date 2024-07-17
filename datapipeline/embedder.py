from document import Chunk
from typing import List
from unidecode import unidecode

class Embedder:
    def embed(self, chunk: Chunk) -> List[float]:
        raise NotImplementedError

class SimpleCharEmbedder(Embedder):
    def embed(self, chunk: Chunk) -> List[float]:
        # Convert each character to its ASCII value
        return [ord(char) for char in chunk.text]
