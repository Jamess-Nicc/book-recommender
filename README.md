# 📚 Book Recommender

A book recommendation project built with Python, Pandas, sentence embeddings, and ChromaDB. The project uses book descriptions to retrieve semantically relevant books from natural-language queries.

**Project Status:** Data preparation and a local semantic-search prototype are working. The recommendation function and user interface are still in development.

## 🚀 Current Features

- Explored a book metadata dataset containing approximately 7,000 books.
- Cleaned and prepared book metadata using Pandas.
- Filtered out books with descriptions containing 25 words or fewer.
- Created a `title_and_subtitle` column, using the title alone when a subtitle is unavailable.
- Created a `tagged_description` column combining each book's ISBN-13 and description, separated by a space.
- Exported cleaned book data to `books_cleaned.csv`.
- Exported ISBN-tagged descriptions to `tagged_description.txt`.
- Loaded text data using LangChain's `TextLoader`.
- Converted individual book descriptions into LangChain `Document` objects.
- Generated text embeddings locally using `sentence-transformers/all-MiniLM-L6-v2`.
- Built a ChromaDB vector database for semantic search.
- Tested semantic search using natural-language queries and retrieved the top five matching documents.

## 🛠️ Technology Stack

- **Python** — Core programming language
- **Pandas** — Data cleaning and manipulation
- **Jupyter Notebook** — Data exploration and experimentation
- **LangChain** — Document loading and embedding integration
- **Sentence Transformers** — Local text embedding model
- **ChromaDB** — Vector storage and semantic similarity search

## ⚙️ How It Works

The current project follows this workflow:

1. **Data Exploration:** Explore the book metadata dataset using Pandas.
2. **Data Cleaning:** Clean the dataset and filter out books with insufficient descriptions.
3. **Text Preparation:** Combine each book's ISBN-13 with its description.
4. **Data Export:** Save the cleaned metadata and tagged descriptions to separate files.
5. **Document Loading:** Load the tagged descriptions and create individual documents for each book.
6. **Embedding Generation:** Convert book descriptions into numerical representations using a local embedding model.
7. **Vector Database:** Store the documents and embeddings in ChromaDB.
8. **Semantic Search:** Retrieve books whose descriptions are semantically similar to a user's natural-language query.

### Example Query

```python
query = "A story about friendship, magic, and adventure"

results = "db_books.similarity_search(query, k=5)"
```

This query retrieves up to five book descriptions related to the requested themes.

Unlike a simple keyword search, semantic search can identify relevant descriptions even when they use different words to express similar ideas.

## 🧠 Local Embeddings

This project uses the following model:

`sentence-transformers/all-MiniLM-L6-v2`

The model is integrated through LangChain's `HuggingFaceEmbeddings` and generates embeddings locally.

This approach avoids paid OpenAI API calls for the current embedding and semantic-retrieval workflow.

The initial model download requires an internet connection. Once downloaded, the model can generate embeddings locally without requiring an OpenAI API key.

## 📂 Project Files

| File | Description |
|---|---|
| `books_cleaned.csv` | Cleaned book metadata for retrieving book information |
| `tagged_description.txt` | Book descriptions prefixed with ISBN-13 identifiers, used for semantic search |
| `data-exploration.ipynb` | Notebook for exploring and preparing the dataset, if present |
| Semantic-search notebook | Notebook for loading documents, generating embeddings, building ChromaDB, and testing retrieval |

File names and notebook organization may change as the project develops.

## 📦 Installation

Install the required Python packages in your project environment:

```bash
python -m pip install pandas jupyter langchain-community langchain-core langchain-huggingface langchain-chroma sentence-transformers
```

If you're using PyCharm, make sure your notebook kernel uses the same Python interpreter or virtual environment where the packages are installed.

## ⚠️ Current Limitations

- The system retrieves relevant book descriptions but does not yet present fully developed book recommendations.
- Retrieved ISBNs have not yet been integrated into a complete recommendation function.
- Recommendation ranking and presentation logic are still in development.
- A user-facing interface has not yet been implemented.
- The current ChromaDB setup uses an in-memory collection unless persistence is configured separately.
- Recommendation relevance and overall system performance still require further testing.

## 🗺️ Roadmap

- [x] Explore and clean the book metadata dataset.
- [x] Prepare ISBN-tagged book descriptions.
- [x] Generate local text embeddings.
- [x] Build a ChromaDB vector database.
- [x] Test semantic search with natural-language queries.
- [ ] Rebuild and verify the corrected document collection.
- [ ] Connect retrieved ISBNs to the corresponding book metadata.
- [ ] Implement a reusable book recommendation function.
- [ ] Improve recommendation ranking and filtering.
- [ ] Continue implementing the recommendation pipeline.
- [ ] Build a user-friendly interface.
- [ ] Test and evaluate recommendation quality.

## 🎯 Learning Objectives

This project is a practical learning experience focused on:

- Python programming
- Data cleaning and manipulation with Pandas
- Natural-language processing
- Text embeddings and semantic similarity
- Vector databases and information retrieval
- Building applications with LangChain
- Integrating machine-learning components into a usable application

## 📖 Dataset

The project uses the **7k Books with Metadata** dataset from Kaggle.

Dataset: [7k Books with Metadata — Kaggle](https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata)

## 📌 Project Status

The project has progressed from data exploration and preparation to a working semantic-search prototype using local embeddings and ChromaDB.

The next milestone is to connect search results to complete book metadata and implement the core recommendation function.

The long-term goal is to build a book recommendation application that accepts natural-language preferences and returns relevant books from the dataset.