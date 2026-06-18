"""
Main FastAPI application entry point.
"""

from fastapi import FastAPI

from src.api.routes import router

app = FastAPI(title="Contextual Knowledge Retrieval System API")
app.include_router(router)
app.state.description_ = ""


@app.get("/")
async def root():
    """Root endpoint to verify API is running."""
    return {"message": "Contextual Knowledge Retrieval System API is running"}
