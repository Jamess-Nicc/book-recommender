from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from recommender import recommend_books


# Create the FastAPI application
app = FastAPI(
    title="Book Recommender API",
    description="A semantic book recommendation API.",
    version="1.0.0"
)


# Define the expected search request
class RecommendationRequest(BaseModel):
    query: str = Field(
        min_length=1,
        max_length=500,
        description="Describe the kind of book you want."
    )

    k: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Number of recommendations to return."
    )

    min_rating: float | None = Field(
        default=None,
        ge=0,
        le=5,
        description="Optional minimum book rating."
    )


# Basic health-check endpoint
@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "message": "Book Recommender API is running."
    }


# Book recommendation endpoint
@app.post("/api/recommend")
def get_recommendations(request: RecommendationRequest):
    try:
        results = recommend_books(
            query=request.query,
            k=request.k,
            min_rating=request.min_rating
        )

        # Convert the Pandas DataFrame to JSON-compatible records
        books = results.to_dict(orient="records")

        return {
            "query": request.query,
            "count": len(books),
            "recommendations": books
        }

    except Exception as exc:
        print(f"Recommendation error: {exc}")

        raise HTTPException(
            status_code=500,
            detail="An error occurred while generating recommendations."
        )