from fastapi import FastAPI
import uvicorn
from routes import router

app = FastAPI(
    title="Student Tracking Backend",
    description="Tracks student's whereabouts",
    version="0.1",
    docs_url=None,
    redoc_url=None
)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)