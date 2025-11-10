from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="Quote API", description="A simple API that returns random inspirational quotes")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Collection of quotes
QUOTES = [
    {
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
        "category": "Motivation"
    },
    {
        "quote": "Innovation distinguishes between a leader and a follower.",
        "author": "Steve Jobs",
        "category": "Innovation"
    },
    {
        "quote": "Life is what happens to you while you're busy making other plans.",
        "author": "John Lennon",
        "category": "Life"
    },
    {
        "quote": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt",
        "category": "Dreams"
    },
    {
        "quote": "It is during our darkest moments that we must focus to see the light.",
        "author": "Aristotle",
        "category": "Perseverance"
    },
    {
        "quote": "The way to get started is to quit talking and begin doing.",
        "author": "Walt Disney",
        "category": "Action"
    },
    {
        "quote": "Don't let yesterday take up too much of today.",
        "author": "Will Rogers",
        "category": "Time"
    },
    {
        "quote": "You learn more from failure than from success.",
        "author": "Unknown",
        "category": "Learning"
    },
    {
        "quote": "If you are working on something exciting that you really care about, you don't have to be pushed. The vision pulls you.",
        "author": "Steve Jobs",
        "category": "Passion"
    },
    {
        "quote": "People who are crazy enough to think they can change the world, are the ones who do.",
        "author": "Rob Siltanen",
        "category": "Change"
    }
]


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to the Quote API! Visit /quote to get a random quote."}


@app.get("/quote")
async def get_random_quote():
    """Returns a random quote"""
    quote = random.choice(QUOTES)
    return {
        "quote": quote["quote"],
        "author": quote["author"],
        "category": quote["category"]
    }


@app.get("/quotes")
async def get_all_quotes():
    """Returns all available quotes"""
    return {"quotes": QUOTES, "total": len(QUOTES)}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

