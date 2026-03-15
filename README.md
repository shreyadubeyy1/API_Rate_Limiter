# API Rate Limiter ⚡

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![Redis](https://img.shields.io/badge/Redis-In--Memory-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

A lightweight backend service built using **FastAPI** and **Redis** to control API request frequency and prevent excessive usage. The system tracks request counts per client and restricts access when requests exceed a defined limit within a specific time window.

---

## 🚀 Project Overview

**API Rate Limiter** demonstrates backend concepts such as API protection, request throttling, Redis-based request tracking, and modular FastAPI architecture.

This project is production-ready in structure and easy to deploy on any cloud platform.

---

## 📌 Problem Statement

Public APIs are vulnerable to abuse through excessive or automated requests. Without rate limiting, a single user or bot can repeatedly hit API endpoints and overload the server — leading to degraded performance or service downtime.

This project builds a backend rate limiting system that:

- Restricts how many requests a client can make within a defined time window
- Prevents API abuse and spam traffic
- Ensures fair usage of backend resources among multiple clients

---

## ⚙️ How the System Works
```
Client Request → Identify by IP → Redis Tracks Count → Check Limit
                                                             │
                                              ┌──────────────┴──────────────┐
                                         Under Limit                   Over Limit
                                              │                              │
                                        ✅ 200 OK                   ❌ 429 Too Many Requests
                                    Return API Response            Redis resets after TTL expires
```

1. A client sends a request to the API endpoint
2. The system identifies the client using its **IP address**
3. **Redis** stores and tracks the request count for that client
4. Each request increments the stored counter
5. If the count exceeds the allowed limit within the time window → **HTTP 429** is returned
6. Redis **automatically resets** the counter after the expiration time

> Redis is used because it provides fast in-memory operations, making it ideal for tracking high-frequency API requests.

---

## 🧱 Features

- **FastAPI Backend** — Lightweight, high-performance API framework
- **Redis-Powered Tracking** — Fast in-memory request count storage
- **IP-Based Rate Limiting** — Identifies and limits clients by IP address
- **Configurable Limits** — Easily adjust request limits and time windows
- **Auto Counter Reset** — Redis TTL handles expiration automatically
- **429 Protection** — Returns proper HTTP error on limit breach
- **Modular Structure** — Clean separation of config, logic, and routes
- **Lightweight** — Easy to run locally or deploy to cloud

---

## 🗂 Project Structure
```
api-rate-limiter/
│
├── app/
│   ├── config.py          # Redis connection configuration
│   ├── limiter.py         # Rate limiting logic
│   └── main.py            # FastAPI application and endpoints
│
├── requirements.txt       # Python dependencies
├── .gitignore             # Files ignored by Git
└── README.md
```

---

## ⚙️ Tech Stack

| Layer              | Technology              |
| ------------------ | ----------------------- |
| Language           | Python 3.10+            |
| Backend Framework  | FastAPI                 |
| In-Memory Store    | Redis                   |
| ASGI Server        | Uvicorn                 |
| API Testing        | Postman / Browser       |
| Version Control    | Git / GitHub            |

---

## 🔌 API Endpoints

| Method | Endpoint | Description              |
| ------ | -------- | ------------------------ |
| GET    | `/`      | Health check             |
| GET    | `/data`  | Rate-limited endpoint    |

**Home Endpoint:**
```json
GET /
// Response:
{
  "message": "API Rate Limiter Running"
}
```

**Rate Limited Endpoint:**
```json
GET /data
// Success Response (200):
{
  "message": "You accessed a rate limited endpoint"
}

// Rate Limit Exceeded (429):
{
  "detail": "Too many requests. Please try again later."
}
```

---

## 💻 Getting Started

### Prerequisites

- Python 3.10+
- Redis installed locally
- Git

---

### 1️⃣ Clone the repository
```bash
git clone https://github.com/shreyadubeyy1/API_Rate_Limiter.git
cd API_Rate_Limiter
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Start Redis server
```bash
redis-server
```

### 5️⃣ Run the FastAPI server
```bash
uvicorn app.main:app --reload
```

### 6️⃣ Test the API
```
# Home endpoint
http://127.0.0.1:8000

# Rate-limited endpoint
http://127.0.0.1:8000/data
```

> 💡 Refresh `/data` multiple times quickly to observe the rate limiting behavior in action.

---

## ☁️ Deployment

This project can be deployed on:

- **AWS EC2** — Full control VM deployment
- **Render / Railway** — Simple Git-based deployment
- **DigitalOcean** — Droplet or App Platform
- **Docker** — Containerized environments

Redis can be deployed as a **managed service** (Redis Cloud, AWS ElastiCache) or as a **containerized instance** alongside the API server.

---

## 🔮 Future Improvements

- Middleware-based **global rate limiting**
- **API key or user-based** rate limiting
- **Sliding window** rate limiting algorithm
- **Token bucket** or leaky bucket algorithms
- Logging and monitoring of blocked requests
- Dashboard for **rate limit analytics**
- **Distributed rate limiting** across multiple servers

---

## 🎯 Key Engineering Concepts Demonstrated

- Real-world **API protection and throttling** implementation
- **Redis** as an in-memory data store for high-frequency tracking
- Clean **modular FastAPI architecture**
- Understanding of **HTTP status codes** and RESTful design
- **TTL-based auto-expiry** logic using Redis

---

## 📚 References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Redis Documentation](https://redis.io/docs/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

---

## 📄 License

MIT License — free to use and modify.
