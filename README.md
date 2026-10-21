# 📚 Book Recommender

A book recommendation project built with Python, Pandas, LangChain, Hugging Face sentence embeddings, and ChromaDB. The project uses semantic search to recommend books based on the meaning of a user's query rather than relying exclusively on keyword matching.

This project is part of my journey into data analytics, machine learning, and natural language processing.

## 🎯 Project Goals

The primary goal is to build a book recommendation system that understands natural-language queries and retrieves relevant books from a dataset of book descriptions.

The project explores:

- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Semantic search and vector embeddings
- Vector databases and similarity search
- Recommendation ranking
- Filtering recommendations using book metadata
- Natural-language processing (NLP)

## 📊 Dataset

**Dataset:** [7k Books with Metadata](https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata)

The dataset contains book metadata, including titles, authors, categories, descriptions, publication years, ratings, page counts, and ISBN identifiers.

After preprocessing, the project contains **5,197 books with usable descriptions**.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and preprocessing |
| Jupyter Notebook | Interactive development and experimentation |
| LangChain | Document processing and embedding integration |
| Hugging Face | Local sentence embedding model |
| Sentence Transformers | Generating semantic embeddings |
| ChromaDB | Vector storage and similarity search |
| Git and GitHub | Version control and project documentation |

### Embedding Model

The project uses the pretrained model:

`sentence-transformers/all-MiniLM-L6-v2`

The model generates vector embeddings locally, avoiding the need for a paid OpenAI API for the current semantic-search implementation.

## ✅ Completed Work

### 1. Data Exploration and Cleaning

- Inspected the dataset's columns and data types.
- Explored book ratings and other numerical variables.
- Examined missing values.
- Investigated relationships between numerical variables using Spearman correlation.
- Filtered out books with descriptions containing 25 words or fewer.
- Created a `title_and_subtitle` field that uses the title alone when a subtitle is unavailable.
- Created a `tagged_description` field combining each book's ISBN-13 identifier and description.
- Exported the cleaned dataset to `books_cleaned.csv`.
- Exported the tagged descriptions to `tagged_description.txt`.

### 2. Local Embeddings

Integrated a pretrained Sentence Transformers model through LangChain's Hugging Face embedding integration.

The embedding model converts book descriptions into numerical vectors that represent semantic meaning, enabling retrieval based on conceptual relevance rather than exact keyword matches.

### 3. ChromaDB Vector Database

- Created LangChain documents from the tagged descriptions.
- Built a ChromaDB vector database using the local embedding model.
- Indexed all **5,197 cleaned book documents**.
- Tested similarity searches using natural-language queries.
- Confirmed that the database returns relevant book descriptions.

### 4. Semantic Book Search

Implemented semantic search using ChromaDB's similarity-search functionality.

Example query:

```python
# Example query — replace this string with your own search.
query = "A story about friendship, magic, and adventure"

# Example search — requires db_books to be initialized.
# results = db_books.similarity_search(query, k=5)
```

The system retrieves book descriptions that are semantically relevant to the query.

### 5. Book Recommendation Function

Developed a `recommend_books()` function that connects semantic-search results to the original Pandas metadata.

The function:

- Accepts a natural-language query.
- Retrieves relevant books from ChromaDB.
- Extracts ISBN-13 identifiers from search results.
- Matches identifiers against the cleaned dataset.
- Preserves ChromaDB's relevance ranking.
- Returns selected metadata in a Pandas DataFrame.

The returned information includes:

- ISBN-13
- Title
- Authors
- Categories
- Description
- Thumbnail
- Average rating

Example usage:

```python
# Example call — requires the recommend_books() function to be defined.
# recommendations = recommend_books(
#     query="A fantasy story about magic and friendship",
#     k=5
# )
```

### 6. Minimum-Rating Filter

Extended the recommendation function with an optional `min_rating` parameter.

Example usage:

```python
# Example: Recommend up to five books rated 4.0 or higher.
# recommendations = recommend_books(
#     query="A fantasy story about magic and friendship",
#     k=5,
#     min_rating=4.0
# )
```

A stricter rating requirement can also be used:

```python
# Example: Recommend books rated 4.5 or higher.
# recommendations = recommend_books(
#     query="A fantasy story about magic and friendship",
#     k=5,
#     min_rating=4.5
# )
```

The rating filter is optional. When `min_rating=None`, the function does not filter recommendations by rating.

The function retrieves up to five times the requested number of candidates to improve the chances of finding enough books that satisfy the rating requirement. Consequently, it may return fewer than the requested number of books when too few candidates qualify.

