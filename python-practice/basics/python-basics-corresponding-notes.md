# Python Basics — Corresponding Notes (Day-wise)

This file contains:
- What we practiced
- Why we practiced it
- How to run the code (terminal commands)
- What output to expect (high level)

Code lives only in: `python-basics.py`

---

# Day 1 — Variables, Types, Lists, Dictionaries, Loops, Functions (AWS-themed)

## Goal
Build foundational Python skills using cloud-themed examples (AWS services), because:
- You will use Python daily for backend services, automation, and data pipelines.
- LeetCode problems are basically combinations of lists/dicts/loops/functions.
- Cloud projects often involve building small scripts and APIs that manipulate data.

---

## What we practiced and why (beginner explanation)

### 1) Variables and data types
**What:** stored values in named variables:
- string, int, float, bool

**Why:** everything in programming starts with storing data.
In real work:
- service name (string)
- number of instances (int)
- cost per hour (float)
- production flag (bool)

**What to notice:**
- Python figures out types automatically.
- Printing helps you verify values quickly.

---

### 2) Lists + loops
**What:** created a list of AWS services and looped through it.

**Why:**
- Lists store ordered collections.
- Loops let you process items one-by-one.
In real work:
- list of files to process
- list of API endpoints
- list of cloud resources

**What to notice:**
- `for item in list:` is the most common loop style in Python.

---

### 3) Dictionaries (key → value mapping)
**What:** mapped each AWS service to a category (Compute/Storage/etc.)

**Why:**
- Dictionaries are the most useful Python structure for fast lookups.
- Many interview questions and real systems rely on dict usage.
In real work:
- configuration maps
- ID → object mapping
- caching

**What to notice:**
- `.items()` returns key + value pairs.
- Lookups are fast and simple.

---

### 4) Functions
**What:** wrote a function that prints service info and uses a dictionary lookup.

**Why:**
- Functions let you reuse logic without repeating code.
- Clean code in projects and interviews depends on functions.
In real work:
- helper functions for parsing
- validation helpers
- reusable API utilities

**What to notice:**
- `dict.get(key, default)` prevents errors when a key is missing.
- The `"Unknown"` default is a safe fallback.

---

## How to run Day 1 code (commands)

### Step 1 — Go to repo and activate your environment
```bash
# Go to your repository
cd ~/cloud-engineering-portfolio

# Activate the virtual environment (recommended habit)
source ~/venvs/cloud-engineering-portfolio-venv/bin/activate

# Confirm python path (should point to your venv)
which python

# Confirm python version
python --version
```
### Step 2 — Run the Python basics file
```bash
# Run the python basics script
python python-practice/basics/python-basics.py

# Expected output (high level)
# You should see:
# Printed variable values (EC2, max instances, price, etc.)
# A list of AWS services printed one per line
# A list of service categories printed as service -> category
# Function output for EC2, S3, and CloudFront (CloudFront should show Unknown)
```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Day 2 — Conditions + Safe Parsing + Simple Aggregations

## Goal
Practice Python concepts that appear constantly in:
- LeetCode / interviews
- Data engineering scripts
- Backend services
- Cloud automation

We focused on:
- **if / elif / else**
- **try / except** for safe conversion
- counting categories (running/stopped)
- totals + derived calculations (daily cost)
- de-duplicating values using **set**

## Why we did this (beginner explanation)

### 1) Conditions (if/elif/else)
Real systems handle different states:
- instance is running vs stopped
- request is valid vs invalid
- user exists vs not found

Conditions help your code take the correct path based on data.

### 2) Safe parsing with try/except
In real data, values are not always clean:
- numbers may come as strings
- strings may be missing or invalid

Using `try/except` prevents your program from crashing and lets you handle bad data safely.

### 3) Aggregations (counts + totals)
Most engineering work involves summarizing:
- how many resources are running
- what’s the total cost
- how much per day/week/month

We practiced counts and totals and then calculated a derived metric (daily cost).

### 4) Sets for unique values
Real logs/configurations can contain duplicates.
A `set` removes duplicates, which helps when you need “unique regions/users/IDs”.

## How to run Day 2 code (commands)

### Step 1 — Activate environment
```bash
cd ~/cloud-engineering-portfolio
source ~/venvs/cloud-engineering-portfolio-venv/bin/activate
```

### Step 2 — Run the script
```bash
python python-practice/basics/python-basics.py
# Expected output (high level)
# running/stopped counts
# total hourly cost
# estimated daily cost
# a label (cheap/normal/expensive)
# unique regions printed as a set
```

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


