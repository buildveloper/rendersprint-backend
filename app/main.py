import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from pydantic import BaseModel
from contextlib import asynccontextmanager

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class HealthResponse(BaseModel):
    status: str = "ok"
    product: str = "RenderSprint"

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(title="RenderSprint API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "RenderSprint backend is alive!"}

@app.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse()