from recommender import recommend_books, db_books

# 1. Verify the database
print("--- DATABASE CHECK ---")
print("Documents stored:", db_books._collection.count())

# 2. Test semantic recommendations
print("\n--- SEMANTIC SEARCH ---")

results = recommend_books(
    query="A fantasy story about magic and friendship",
    k=5
)

print(results[["title", "authors", "average_rating"]])

# 3. Test the minimum-rating filter
print("\n--- BOOKS RATED 4.0 OR HIGHER ---")

filtered_results = recommend_books(
    query="A fantasy story about magic and friendship",
    k=5,
    min_rating=4.0
)

print(filtered_results[["title", "authors", "average_rating"]])