# Job Tracker

A full-stack job application tracking system that automatically monitors Gmail, extracts job application updates, and maintains the complete lifecycle of every application.

Instead of manually updating spreadsheets, Job Tracker automatically reads incoming recruitment emails, links them to existing applications, updates their current stage, and provides a dashboard to track the entire hiring process.

> **Status:** 🚧 Under Active Development

---

# Motivation

After applying to hundreds of jobs, keeping track of applications became increasingly difficult.

Recruiters send multiple emails throughout the hiring process:

- Application Confirmation
- Assessment Invitation
- Technical Interview
- HR Interview
- Offer
- Rejection

Most job trackers only record that an application exists.

This project aims to automatically understand the journey of every application directly from Gmail while providing a clean, scalable backend architecture suitable for production.

---

# Features

## Current

- Gmail OAuth2 Authentication
- Gmail API Integration
- Read emails from Gmail
- Parse Gmail messages into structured data
- Store emails in PostgreSQL
- Prevent duplicate email processing
- Repository pattern implementation
- SQLAlchemy ORM
- FastAPI backend
- Layered architecture

---

## Planned

- Automatic application creation
- Email to Application linking
- Status progression tracking
- Timeline of every application
- React Dashboard
- Search and filtering
- Company analytics
- Interview tracking
- AI-powered email classification
- Resume and cover letter storage
- Application insights and statistics

---

# Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Gmail API
- Google OAuth2

## Frontend (Planned)

- React
- TypeScript
- TailwindCSS

## AI (Planned)

- OpenAI API
- Embedding-based email similarity
- LLM-powered email classification

---

# Architecture

```
React Frontend
        │
        ▼
FastAPI REST API
        │
        ▼
Service Layer
        │
        ▼
Repository Layer
        │
        ▼
SQLAlchemy ORM
        │
        ▼
PostgreSQL
```

Business logic is intentionally isolated from:

- API Routes
- Database Models
- Frontend

making each layer independently testable and maintainable.

---

# Project Structure

```
backend/
│
├── app/
│   ├── api/
│   │
│   ├── core/
│   │
│   ├── database/
│   │
│   ├── models/
│   │   ├── application.py
│   │   ├── email.py
│   │   └── oauth_token.py
│   │
│   ├── repositories/
│   │
│   ├── services/
│   │   ├── gmail_service.py
│   │   ├── email_processor.py
│   │   └── application_service.py
│   │
│   └── schemas/
│
└── main.py

frontend/ (planned)
```

---

# Current Data Flow

```
Gmail
   │
   ▼
Gmail API
   │
   ▼
gmail_service.py
   │
   ▼
email_processor.py
   │
   ▼
Repositories
   │
   ▼
PostgreSQL
```

---

# Database Design

## Applications

Represents a single job application.

Contains information such as:

- Company
- Role
- Current Status
- Date Applied
- Last Updated

One application may have many emails.

---

## Emails

Stores immutable email records retrieved from Gmail.

Includes:

- Gmail Message ID
- Gmail Thread ID
- Subject
- Sender
- Received Date
- Snippet

Emails are never modified after insertion.

---

# Design Principles

## Repository Pattern

Database access is isolated inside repositories.

Example:

```python
ApplicationRepository.create()
ApplicationRepository.get_by_company_and_role()

EmailRepository.exists_by_message_id()
EmailRepository.list_by_thread_id()
```

---

## Service Layer

Business logic belongs inside services.

Examples:

- processing emails
- creating applications
- updating application status
- Gmail synchronization

---

## Thin API Layer

FastAPI endpoints should only:

- validate requests
- call services
- return responses

No business logic should exist inside API routes.

---

# Current Progress

## Completed

- Project architecture
- FastAPI setup
- PostgreSQL integration
- SQLAlchemy models
- Gmail OAuth
- Gmail API integration
- Email retrieval
- Email parsing
- Repository layer
- Duplicate email detection

---

## In Progress

- Email processing pipeline
- Application creation workflow
- Thread-based email linking
- Status update engine

---

## Upcoming

- REST endpoints
- React frontend
- Dashboard
- Authentication
- AI email classification
- Analytics
- Docker deployment
- Unit tests
- CI/CD pipeline

---

# Future AI Features

Instead of relying solely on keyword matching, future versions will use LLMs to understand recruitment emails.

Examples:

```
"We'd love to invite you for a technical interview."

↓

Interview Stage
```

```
"Unfortunately we have decided to move forward with another candidate."

↓

Rejected
```

This will allow much more accurate classification than simple rule-based matching.

---

# Long-Term Vision

The goal is to evolve Job Tracker into a personal career management platform capable of:

- Tracking every application automatically
- Understanding recruitment conversations
- Providing interview analytics
- Measuring application success rates
- Generating job search insights
- Serving as a portfolio-quality demonstration of scalable backend architecture and AI integration

---

# Development Roadmap

- [x] FastAPI backend
- [x] PostgreSQL
- [x] SQLAlchemy models
- [x] Gmail OAuth
- [x] Gmail email retrieval
- [x] Repository pattern
- [ ] Application lifecycle engine
- [ ] REST API
- [ ] React frontend
- [ ] Dashboard
- [ ] AI email classification
- [ ] Semantic email matching
- [ ] Analytics
- [ ] Docker
- [ ] Automated testing
- [ ] CI/CD

---

# License

This project is being developed as a personal learning and portfolio project.