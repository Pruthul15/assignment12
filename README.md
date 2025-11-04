# Module 12: FastAPI User Authentication & Calculations API

## Overview
This is a production-ready FastAPI application implementing user registration, authentication, and full BREAD (Browse, Read, Edit, Add, Delete) operations for calculations with JWT-based security.

## Features
- ✅ User Registration & Login with JWT tokens
- ✅ Secure password hashing with bcrypt
- ✅ Full CRUD operations for calculations
- ✅ Polymorphic calculation types (addition, subtraction, multiplication, division)
- ✅ PostgreSQL database with SQLAlchemy ORM
- ✅ 96 comprehensive integration tests
- ✅ Docker containerization
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Automated deployment to Docker Hub

## Quick Start

### Local Development
```bash
# Clone repository
git clone https://github.com/Pruthul15/assignment12.git
cd assignment12

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export DATABASE_URL="postgresql://user:password@localhost:5432/fastapi_db"
export JWT_SECRET_KEY="your-secret-key-min-32-chars"

# Run database setup
python -m app.database_init

# Start server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Using Docker
```bash
# Build image
docker build -t assignment12:latest .

# Run container
docker run -p 8000:8000 \
  -e DATABASE_URL="postgresql://user:password@db:5432/fastapi_db" \
  -e JWT_SECRET_KEY="your-secret-key" \
  assignment12:latest

# Or use Docker Compose
docker-compose up --build
```

## API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login and get JWT token
- `POST /auth/token` - Get token (Swagger form)

### Calculations
- `GET /calculations` - Browse all calculations
- `GET /calculations/{id}` - Read specific calculation
- `POST /calculations` - Add new calculation
- `PUT /calculations/{id}` - Edit calculation
- `DELETE /calculations/{id}` - Delete calculation

### Health
- `GET /health` - Server status

## Testing

### Run All Tests
```bash
pytest --cov=app --cov-report=term-missing -v
```

### Run Specific Test Categories
```bash
# Unit tests only
pytest tests/unit/ -v

# Integration tests only
pytest tests/integration/ -v

# E2E tests only
pytest tests/e2e/ -v
```

### Test Results
- ✅ 96 tests PASSED
- ⊘ 4 tests SKIPPED (slow tests)
- 📊 70% code coverage

## Manual Testing via OpenAPI

1. Start the server (see Quick Start)
2. Open: http://localhost:8000/docs
3. Test endpoints:
   - Register: Click "POST /auth/register" → Try it out
   - Login: Click "POST /auth/login" → Try it out
   - Create Calculation: Click "POST /calculations" → Try it out

## Project Structure
```
assignment12/
├── app/
│   ├── auth/              # JWT & authentication
│   ├── models/            # SQLAlchemy models
│   ├── schemas/           # Pydantic schemas
│   ├── operations/        # Calculation operations
│   ├── main.py           # FastAPI app & routes
│   ├── database.py       # Database setup
│   └── core/             # Configuration
├── tests/
│   ├── unit/             # Unit tests
│   ├── integration/      # Integration tests
│   └── e2e/              # End-to-end tests
├── .github/
│   └── workflows/
│       └── test.yml      # CI/CD pipeline
├── docker-compose.yml    # Docker services
├── Dockerfile            # Container definition
├── requirements.txt      # Python dependencies
├── .trivyignore         # Security scan exceptions
└── README.md            # This file
```

## Technologies
- **Framework:** FastAPI 0.120.0
- **Database:** PostgreSQL 17
- **ORM:** SQLAlchemy 2.0.38
- **Authentication:** JWT (PyJWT) + Bcrypt
- **Testing:** Pytest with coverage
- **Containerization:** Docker & Docker Compose
- **CI/CD:** GitHub Actions
- **Registry:** Docker Hub

## Docker Hub
- **Repository:** https://hub.docker.com/r/pruthul123/assignment12
- **Pull:** `docker pull pruthul123/assignment12:latest`
- **Run:** `docker run -p 8000:8000 pruthul123/assignment12:latest`

## CI/CD Pipeline

GitHub Actions workflow runs on every push:

1. **Test Job** - Runs 96 integration tests with PostgreSQL
2. **Security Job** - Trivy vulnerability scanning
3. **Deploy Job** - Builds and pushes to Docker Hub

**View:** https://github.com/Pruthul15/assignment12/actions

## Environment Variables
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/fastapi_db
JWT_SECRET_KEY=your-secret-key-minimum-32-characters
JWT_REFRESH_SECRET_KEY=your-refresh-secret-key-min-32-chars
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
BCRYPT_ROUNDS=12
```

## Author
**Pruthul Patel**  
IS 601: Web Systems Development  

