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

## Manual Testing via Swagger UI

### Access OpenAPI Documentation
1. Start the server: `uvicorn app.main:app --reload`
2. Open browser: http://localhost:8000/docs
3. You'll see the interactive Swagger UI with all endpoints

---

## Complete Manual Testing Workflow

### STEP 1: User Registration

**Endpoint:** `POST /auth/register`

1. In Swagger, find **POST /auth/register** (green button)
2. Click **"Try it out"**
3. Fill in the request body:

```json
{
  "username": "newuser2025",
  "email": "newuser@example.com",
  "password": "NewPass@2025",
  "confirm_password": "NewPass@2025",
  "first_name": "John",
  "last_name": "Doe"
}
```

4. Click **"Execute"**
5. Expected Response (201 Created):

```json
{
  "id": "e3bd24d0-93ff-4187-9fcc-8233bd7ccae1",
  "username": "newuser2025",
  "email": "newuser@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "is_active": true,
  "is_verified": false,
  "created_at": "2025-11-10T14:45:33.816308Z",
  "updated_at": "2025-11-10T14:45:33.816318Z"
}
```

**cURL Command:**
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"username": "newuser2025", "email": "newuser@example.com", "password": "NewPass@2025", "confirm_password": "NewPass@2025", "first_name": "John", "last_name": "Doe"}'
```

**Password Requirements:**
- Minimum 8 characters
- At least one special character (@, !, #, $, %, etc.)
- Recommended: Mix of uppercase, lowercase, numbers, and special chars

---

### STEP 2: User Login

**Endpoint:** `POST /auth/login`

1. Find **POST /auth/login** (green button)
2. Click **"Try it out"**
3. Fill in the request body:

```json
{
  "username": "newuser2025",
  "password": "NewPass@2025"
}
```

4. Click **"Execute"**
5. Expected Response (200 OK):

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_at": "2025-11-10T03:00:38.558412Z",
  "user_id": "e3bd24d0-93ff-4187-9fcc-8233bd7ccae1",
  "username": "newuser2025",
  "email": "newuser@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "is_active": true,
  "is_verified": false
}
```

**⚠️ IMPORTANT:** Copy the `access_token` value - you'll need it for all calculation endpoints!

**cURL Command:**
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"username": "newuser2025", "password": "NewPass@2025"}'
```

---

### STEP 3: Authorize in Swagger UI

1. At the **top right** of Swagger page, find **"Authorize"** button (🔓 lock icon)
2. Click **"Authorize"**
3. Paste your `access_token` from login response
4. Click **"Authorize"** in the popup
5. Close the popup

Now all subsequent requests will automatically include your token!

---

### STEP 4: Create Calculation (Add)

**Endpoint:** `POST /calculations`

1. Find **POST /calculations** (green button)
2. Click **"Try it out"**
3. Fill in the request body:

```json
{
  "type": "addition",
  "inputs": [15, 10]
}
```

4. Click **"Execute"**
5. Expected Response (201 Created):

```json
{
  "type": "addition",
  "inputs": [15.0, 10.0],
  "id": "91d4d0f6-d664-481c-8c96-d8a50bd6d48d",
  "user_id": "e3bd24d0-93ff-4187-9fcc-8233bd7ccae1",
  "result": 25.0,
  "created_at": "2025-11-10T15:17:48.483679",
  "updated_at": "2025-11-10T15:17:48.483679"
}
```

**Supported Calculation Types:**
- `addition` - Add numbers: [15, 10] = 25
- `subtraction` - Subtract numbers: [30, 5] = 25
- `multiplication` - Multiply numbers: [5, 4] = 20
- `division` - Divide numbers: [20, 4] = 5

**cURL Command:**
```bash
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

