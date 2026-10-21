from pathlib import Path

import pandas as pd
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# Locate the project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Paths to the existing project files
BOOKS_CSV_PATH = PROJECT_ROOT / "books_cleaned.csv"
CHROMA_DB_PATH = PROJECT_ROOT / "chroma.db"


# Load book metadata
books = pd.read_csv(BOOKS_CSV_PATH)

# Initialize the embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Connect to the persistent ChromaDB database
db_books = Chroma(
    persist_directory=str(CHROMA_DB_PATH),
    embedding_function=embedding_model
)


def recommend_books(query, k=5, min_rating=None):
    # Search for more candidates than we need
    candidate_results = db_books.similarity_search(
        query,
        k=max(k * 5, k)
    )

    # Extract ISBNs in relevance order
    isbn_list = [
        doc.page_content.split()[0].strip('"')
        for doc in candidate_results
    ]

    # Prepare the book metadata
    books_lookup = books.copy()
    books_lookup["isbn13"] = books_lookup["isbn13"].astype(str)
    books_lookup = books_lookup.set_index("isbn13")

    # Retrieve books in ChromaDB's search order
    recommended_books = books_lookup.reindex(isbn_list)

    # Remove books that were not found
    recommended_books = recommended_books.dropna(how="all")

    # Apply the minimum rating filter if requested
    if min_rating is not None:
        recommended_books = recommended_books[
            recommended_books["average_rating"] >= min_rating
        ]

    # Limit the number of recommendations
    recommended_books = recommended_books.head(k)

    # Select useful information
    columns_to_display = [
        "title",
        "authors",
        "categories",
        "description",
        "thumbnail",
        "average_rating"
    ]

    recommended_books = recommended_books[columns_to_display]

    return recommended_books.reset_index()