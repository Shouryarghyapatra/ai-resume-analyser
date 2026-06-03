# AI Resume Analyser

An AI-powered Resume Analysis and Job Matching System that evaluates the semantic alignment between a candidate's resume and job descriptions using modern Natural Language Processing (NLP), Sentence Embeddings, and Transformer-based Re-ranking models.

## Overview

AI Resume Analyser helps job seekers assess how well their resumes match job requirements. The system extracts resume content from PDF files, generates semantic embeddings, retrieves the most relevant job descriptions, and computes similarity scores to provide meaningful matching insights.

The application supports:

* Resume vs Job Description Database Matching
* Resume vs Custom Job Description Matching
* Semantic Similarity Scoring
* Transformer-based Re-ranking
* Interactive Streamlit Interface
* Dockerized Deployment
* Cloud Deployment on AWS EC2

---

## Features

### Resume Parsing

* Extracts text from uploaded PDF resumes
* Supports text-based PDF resumes
* Resume cleaning and preprocessing pipeline

### Semantic Search

* Generates dense vector embeddings using Sentence Transformers
* Retrieves top matching job descriptions using vector similarity search

### Transformer Re-ranking

* Uses cross-encoder models for contextual relevance scoring
* Produces more accurate matching results than traditional keyword approaches

### Job Description Database Matching

* Matches uploaded resumes against a curated repository of job descriptions
* Displays ranked job matches

### Custom JD Matching

* Allows users to paste their own Job Description
* Generates a semantic match score instantly

### Interactive Dashboard

* Built with Streamlit
* User-friendly interface
* Resume preview
* Match score visualization

### Deployment Ready

* Dockerized application
* AWS EC2 deployment support
* CI/CD ready architecture

---

## Project Architecture

```text
Resume PDF
     │
     ▼
Resume Parser
     │
     ▼
Text Cleaning
     │
     ▼
Sentence Transformer Embeddings
     │
     ▼
Vector Retrieval (Top-K JDs)
     │
     ▼
Cross Encoder Re-ranking
     │
     ▼
Similarity Scores
     │
     ▼
Interactive Streamlit Dashboard
```

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### NLP & Machine Learning

* Sentence Transformers
* Hugging Face Transformers
* PyTorch
* NumPy

### PDF Processing

* pdfplumber
* pdf2image (optional OCR workflow)
* pytesseract

### Deployment

* Docker
* AWS EC2
* GitHub Actions (CI/CD ready)

---

## Folder Structure

```text
AI-Resume-Analyser/
│
├── app/
│   └── app.py
│
├── src/
│   ├── parser2.py
│   ├── preprocess.py
│   ├── embedder.py
│   ├── retriever.py
│   ├── reranker.py
│   └── pipeline.py
│
├── data/
│   └── jobs_text/
│
├── temp/
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/ai-resume-analyser.git

cd ai-resume-analyser
```

### Create Virtual Environment

```bash
python -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running Locally

```bash
streamlit run app/app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## Docker Deployment

### Build Docker Image

```bash
docker build -t ai-resume-analyser .
```

### Run Container

```bash
docker run -d \
-p 8501:8501 \
--name ai-resume-analyser \
ai-resume-analyser
```

Open:

```text
http://localhost:8501
```

---

## AWS EC2 Deployment

1. Launch Ubuntu EC2 Instance
2. Install Docker
3. Clone Repository
4. Build Docker Image
5. Run Container
6. Configure Security Group:

   * Port 22 (SSH)
   * Port 8501 (Streamlit)

Access:

```text
http://<EC2_PUBLIC_IP>:8501
```

---

## Future Improvements

* ATS Score Prediction
* Resume Section Analysis
* Keyword Gap Detection
* Skill Extraction
* Resume Improvement Suggestions
* FastAPI Backend
* React Frontend
* PostgreSQL Storage
* Vector Database Integration (FAISS / ChromaDB)
* Multi-Resume Comparison
* Production CI/CD Pipeline

---

## Use Cases

* Job Seekers
* Career Coaches
* Recruitment Teams
* HR Departments
* University Placement Cells
* Resume Screening Platforms

---

## Key Learning Outcomes

* NLP Pipeline Development
* Semantic Search Systems
* Transformer-based Re-ranking
* Dockerization
* AWS Deployment
* Streamlit Application Development
* End-to-End MLOps Workflow

---

## Author

Shouryarghya Patra

Data Analyst | NLP Enthusiast | Machine Learning Practitioner

LinkedIn: Add your LinkedIn URL here

GitHub: Add your GitHub URL here
