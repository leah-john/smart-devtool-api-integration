# Smart DevTool for API Integration

## Overview

Smart DevTool is an AI-powered developer assistant that simplifies API integration by automatically analyzing API documentation and generating integration guidance.

Given an API documentation URL and a developer use case, the system:

* Crawls and analyzes API documentation
* Detects the API provider
* Identifies authentication mechanisms
* Extracts available endpoints and resources
* Recommends suitable SDKs
* Generates AI-powered integration recommendations
* Creates ready-to-use wrapper classes
* Allows wrapper download for faster development

The project was developed as part of the AI/ML Hackathon 2026.

---

## Problem Statement

Integrating third-party APIs often requires developers to manually:

* Read lengthy documentation
* Understand authentication methods
* Identify endpoints
* Select SDKs
* Write boilerplate wrapper code

This process is time-consuming and error-prone.

Smart DevTool automates these steps using AI, Retrieval-Augmented Generation (RAG), and documentation analysis.

---

## Features

### Documentation Crawling

Extracts textual content from API documentation URLs using web scraping.

### Provider Detection

Identifies API providers such as:

* PayPal
* Stripe
* GitHub
* Other documented APIs

### Authentication Detection

Detects common authentication mechanisms:

* API Key
* OAuth 2.0
* JWT
* Bearer Token

### Endpoint Extraction

Extracts API endpoints and resources from documentation.

Examples:

* Customers
* Charges
* Refunds
* Payment Intents
* Repositories
* Users

### SDK Recommendations

Suggests official SDKs and integration paths.

Examples:

* Python SDK
* Java SDK
* Node.js SDK
* REST API Integration

### AI-Powered Recommendations

Uses Gemini AI together with retrieved documentation context to generate:

* Integration guidance
* Best practices
* SDK suggestions
* REST alternatives

### Wrapper Generation

Automatically generates reusable wrapper classes based on:

* Authentication type
* Provider
* Available endpoints

### Wrapper Download

Generated wrappers can be downloaded directly from the application.

---

## Solution Architecture

```text
User
 ↓
Next.js Frontend
 ↓
FastAPI Backend
 ↓
Documentation URL
 ↓
Crawler (BeautifulSoup)
 ↓
Text Cleaner
 ↓
Provider Detection
 ↓
Authentication Detection
 ↓
Endpoint Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
ChromaDB Vector Store
 ↓
Context Retrieval
 ↓
Gemini AI
 ↓
Recommendations + Wrapper Generation
 ↓
Download Wrapper
```

---

## Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### Backend

* FastAPI
* Python

### AI & RAG

* Gemini API
* ChromaDB
* Sentence Transformers
* Retrieval-Augmented Generation (RAG)

### Documentation Processing

* BeautifulSoup
* Requests

### Version Control

* Git
* GitHub

---

## Project Structure

```text
smart-devtool-api-integration/

├── backend/
│   ├── app/
│   │   ├── crawler/
│   │   ├── rag/
│   │   ├── services/
│   │   ├── models/
│   │   └── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── package.json
│
├── docs/
    └── screenshots
└── README.md
```
---

## Google Colab Demonstration

A demonstration notebook is included for project presentation and evaluation.

Location:

```text
notebooks/Smart_DevTool_Demo.ipynb
```
---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/your-username/smart-devtool-api-integration.git

cd smart-devtool-api-integration
```

---

### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Run backend:

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

---

## Usage

1. Open the frontend application.
2. Enter API documentation URL.
3. Enter intended use case.
4. Click Analyze Documentation.
5. Review:

   * Provider
   * Authentication Method
   * Endpoints
   * SDK Recommendations
   * AI Recommendations
6. Download generated wrapper code.

---

## Example Input

Documentation URL:

```text
https://developer.paypal.com/docs/api
```

Use Case:

```text
Build an e-commerce website that accepts online payments using PayPal.
```

---

## Example Output

Authentication:

```text
OAuth 2.0
```

Endpoints:

```text
Orders
Payments
Refunds
Subscriptions
```

SDK Recommendations:

```text
PayPal Python SDK
PayPal Java SDK
REST Integration
```

Generated Wrapper:

```python
class PayPalWrapper:
    ...
```

---

## Demo Screenshots

### PayPal Analysis

![PayPal Analysis](docs/screenshots/paypal.png)

### Stripe Analysis

![Stripe Analysis](docs/screenshots/stripe.png)

### GitHub Analysis

![GitHub Analysis](docs/screenshots/github.png)

### Razorpay Analysis

![Razorpay Analysis](docs/screenshots/razorpay.png)

---

## Future Improvements

* OpenAPI/Swagger parsing
* Multi-language wrapper generation
* Docker deployment
* User authentication
* API testing sandbox
* Advanced endpoint discovery
* Multiple LLM support

---

## Known Limitations

AI-powered recommendations and wrapper generation rely on the Google Gemini API.

When Gemini free-tier quota limits are exceeded, the system will continue to perform:

* Documentation crawling
* Provider detection
* Authentication detection
* Endpoint extraction
* SDK recommendation

However, AI-generated recommendations and wrapper generation may be temporarily unavailable until the quota resets.

The application remains functional for documentation analysis even during quota exhaustion.

---

## Contributors

Leah John

B.Tech Computer Science and Engineering

AI/ML Developer
