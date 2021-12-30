from fastapi import FastAPI
import uvicorn

app = FastAPI(title="test")

@app.get("/")
async def root():
    return {"message": "Application Running!"}

@app.get("/test")
async def root():
    return {"message": "Test Running!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        reload=True
        )