# Book Recommender

A full-stack semantic book recommendation application built as a hands-on learning project. It combines data cleaning and exploration with local text embeddings, vector similarity search, a Python API, and a Vue web interface.

The project is inspired by the tutorial **"Build a Semantic Book Recommender with LLMs"** and uses the **7k Books with Metadata** dataset from Kaggle.

## Current Features

- **Data exploration and cleaning** with Pandas in Jupyter Notebook.
- Filters out book descriptions containing 25 words or fewer.
- Creates a `title_and_subtitle` field, falling back to the title when a subtitle is missing.
- Creates ISBN-tagged descriptions to connect semantic-search results to book metadata.
- Uses the local Hugging Face embedding model `sentence-transformers/all-MiniLM-L6-v2`.
- Stores book-description documents and embeddings in ChromaDB for semantic similarity search.
- Provides a reusable recommendation function in `backend/recommender.py`.
- Maps retrieved ISBNs to book metadata, including titles, authors, categories, descriptions, thumbnails, and average ratings.
- Supports recommendation settings such as the number of results and minimum rating.
- Exposes a FastAPI backend with `/api/health` and `/api/recommend` endpoints.
- Includes a Vue 3 + TypeScript frontend built with Vite.
- Displays recommended books through a card-based interface.
- Includes loading and error states in the frontend.
- Uses a Vite development proxy to route `/api` requests to the FastAPI backend.

## Technology Stack

### Data Processing and Recommendation Engine
- Python
- Pandas
- Jupyter Notebook
- LangChain
- Hugging Face Sentence Transformers
- `sentence-transformers/all-MiniLM-L6-v2`
- ChromaDB

### Backend
- FastAPI
- Uvicorn
- Pydantic

### Frontend
- Vue 3
- TypeScript
- Vite
- HTML and CSS

## Dataset

The project uses the **[7k Books with Metadata dataset](https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata)** from Kaggle.

The cleaned dataset currently contains **5,197 books**.

### Data Preparation

The data preparation process includes:

1. Exploring the original dataset using Pandas.
2. Inspecting missing values and summary statistics.
3. Filtering out descriptions containing 25 words or fewer.
4. Creating `title_and_subtitle`, using the title when a subtitle is unavailable.
5. Creating `tagged_description` by combining the ISBN-13 and book description.
6. Exporting the cleaned metadata and tagged descriptions for use by the recommendation pipeline.

### Important Data Files

- `books_cleaned.csv` — cleaned book metadata used to retrieve book details.
- `tagged_description.txt` — ISBN-tagged descriptions used to build the vector database.
- `data-exploration.ipynb` — notebook for data exploration and preparation.
- `chroma.db` or the configured ChromaDB persistence directory — local vector database, depending on the configured storage path.

File locations may vary depending on the current project configuration.

## How Semantic Search Works

The recommendation pipeline follows these steps:

1. The embedding model converts book descriptions into numerical vectors.
2. ChromaDB stores the documents and their embeddings.
3. A user submits a natural-language query, such as `"a story about friendship, magic, and adventure"`.
4. ChromaDB retrieves book descriptions that are semantically similar to the query.
5. The recommendation function extracts ISBNs from the retrieved documents.
6. The ISBNs are used to retrieve the corresponding book metadata while preserving the relevance order returned by ChromaDB.
7. FastAPI returns the recommendations as JSON.
8. Vue displays the recommended books in the user interface.

This implementation uses **semantic retrieval through embeddings and vector similarity**. It does not currently depend on an LLM generating recommendations from scratch.

## Project Structure

The project is organized approximately as follows. Actual filenames and storage locations may differ slightly as development continues.

```text
book-recommender/
├── backend/
│   ├── main.py
│   ├── recommender.py
│   └── test_recommender.py
├── frontend/
│   ├── package.json
│   ├── vite.config.ts
│   └── src/
│       └── App.vue
├── books_cleaned.csv
├── tagged_description.txt
├── data-exploration.ipynb
└── chroma.db
```

The ChromaDB database may instead be stored in a configured persistence directory.

## Installation and Setup

### Requirements

- Python
- Node.js and npm
- A Python virtual environment
- Internet access for installing packages and initially downloading the embedding model

### 1. Clone the Repository

```bash
git clone https://github.com/Jamess-Nicc/book-recommender.git
cd book-recommender
```

If the repository is already on your computer, open a terminal in the existing project directory instead.

### 2. Create a Python Virtual Environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If you already have a working virtual environment, activate that environment instead.

### 3. Install Python Dependencies

```bash
python -m pip install pandas jupyter fastapi "uvicorn[standard]" langchain-community langchain-core langchain-huggingface langchain-chroma sentence-transformers
```

If the project has a maintained `requirements.txt`, use that file to install the project's dependencies instead.

### 4. Install Frontend Dependencies

