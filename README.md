# Module 12: FastAPI User Authentication & Calculations BREAD API

## Overview

This is a FastAPI application implementing user registration, authentication, and full BREAD (Browse, Read, Edit, Add, Delete) operations for calculations. The application uses PostgreSQL for persistence, JWT for authentication, and includes comprehensive integration testing.

## Features

- **User Authentication**: Registration and login with password hashing
- **JWT Tokens**: Access and refresh token generation
- **Calculations API**: Full BREAD operations with polymorphic inheritance
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Testing**: 94+ passing tests with 70% code coverage
- **CI/CD**: GitHub Actions with automated Docker deployment
- **Docker**: Complete containerization with Docker Compose

## Tech Stack

- **Backend**: FastAPI, Uvicorn
- **Database**: PostgreSQL 17, SQLAlchemy
- **Authentication**: JWT (PyJWT), Bcrypt
- **Testing**: Pytest, Faker
- **Containerization**: Docker, Docker Compose
- **CI/CD**: GitHub Actions

## Setup & Installation

### Prerequisites

- Docker & Docker Compose
- Python 3.10+ (for local development)
- PostgreSQL (optional - Docker handles this)

### Using Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/Pruthul15/assignment12.git
cd assignment12

# Start all services (web, database, pgAdmin)
docker-compose up --build

# Services will be available at:
# - API: http://localhost:8000
# - Swagger UI: http://localhost:8000/docs
# - pgAdmin: http://localhost:5050 (admin@example.com / admin)
```

### Local Development Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/fastapi_db"
export JWT_SECRET_KEY="super-secret-key-for-jwt-min-32-chars"

# Run database migrations (if needed)
python -m app.database_init

# Start the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

### Authentication

- `POST /auth/register` - User registration
- `POST /auth/login` - User login (JSON)
- `POST /auth/token` - User login (Form data for Swagger)

### Calculations (Requires Authentication)

- `POST /calculations` - Create calculation
- `GET /calculations` - List all user calculations
- `GET /calculations/{calc_id}` - Get specific calculation
- `PUT /calculations/{calc_id}` - Update calculation
- `DELETE /calculations/{calc_id}` - Delete calculation

### Calculation Types

- **addition**: Sum all inputs
- **subtraction**: Subtract all inputs from first value
- **multiplication**: Multiply all inputs
- **division**: Divide first value by all subsequent inputs

### Health Check

- `GET /health` - Server health status

## Testing

### Run All Tests

```bash
# In Docker container or local environment
pytest --cov=app --cov-report=term-missing -v
```

### Expected Results

- **94 tests PASSED**
- **1 test SKIPPED** (slow test - use `--run-slow` to include)
- **70% code coverage**
- **Test types**: Unit tests, Integration tests, E2E tests

### Manual API Testing

1. Open Swagger UI: `http://localhost:8000/docs`
2. Register a user:
   ```json
   {
     "first_name": "John",
     "last_name": "Doe",
     "email": "john@example.com",
     "username": "johndoe",
     "password": "SecurePass123!",
     "confirm_password": "SecurePass123!"
   }
   ```
3. Login to get JWT token
4. Create a calculation:
   ```json
   {
     "type": "addition",
     "inputs": [10, 20, 15]
   }
   ```
5. Test other operations (GET, PUT, DELETE)

## Docker Hub Deployment

### Push to Docker Hub

```bash
# Login to Docker Hub
docker login

# Build image
docker build -t <your-username>/assignment12:latest .

# Push to Docker Hub
docker push <your-username>/assignment12:latest

# Pull and run from Docker Hub
docker run -p 8000:8000 <your-username>/assignment12:latest
```

**Docker Hub**: [pruthul123/assignment12](https://hub.docker.com/r/pruthul123/assignment12)

## Database Structure

### Users Table
- `id` (UUID, Primary Key)
- `username` (String, Unique)
- `email` (String, Unique)
- `password` (String, hashed)
- `first_name` (String)
- `last_name` (String)
- `is_active` (Boolean)
- `is_verified` (Boolean)
- `created_at` (DateTime)
- `updated_at` (DateTime)
- `last_login` (DateTime, nullable)

### Calculations Table
- `id` (UUID, Primary Key)
- `user_id` (UUID, Foreign Key to users)
- `type` (String - polymorphic discriminator)
- `inputs` (JSON array of numbers)
- `result` (Float)
- `created_at` (DateTime)
- `updated_at` (DateTime)

## File Structure

```
assignment12/
├── app/
│   ├── auth/              # JWT and authentication
│   ├── models/            # SQLAlchemy models
│   ├── schemas/           # Pydantic schemas
│   ├── operations/        # Calculation operations
│   ├── main.py            # FastAPI app & routes
│   ├── database.py        # Database setup
│   └── core/              # Configuration
├── tests/
│   ├── e2e/               # End-to-end tests
│   ├── integration/       # Integration tests
│   └── unit/              # Unit tests
├── docker-compose.yml     # Docker services
├── Dockerfile             # Container definition
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Environment Variables

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/fastapi_db
TEST_DATABASE_URL=postgresql://postgres:postgres@db:5432/fastapi_test_db
JWT_SECRET_KEY=super-secret-key-for-jwt-min-32-chars
JWT_REFRESH_SECRET_KEY=super-refresh-secret-key-min-32-chars
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
BCRYPT_ROUNDS=12
```

## Troubleshooting

### "Tables not created" Error

Solution: Tables are created automatically on startup. If you see errors:
```bash
# Restart Docker
docker-compose down
docker-compose up --build
```

### Port Already in Use

```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Or use different port
docker-compose up -e "PORT=8001"
```

### Database Connection Error

```bash
# Check database is running
docker-compose ps

# Check logs
docker-compose logs db
```

## Submission

- **GitHub Repository**: https://github.com/Pruthul15/assignment12
- **Docker Hub**: https://hub.docker.com/r/pruthul123/assignment12
- **Test Coverage**: 70%
- **Tests Passing**: 94/100
- **Status**: ✅ Ready for Production

## Learning Outcomes

This project demonstrates:
- FastAPI web framework
- User authentication and JWT tokens
- Database design with SQLAlchemy ORM
- Polymorphic inheritance patterns
- Comprehensive testing (unit, integration, E2E)
- Docker containerization
- CI/CD pipelines
- RESTful API design

## License

MIT License - Course Assignment

## Author

Pruthul Patel  
IS 601: Web Systems Development  
Fall 2025