## ⚙️ Current Recommendation Workflow

The current system follows this workflow:

1. The user enters a natural-language query.
2. The embedding model represents the query for semantic search.
3. ChromaDB retrieves books with semantically similar descriptions.
4. ISBN-13 identifiers connect search results to the cleaned Pandas dataset.
5. The recommendation function retrieves the relevant metadata.
6. An optional minimum-rating filter removes books below the requested threshold.
7. The function returns recommendations in semantic relevance order.

## 📁 Project Files

| File | Description |
|---|---|
| `data-exploration.ipynb` | Notebook containing data exploration, preprocessing, embeddings, vector search, and recommendation experiments |
| `books_cleaned.csv` | Cleaned book metadata |
| `tagged_description.txt` | ISBN-tagged book descriptions used to create the vector database |
| `README.md` | Project documentation |
| `.gitignore` | Specifies files and directories Git should ignore |

The vector database is generated during development and may need to be rebuilt if its persisted files are not included in the repository.

## 🚀 Setup and Installation

### Prerequisites

- Python
- Jupyter Notebook
- Git

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd book-recommender
```

Replace `<your-repository-url>` with the URL of your GitHub repository.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install pandas jupyter langchain-community langchain-core langchain-huggingface langchain-chroma sentence-transformers
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open `data-exploration.ipynb` and execute the notebook cells in order.

**Note:** The first embedding-model initialization may require an internet connection to download the pretrained model. Subsequent runs can use the locally cached model.

The notebook and generated data files must be available at the paths expected by the code.

## 🔄 Current Project Status

**Status: Working semantic-search and metadata-based recommendation prototype.**

| Component | Status |
|---|---|
| Dataset exploration | Completed |
| Data cleaning and preprocessing | Completed |
| Cleaned CSV and tagged-description exports | Completed |
| Local embedding model integration | Completed |
| ChromaDB indexing | Completed |
| Semantic similarity search | Working |
| ISBN-based metadata retrieval | Working |
| Recommendation function | Working |
| Optional minimum-rating filter | Implemented and tested |
| Category filtering | Planned |
| Publication-year filtering | Planned |
| Page-count filtering | Planned |
| Combined recommendation filters | Planned |
| User interface | Planned |
| End-to-end application | In development |

## 🗺️ Roadmap

### Phase 1: Data Preparation

- [x] Explore the dataset.
- [x] Clean book metadata and descriptions.
- [x] Generate tagged descriptions.
- [x] Export the cleaned dataset.

### Phase 2: Semantic Search

- [x] Integrate a local sentence embedding model.
- [x] Convert book descriptions into LangChain documents.
- [x] Build the ChromaDB vector database.
- [x] Test semantic similarity search.

### Phase 3: Recommendation Logic

- [x] Connect search results to book metadata using ISBN-13.
- [x] Implement the `recommend_books()` function.
- [x] Preserve semantic relevance ranking.
- [x] Add an optional minimum-rating filter.
- [ ] Add category filtering.
- [ ] Add publication-year filtering.
- [ ] Add page-count filtering.
- [ ] Support combinations of filters.
- [ ] Improve recommendation quality and evaluation.

### Phase 4: User Experience

- [ ] Design a user-friendly interface.
- [ ] Display book covers and relevant metadata.
- [ ] Allow users to search using natural language.
- [ ] Add controls for recommendation filters.
- [ ] Integrate the recommendation function into the interface.

### Phase 5: Evaluation and Improvements

- [ ] Test the system using different types of queries.
- [ ] Evaluate recommendation relevance.
- [ ] Improve handling of empty or insufficient results.
- [ ] Optimize retrieval and response time.
- [ ] Document limitations and future improvements.

## 📚 Learning Objectives

This project provides practical experience with:

- Data cleaning and exploratory data analysis
- Pandas DataFrame operations
- Natural-language processing
- Sentence embeddings
- Vector databases
- Semantic similarity search
- LangChain document processing
- Metadata-based recommendation filtering
- Building an end-to-end machine learning application

## 🔮 Future Possibilities

Potential future improvements include:

- More advanced recommendation strategies
- Improved ranking using multiple metadata signals
- Better book discovery through combined semantic and metadata filters
- Recommendation explanations
- A web-based interface
- Evaluation using recommendation metrics

These are future possibilities rather than currently implemented features.

## 👨‍💻 Project Status and Development

This is an actively developed learning and portfolio project. Its current focus is building a functional semantic book recommendation system using local embeddings and a vector database.