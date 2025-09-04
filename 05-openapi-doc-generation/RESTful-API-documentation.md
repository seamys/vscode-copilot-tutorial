# RESTful API Documentation Template

## Base URL
`https://api.example.com/v1`

---

## Authentication
- Use Bearer Token in the `Authorization` header:
  ```
  Authorization: Bearer <token>
  ```

---

## Endpoints

### 1. User Management

#### GET `/users`
Retrieve a list of users.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | integer | No | Page number for pagination (default: 1) |
| `limit` | integer | No | Number of users per page (default: 10) |
| `status` | string | No | Filter by user status (`active`, `inactive`) |

**Response:**
```json
{
  "status": "success",
  "data": {
    "users": [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "status": "active"
      }
    ],
    "pagination": {
      "current_page": 1,
      "total_pages": 5,
      "total_users": 50
    }
  }
}
```

**cURL Example:**
```bash
curl -X GET "https://api.example.com/v1/users?page=1&limit=10" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json"
```

---

#### POST `/users`
Create a new user.

**Request Body Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | User's full name |
| `email` | string | Yes | Valid email address |
| `password` | string | Yes | Password (min 8 characters) |

**Request Body:**
```json
{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com",
    "created_at": "2023-01-21T09:15:00Z"
  }
}
```

**cURL Example:**
```bash
curl -X POST "https://api.example.com/v1/users" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "email": "jane@example.com",
    "password": "securepassword123"
  }'
```

---

### 2. Authentication

#### POST `/auth/login`
Authenticate a user and return a token.

**Request Body Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `email` | string | Yes | User's email address |
| `password` | string | Yes | User's password |

**Request Body:**
```json
{
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com"
    }
  }
}
```

**cURL Example:**
```bash
curl -X POST "https://api.example.com/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "securepassword123"
  }'
```

---

## Response Format

**Success:**
```json
{
  "status": "success",
  "data": { ... }
}
```

**Error:**
```json
{
  "status": "error",
  "message": "Error details",
  "errors": {
    "field_name": ["Specific error message"]
  }
}
```

---

## Status Codes
- `200 OK` - Successful request
- `201 Created` - Resource created successfully
- `400 Bad Request` - Invalid input data
- `401 Unauthorized` - Authentication failed
- `404 Not Found` - Resource not found
- `422 Unprocessable Entity` - Validation errors
- `500 Internal Server Error` - Server error

---

## Common Error Example

### Validation Error (422)
```bash
curl -X POST "https://api.example.com/v1/users" \
  -H "Content-Type: application/json" \
  -d '{"email": "invalid-email"}'
```

**Response:**
```json
{
  "status": "error",
  "message": "Validation failed",
  "errors": {
    "name": ["The name field is required."],
    "email": ["Please enter a valid email address."],
    "password": ["Password must be at least 8 characters long."]
  }
}
```

