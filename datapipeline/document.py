from typing import List

class Document:
    def __init__(self, id: str, dataset: str, title: str, text: str):
        self.id = id
        self.dataset = dataset
        self.title = title
        self.text = text

class Chunk:
    def __init__(self, id: str, doc_id: str, text: str, embedding: List[float] = None):
        self.id = id
        self.doc_id = doc_id
        self.text = text
        self.embedding = embedding
