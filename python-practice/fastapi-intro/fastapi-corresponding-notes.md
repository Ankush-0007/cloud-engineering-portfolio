# Day 1 — Minimal FastAPI Health Check

## What we built
A very small FastAPI app with one endpoint:

- `GET /health` → returns JSON: `{"status": "ok"}`

## Why we did this (beginner explanation)
On Day 1, the goal was **not** to build a full application. The goal was to prove 3 core things:

1) **You can run a backend server locally**
- This is the first step before you ever deploy anything to AWS/GCP.

2) **You understand what an endpoint is**
- An endpoint is a URL path (like `/health`) that your server listens to.
- When a client calls that path, your code runs and returns a response.

3) **You can return JSON**
- Most real backend systems communicate using JSON.
- FastAPI automatically converts Python dictionaries into JSON responses.

## Concepts you learned
### 1) `FastAPI()` creates your application
- `app = FastAPI()` is the main object that represents your API server.

### 2) `@app.get("/health")` creates a route
- This is called a **decorator**.
- It tells FastAPI: “When someone sends a GET request to `/health`, run this function.”

### 3) Returning a dictionary becomes JSON
- `return {"status": "ok"}` returns a Python dictionary.
- FastAPI converts it into a JSON HTTP response automatically.

## How to run and test it (commands)

> Important: commands are run in the **Terminal**, not inside Python (`>>>`).

### Step 1 — Go to your repo and activate the virtual environment
```bash
# Go to your repository folder
cd ~/cloud-engineering-portfolio

# Activate the virtual environment (so we use the correct Python + installed packages)
source ~/venvs/cloud-engineering-portfolio-venv/bin/activate

# Confirm which python is active (should point to ~/venvs/...)
which python

# Confirm python version
python --version
```

### Step 2 — Start the FastAPI server (Uvicorn)
```bash
# Move to the folder that contains main.py
cd ~/cloud-engineering-portfolio/python-practice/fastapi-intro

# Run the server (reload means auto-restart when file changes)
uvicorn main:app --reload
```

### Step 3 — Test the health endpoint
```bash
Open a new terminal (or another tab) and run:
# Call the health endpoint
curl -s http://127.0.0.1:8000/health
```

### Step 4 — Stop the server
```bash
In the terminal where Uvicorn is running:
Press Ctrl + C
```

### Step 5 — Confirm the server is stopped
```bash
# Without -s so you can see the error clearly
curl http://127.0.0.1:8000/health
```

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Day 2 — Notes API (Model + POST + GET)

## What we built
We upgraded the app from a simple health check into a tiny “Notes API” with these endpoints:

- `GET /` → confirms the API is running
- `GET /health` → health check endpoint
- `POST /notes` → create a note (send JSON)
- `GET /notes` → list all notes

Notes were stored in a **temporary in-memory list** (a simple Python list). This is like a “fake database” for practice. Later we’ll replace this with a real database (e.g., DynamoDB).

---

## Why we did this (beginner explanation)
In real backend work, the most common flow is:

1) A client sends data to your server (usually JSON)
2) Your server validates the data (to prevent bad input)
3) Your server stores it (in memory, a database, etc.)
4) Your server returns data back to the client

Today’s API is the smallest version of that pattern.

This also connects directly to your Cloud project goal:
- Local API today
- AWS Serverless API later (API Gateway + Lambda + DynamoDB)

---

## Concepts learned (simple)

### 1) GET vs POST
- **GET** = read data (should not change server state)
- **POST** = create data (changes server state by adding something)

### 2) Data validation using a model (Pydantic)
We used a model because:
- it ensures the JSON includes the correct fields (`title`, `content`)
- it ensures the values have correct types (strings)
- it stops invalid requests early, before they break your code

### 3) Temporary storage (in-memory list)
We stored notes in a list because:
- it’s the fastest way to practice CRUD-like behavior
- it proves the API state changes after a POST
Important limitation:
- if you restart the server, the list becomes empty (because it lives in RAM)

---

## How to run and test it (commands)

### Step 1 — Activate the virtual environment (correct Python)
```bash
# Go to your repository
cd ~/cloud-engineering-portfolio

# Activate the virtual environment so we use the correct python + packages
source ~/venvs/cloud-engineering-portfolio-venv/bin/activate

# Confirm the active interpreter
which python

# Confirm python version
python --version
```

### Step 2 — Start the server
```bash
# Go to the FastAPI folder where main.py exists
cd ~/cloud-engineering-portfolio/python-practice/fastapi-intro

# Start the FastAPI app using uvicorn (reload auto-restarts on file changes)
uvicorn main:app --reload
```

### Step 3 — Test endpoints (while server is running)

### 3.1 Test root endpoint
```bash
# Why: confirms server is reachable and responding.
curl -s http://127.0.0.1:8000/
```

### 3.2 Confirm notes list is empty initially
```bash
# Why: confirms /notes exists and storage starts empty.
curl -s http://127.0.0.1:8000/notes
```

### 3.3 Create a note (POST)
```bash
# Why: proves server can accept JSON, validate it, and store it.
curl -s -X POST http://127.0.0.1:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title":"day2","content":"first note from FastAPI"}'
```

### 3.4 Fetch notes again (GET)
```bash
# Why: proves POST changed server state (note is stored).
curl -s http://127.0.0.1:8000/notes
```

### Step 4 — Stop the server
```bash
# In the terminal where uvicorn is running:
Press Ctrl + C
```

### Step 5 — Confirm the server is stopped (important)
```bash
# Why: confirms nothing is listening on port 8000 anymore.
curl http://127.0.0.1:8000/health
```

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