```powershell
cd frontend
npm install
```

Return to the project root before starting the backend:

```powershell
cd ..
```

## Running the Application

The frontend and backend must run in separate terminal windows during local development.

### Terminal 1: Start the Backend

From the project root, with the Python virtual environment activated:

```powershell
python -m uvicorn main:app --app-dir backend --reload --port 8001
```

The backend runs locally on port `8001`.

Available development endpoints:

- Health check: `http://127.0.0.1:8001/api/health`
- Interactive API documentation: `http://127.0.0.1:8001/docs`

The backend must be able to access the cleaned metadata and ChromaDB database at the paths configured in the code.

### Terminal 2: Start the Frontend

```powershell
cd frontend
npm run dev
```

Open the local URL provided by Vite.

The current development configuration uses:

```text
http://localhost:5175
```

The Vite development proxy forwards requests beginning with `/api` to the FastAPI backend at `http://127.0.0.1:8001`.

## API Endpoints

### `GET /api/health`

Checks whether the backend is running.

### `POST /api/recommend`

Accepts a natural-language query and recommendation settings, then returns matching book records.

Depending on the current backend schema, the request can include:

- `query` — the user's natural-language search query.
- `k` — the requested number of recommendations.
- `min_rating` — the optional minimum average rating.

Example request body:

```json
{
  "query": "a story about friendship, magic, and adventure",
  "k": 5,
  "min_rating": 0
}
```

The exact request fields and validation rules are defined by the current FastAPI implementation.

The response contains a list of recommendations with book metadata used by the frontend.

## Local Embeddings

The project uses the Hugging Face model:

`sentence-transformers/all-MiniLM-L6-v2`

The model is loaded through LangChain's `HuggingFaceEmbeddings` integration.

Because embeddings are generated locally, the project does not require a paid OpenAI embedding API or an OpenAI API key for its current semantic-search pipeline.

The initial model download requires internet access. Authentication is generally unnecessary for this public model, although Hugging Face may display an informational warning about unauthenticated requests.

## Testing and Troubleshooting

### `npm` Reports `ENOENT`

This usually means npm cannot find a required file, such as `package.json`, in the current directory.

**Solution:** Run frontend commands from the `frontend` directory.

### The Frontend Loads but Search Fails

Check the following:

1. Confirm that the FastAPI backend is running.
2. Confirm that the backend is listening on port `8001`.
3. Open the browser's Developer Tools and inspect the Console and Network panels.
4. Check the backend terminal for errors.
5. Verify that the API endpoint and request fields match the frontend code.

### The Backend Cannot Find the Dataset or Database

Check that:

- The cleaned CSV exists.
- The ChromaDB database has been built.
- The paths configured in the backend match the actual file locations.
- The application is being started from the expected working directory.

### Python Reports `NameError`

A `NameError` can occur when a variable, function, or class has not been defined or imported before it is used.

In Jupyter Notebook, restart the kernel and run the cells in order if execution order has become inconsistent.

### Duplicate Search Results

Compare the total number of stored documents against the number of unique IDs and unique document contents.

Previously, the database contained 10,394 documents but only 5,197 unique descriptions, indicating duplicate entries. The database was rebuilt and verified to contain 5,197 documents.

Before deleting or rebuilding a persistent vector database, confirm its configured storage location and whether its contents need to be preserved.

### Rating Filtering Returns Fewer Results Than Requested

If the recommender retrieves only `k` candidates and then applies a minimum-rating filter, some candidates may be removed.

A potential improvement is to retrieve a larger candidate pool before filtering, allowing the application to return the requested number of recommendations when enough suitable matches exist.

## Current Limitations and Future Improvements

This is an active learning project. Potential improvements include:

- Evaluate recommendation quality using a consistent collection of test queries.
- Improve candidate retrieval and minimum-rating filtering.
- Improve handling of missing book-cover images and incomplete metadata.
- Expand automated tests for API validation, recommendation ordering, and edge cases.
- Improve production configuration for API routing and deployment.
- Make dataset and vector database paths configurable through environment variables.
- Explore optional LLM-powered explanations or summaries after the retrieval pipeline is stable.

## Learning Goals

This project provides practical experience with:

- Data cleaning and exploratory data analysis using Pandas.
- Text preparation and identifier-based metadata lookup.
- Text embeddings and semantic similarity.
- Vector databases and information retrieval.
- Python module organization and testing.
- REST API development with FastAPI.
- Frontend development with Vue 3 and TypeScript.
- Connecting a frontend to a Python backend.
- Debugging a full-stack application.

## Acknowledgements

- **Dataset:** [7k Books with Metadata — Kaggle](https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata)
- **Tutorial inspiration:** [Build a Semantic Book Recommender with LLMs — freeCodeCamp](https://youtu.be/Q7mS1VHm3Yw?si=8Os6jP2P3AKcFAIG)

---