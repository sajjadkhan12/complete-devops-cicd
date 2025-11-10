from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import random

# Load environment variables from .env file
load_dotenv()

# Get secrets from environment variables
API_SECRET_KEY = os.getenv("API_SECRET_KEY", "default-secret-key")
SERVICE_NAME = os.getenv("SERVICE_NAME", "Poem Service")
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "default-admin-token")

app = FastAPI(title="Poem API", description="A simple API that returns random poems")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (requests proxied through nginx)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Collection of poems
POEMS = [
    {
        "title": "The Road Not Taken",
        "author": "Robert Frost",
        "lines": [
            "Two roads diverged in a yellow wood,",
            "And sorry I could not travel both",
            "And be one traveler, long I stood",
            "And looked down one as far as I could",
            "To where it bent in the undergrowth;"
        ]
    },
    {
        "title": "Stopping by Woods on a Snowy Evening",
        "author": "Robert Frost",
        "lines": [
            "Whose woods these are I think I know.",
            "His house is in the village though;",
            "He will not see me stopping here",
            "To watch his woods fill up with snow."
        ]
    },
    {
        "title": "If",
        "author": "Rudyard Kipling",
        "lines": [
            "If you can keep your head when all about you",
            "Are losing theirs and blaming it on you,",
            "If you can trust yourself when all men doubt you,",
            "But make allowance for their doubting too;"
        ]
    },
    {
        "title": "The Raven",
        "author": "Edgar Allan Poe",
        "lines": [
            "Once upon a midnight dreary, while I pondered, weak and weary,",
            "Over many a quaint and curious volume of forgotten lore—",
            "While I nodded, nearly napping, suddenly there came a tapping,",
            "As of some one gently rapping, rapping at my chamber door."
        ]
    },
    {
        "title": "Sonnet 18",
        "author": "William Shakespeare",
        "lines": [
            "Shall I compare thee to a summer's day?",
            "Thou art more lovely and more temperate:",
            "Rough winds do shake the darling buds of May,",
            "And summer's lease hath all too short a date;"
        ]
    }
]


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to the Poem API! Visit /poem to get a random poem."}


@app.get("/poem")
async def get_random_poem():
    """Returns a random poem"""
    poem = random.choice(POEMS)
    return {
        "title": poem["title"],
        "author": poem["author"],
        "poem": "\n".join(poem["lines"])
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": SERVICE_NAME,
        "api_key_configured": API_SECRET_KEY != "default-secret-key"
    }


@app.get("/config")
async def get_config():
    """Get service configuration (admin only - demonstrates secret usage)"""
    # In a real app, you'd verify the admin token from request headers
    return {
        "service_name": SERVICE_NAME,
        "api_secret_configured": bool(API_SECRET_KEY),
        "admin_token_configured": bool(ADMIN_TOKEN)
    }

