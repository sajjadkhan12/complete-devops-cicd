# Microservices Project

A simple microservices architecture with two backend services and a Vue.js frontend.

## Architecture

- **microservice-poem** - FastAPI service on port 8000 that returns random poems
- **microservice-quote** - FastAPI service on port 8001 that returns random quotes
- **frontend** - Vue.js application on port 3000 that displays content from both services

## Quick Start

### 1. Setup Backend Services

**Poem Service:**
```bash
cd microservice-poem
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Quote Service:**
```bash
cd microservice-quote
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

### 2. Setup Frontend

```bash
cd frontend
npm install
npm run dev
```

### 3. Access

- Frontend: http://localhost:3000
- Poem API: http://localhost:8000
- Quote API: http://localhost:8001

## Environment Variables

Each microservice uses a `.env` file for configuration:
- `API_SECRET_KEY` - Secret key for the service
- `SERVICE_NAME` - Name of the service
- `ADMIN_TOKEN` - Admin authentication token

Copy `.env.example` to `.env` and update the values.

## Docker Deployment

### Build and Run with Docker Compose

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

### Build Individual Services

**Poem Service:**
```bash
cd microservice-poem
docker build -t poem-service .
docker run -p 8000:8000 --env-file .env poem-service
```

**Quote Service:**
```bash
cd microservice-quote
docker build -t quote-service .
docker run -p 8001:8001 --env-file .env quote-service
```

**Frontend:**
```bash
cd frontend
docker build -t frontend .
docker run -p 3000:80 frontend
```

## API Endpoints

**Poem Service (port 8000):**
- `GET /poem` - Get a random poem
- `GET /health` - Health check
- `GET /config` - Service configuration

**Quote Service (port 8001):**
- `GET /quote` - Get a random quote
- `GET /quotes` - Get all quotes
- `GET /health` - Health check
- `GET /config` - Service configuration

