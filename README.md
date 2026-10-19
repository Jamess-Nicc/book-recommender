# 📚 Book Recommender

A book recommendation system project focused on data analysis, data preprocessing, semantic search, and personalized book recommendations.

This project serves as a hands-on learning experience in Python, data science, and machine learning, with the long-term goal of developing an intelligent book recommendation system powered by vector search and Large Language Models (LLMs).

## 🎯 Project Objectives

- Explore and understand real-world book metadata.
- Perform data cleaning and exploratory data analysis (EDA).
- Identify patterns and relationships between book attributes.
- Prepare book descriptions and metadata for vector search.
- Implement semantic search to retrieve books based on the meaning of a query.
- Explore content-based recommendation techniques.
- Investigate how LLMs can improve personalized book recommendations.

## 🛠️ Tech Stack

### Currently Used
- **Python** — Core programming language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical computing
- **Matplotlib / Seaborn** — Data visualization
- **Jupyter Notebook** — Interactive data exploration

### Planned Technologies
- **Scikit-learn** — Machine learning and similarity-based retrieval
- **Vector Search** — Semantic retrieval using numerical representations of book descriptions
- **LLMs** — Natural-language understanding and recommendation generation

*Planned technologies may change as the project develops.*

## 📊 Dataset

This project uses the **7k Books with Metadata** dataset from Kaggle.

**Original dataset:** [7k Books with Metadata — Kaggle](https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata)

The repository includes `books_cleaned.csv`, a preprocessed version of the dataset prepared for further analysis and future vector search experiments.

### Data Preparation

The preprocessing workflow includes:

- Filtering out books whose descriptions contain 25 words or fewer.
- Creating a `title_and_subtitle` column that combines the title and subtitle, using the title alone when the subtitle is missing.
- Creating a column that combines the ISBN-13 identifier and book description for future indexing and retrieval.
- Tracking the word count of each book description.
- Removing columns considered unnecessary for the current stage of analysis.
- Exporting the cleaned dataset to CSV using `index=False` to prevent the DataFrame index from being saved as an additional column.

### Exploratory Data Analysis

The notebook also explores:

- Dataset structure and column data types.
- Missing values in book metadata.
- Book titles, subtitles, and descriptions.
- Numerical features such as page count and average rating.
- Relationships between numerical variables using Spearman correlation.

## 📈 Current Progress

### Completed

- [x] Explored the book metadata dataset.
- [x] Investigated missing values and column data types.
- [x] Analyzed relationships between numerical features using Spearman correlation.
- [x] Filtered books based on description length.
- [x] Created a combined title-and-subtitle field with missing-subtitle handling.
- [x] Prepared a combined ISBN-13 and description field for future retrieval.
- [x] Added description word-count tracking.
- [x] Removed unnecessary columns from the final dataset.
- [x] Exported the preprocessed data to `books_cleaned.csv`.

### Next Steps

- [ ] Review the cleaned dataset for remaining data quality issues.
- [ ] Generate vector embeddings from book descriptions and relevant metadata.
- [ ] Build a vector index for efficient similarity search.
- [ ] Implement semantic search using natural-language queries.
- [ ] Evaluate search relevance and retrieval quality.
- [ ] Develop a baseline content-based recommendation system.
- [ ] Explore LLM integration for more contextual and personalized recommendations.

## 📁 Repository Structure

```text
book-recommender/
├── books_cleaned.csv       # Preprocessed book dataset
├── data-exploration.ipynb  # Data cleaning and exploratory analysis
├── .gitignore              # Files excluded from version control
└── README.md               # Project documentation
```

The repository structure may evolve as the project expands to include embedding generation, vector indexing, and recommendation functionality.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible version
- Git
- Jupyter Notebook or an IDE that supports notebooks

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd book-recommender
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install pandas numpy matplotlib seaborn jupyter
```

### 4. Open the notebook

```bash
jupyter notebook data-exploration.ipynb
```

Alternatively, open `data-exploration.ipynb` directly in PyCharm or another compatible notebook editor.

The notebook may contain dataset paths specific to the development environment. Update those paths if necessary to point to the appropriate local files.

## 🧠 Learning Goals

This project is intended to strengthen my understanding of:

- Data cleaning and preprocessing
- Feature engineering
- Exploratory data analysis and statistical correlation
- Vector embeddings and semantic search
- Similarity measures and information retrieval
- Content-based recommendation systems
- Natural language processing
- LLM integration and AI-assisted recommendations

## 📌 Project Status

**Status:** In Development — Data Preparation Completed for the Current Iteration

The initial data exploration and preprocessing workflow has been implemented. The next major milestone is building a vector search pipeline to retrieve books based on the semantic meaning of their descriptions.

Future development will focus on improving retrieval quality and exploring LLM-assisted book recommendations.

## 👨‍💻 Author

**James Nicdao**

Full-Stack Developer | Python | TypeScript | Vue.js | SQL | Machine Learning

---

*An ongoing learning project exploring the foundations of intelligent book search and recommendation systems.*
