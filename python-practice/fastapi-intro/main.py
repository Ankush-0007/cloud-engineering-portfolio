# Day 1 — Minimal FastAPI Health Check (REFERENCE)
# NOTE: This block is kept for history; it is commented out so it does not run.
# ------------------------------------------------------------------------------

# # Import FastAPI so we can create an API application
# from fastapi import FastAPI
#
# # Create the FastAPI application object (this is the API "app")
# app = FastAPI()
#
# # Create a GET endpoint used to check server health ("/health")
# @app.get("/health")
# def health():
#     # Return a standard health response
#     return {"status": "ok"}

# ================================================================================================================================
# ================================================================================================================================


# Day 2 — Notes API (ACTIVE)
# NOTE: This is the currently running code.
# ------------------------------------------

# Import FastAPI so we can create an API application
from fastapi import FastAPI

# Import BaseModel so we can validate incoming JSON request data
from pydantic import BaseModel

# Import List so we can type-hint a list of notes (improves readability and tooling)
from typing import List

# Create the FastAPI application object (this is the API "app")
app = FastAPI()

# Define the schema for a note that the client will send in a POST request
class NoteCreate(BaseModel):
    # Define the title field as a string (required)
    title: str
    # Define the content field as a string (required)
    content: str


# Create an in-memory list to store notes temporarily (acts like a fake database today)
NOTES: List[NoteCreate] = []


# Create a GET endpoint for the root URL ("/")
@app.get("/")
def root():
    # Return a simple JSON message so we can confirm the API is running
    return {"message": "Notes API is running"}


# Create a GET endpoint used to check server health ("/health")
@app.get("/health")
def health():
    # Return a standard health response
    return {"status": "ok"}


# Create a POST endpoint to create a new note ("/notes")
@app.post("/notes")
def create_note(note: NoteCreate):
    # Add the validated note object to our in-memory list
    NOTES.append(note)
    # Return confirmation plus the created note
    return {"message": "note created", "note": note}


# Create a GET endpoint to list all notes ("/notes")
@app.get("/notes")
def list_notes():
    # Return how many notes exist and the list of notes
    return {"count": len(NOTES), "notes": NOTES}
