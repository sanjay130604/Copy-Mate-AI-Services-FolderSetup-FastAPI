CopyMate – AI Services (FastAPI)

This repository contains the AI Services backend for CopyMate, an AI-powered marketing copy generator.
It provides APIs for generating copy, managing personas, storing brand memory, handling feedback, and more — all powered by FastAPI + MongoDB + AI/LLMs.

Features

JWT Authentication (Login/Register)
AI Copy Generation (AIDA, PAS, Multi-Format)
Persona Management (CRUD APIs)
Brand Memory (Voice, Tone, Pillars)
Copy History & Versioning
Feedback Loop & Real-Time Collaboration
Analytics Dashboard Support
Export Options (TXT, PDF, CSV)


Project Structure

AI-Services-FastAPI/
│── app/
│   ├── main.py                 # FastAPI entry point
│   ├── api/                    # API routes
│   ├── core/                   # Config & security
│   ├── services/                # AI + business logic
│   ├── models/                  # DB schemas (Pydantic/Mongo)
│   ├── db/                      # MongoDB connection
│   ├── utils/                   # Helpers (logging, responses)
│   └── tests/                   # Unit & integration tests
│
├── .env                         # Env variables (DB, API keys)
├── requirements.txt             # Dependencies
├── README.md                    # Project docs


Tech Stack

Framework: FastAPI

Database: MongoDB

AI/ML: Google Gemini API (or OpenAI as fallback)

Auth: JWT-based Authentication

Deployment: Uvicorn / Docker-ready


| Endpoint                | Method | Description                |
| ----------------------- | ------ | -------------------------- |
| `/api/v1/auth/register` | POST   | Register new user          |
| `/api/v1/auth/login`    | POST   | User login (JWT)           |
| `/api/v1/ai/generate`   | POST   | Generate marketing copy    |
| `/api/v1/ai/feedback`   | POST   | Submit feedback on copy    |
| `/api/v1/persona`       | CRUD   | Manage personas            |
| `/api/v1/brand`         | CRUD   | Save & manage brand memory |
| `/api/v1/history`       | GET    | Fetch copy history         |