curl -X POST "http://localhost:8000/calculations" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"type": "addition", "inputs": [15, 10]}'
```

**⚠️ IMPORTANT:** Copy the `id` from response - you'll need it for Read, Update, and Delete!

---

### STEP 5: Browse All Calculations

**Endpoint:** `GET /calculations`

1. Find **GET /calculations** (blue button)
2. Click **"Try it out"**
3. Don't fill anything - just click **"Execute"**
4. Expected Response (200 OK):

```json
[
  {
    "type": "addition",
    "inputs": [15.0, 10.0],
    "id": "91d4d0f6-d664-481c-8c96-d8a50bd6d48d",
    "user_id": "e3bd24d0-93ff-4187-9fcc-8233bd7ccae1",
    "result": 25.0,
    "created_at": "2025-11-10T15:17:48.483679",
    "updated_at": "2025-11-10T15:17:48.483679"
  }
]
```

**cURL Command:**
```bash
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

curl -X GET "http://localhost:8000/calculations" \
  -H "Authorization: Bearer $TOKEN"
```

---

### STEP 6: Read One Calculation

**Endpoint:** `GET /calculations/{calc_id}`

1. Find **GET /calculations/{calc_id}** (blue button)
2. Click **"Try it out"**
3. Fill in the `calc_id` parameter:

```
91d4d0f6-d664-481c-8c96-d8a50bd6d48d
```

4. Click **"Execute"**
5. Expected Response (200 OK):

```json
{
  "type": "addition",
  "inputs": [15.0, 10.0],
  "id": "91d4d0f6-d664-481c-8c96-d8a50bd6d48d",
  "user_id": "e3bd24d0-93ff-4187-9fcc-8233bd7ccae1",
  "result": 25.0,
  "created_at": "2025-11-10T15:17:48.483679",
  "updated_at": "2025-11-10T15:17:48.483679"
}
```

**cURL Command:**
```bash
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
CALC_ID="91d4d0f6-d664-481c-8c96-d8a50bd6d48d"

curl -X GET "http://localhost:8000/calculations/$CALC_ID" \
  -H "Authorization: Bearer $TOKEN"
```

---

### STEP 7: Update Calculation (Edit)

**Endpoint:** `PUT /calculations/{calc_id}`

1. Find **PUT /calculations/{calc_id}** (orange button)
2. Click **"Try it out"**
3. Fill in the `calc_id` parameter:

```
91d4d0f6-d664-481c-8c96-d8a50bd6d48d
```

4. Fill in the request body:

```json
{
  "type": "subtraction",
  "inputs": [30, 5]
}
```

5. Click **"Execute"**
6. Expected Response (200 OK):

```json
{
  "type": "subtraction",
  "inputs": [30.0, 5.0],
  "id": "91d4d0f6-d664-481c-8c96-d8a50bd6d48d",
  "user_id": "e3bd24d0-93ff-4187-9fcc-8233bd7ccae1",
  "result": 25.0,
  "created_at": "2025-11-10T15:17:48.483679",
  "updated_at": "2025-11-10T15:20:00.000000"
}
```

**Note:** `updated_at` timestamp is newer!

**cURL Command:**
```bash
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
CALC_ID="91d4d0f6-d664-481c-8c96-d8a50bd6d48d"

curl -X PUT "http://localhost:8000/calculations/$CALC_ID" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"type": "subtraction", "inputs": [30, 5]}'
```

---

### STEP 8: Delete Calculation

**Endpoint:** `DELETE /calculations/{calc_id}`

1. Find **DELETE /calculations/{calc_id}** (red button)
2. Click **"Try it out"**
3. Fill in the `calc_id` parameter:

```
91d4d0f6-d664-481c-8c96-d8a50bd6d48d
```

4. Click **"Execute"**
5. Expected Response (204 No Content):

Empty response body (calculation successfully deleted)

**cURL Command:**
```bash
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
CALC_ID="91d4d0f6-d664-481c-8c96-d8a50bd6d48d"

curl -X DELETE "http://localhost:8000/calculations/$CALC_ID" \
  -H "Authorization: Bearer $TOKEN"
```

---

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

---

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


## Submission Information
- **GitHub Repository:** https://github.com/Pruthul15/assignment12
- **Docker Hub Image:** https://hub.docker.com/r/pruthul123/assignment12
