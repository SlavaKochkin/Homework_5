from fastapi import FastAPI
from app.routers import pages, api


app = FastAPI(title="Homework 05", description="FastAPI Web App")


app.include_router(pages.router)
app.include_router(api.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
