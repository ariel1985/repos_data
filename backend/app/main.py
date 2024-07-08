from fastapi import FastAPI
from app.api import repos
from app.db.database import connect_db, close_db

app = FastAPI()

# Include routers
app.include_router(repos.router, prefix="/api/repos", tags=["repos"])

# Database connection events
@app.on_event("startup")
async def startup_db_client():
    await connect_db()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_db()
