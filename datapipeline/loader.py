import json
import os
import pandas as pd
from document import Document
from typing import List
import logging

class Loader:
    def load(self) -> List[Document]:
        raise NotImplementedError

class FinancialNewsLoader(Loader):
    def __init__(self, data_path: str):
        self.data_path = data_path

    def load(self) -> List[Document]:
        documents = []
        for root, dirs, files in os.walk(self.data_path):
            logging.info(f"Processing directory: {root}")
            for file_name in files:
                if file_name.endswith(".json"):
                    file_path = os.path.join(root, file_name)
                    logging.info(f"Processing file: {file_path}")
                    with open(file_path, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        doc_id = data["url"]  # Use URL as document ID
                        title = data.get("title", "No Title")
                        text = data.get("text", "")
                        documents.append(Document(id=doc_id, dataset="financial_news", title=title, text=text))
        logging.info(f"Loaded {len(documents)} documents.")
        return documents

class FootballNewsLoader(Loader):
    def __init__(self, data_path: str):
        self.data_path = data_path

    def load(self) -> List[Document]:
        documents = []
        df = pd.read_csv(self.data_path)
        for index, row in df.iterrows():
            doc_id = row["link"]  # Use URL as document ID
            title = row["title"]
            text = row["content"]
            documents.append(Document(id=doc_id, dataset="football_news", title=title, text=text))
        return documents
