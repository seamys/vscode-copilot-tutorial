# Swagger Petstore API Documentation

## Base URL
`http://petstore.swagger.io/v2`

**Version:** 1.0.0

**Description:** This is a sample server Petstore server. You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/). For this sample, you can use the api key `special-key` to test the authorization filters.

**Contact:** apiteam@swagger.io  
**License:** Apache 2.0 - http://www.apache.org/licenses/LICENSE-2.0.html  
**Terms of Service:** http://swagger.io/terms/

---

## Authentication
- Use OAuth2 with petstore_auth:
  - Scopes: `write:pets`, `read:pets`

---

## Endpoints

### 1. Pet Management

#### GET `/pet/findByStatus/MultipleExamples`
Finds Pets by status with multiple examples support.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | array[string] | Yes | Status values that need to be considered for filter. Enum: `available`, `pending`, `sold` |

**Examples:**
- **Available**: `status=available`
- **Sold**: See external example at http://example.com/examples/dog.json

**Response (200 - Successful Operation):**
```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "category": {
        "id": 1,
        "name": "cat"
      },
      "name": "fluffy",
      "photoUrls": [
        "http://example.com/path/to/cat/1.jpg",
        "http://example.com/path/to/cat/2.jpg"
      ],
      "tags": [
        {
          "id": 1,
          "name": "cat"
        }
      ],
      "status": "available"
    },
    {
      "id": 2,
      "category": {
        "id": 2,
        "name": "dog"
      },
      "name": "puppy",
      "photoUrls": [
        "http://example.com/path/to/dog/1.jpg"
      ],
      "tags": [
        {
          "id": 2,
          "name": "dog"
        }
      ],
      "status": "available"
    }
  ]
}
```

**cURL Example:**
```bash
curl -X GET "http://petstore.swagger.io/v2/pet/findByStatus/MultipleExamples?status=available" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json"
```

**Error Response (400 - Invalid Status Value):**
```json
{
  "status": "error",
  "message": "Invalid status value"
}
```

---

#### GET `/pet/findByStatus/singleExample`
Finds Pets by status with single example support.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | array[string] | Yes | Status values that need to be considered for filter. Enum: `available`, `pending`, `sold` |

**Example:**
- **Available**: `status=available`

**Response (200 - Successful Operation):**
```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "category": {
        "id": 1,
        "name": "cat"
      },
      "name": "fluffy",
      "photoUrls": [
        "http://example.com/path/to/cat/1.jpg",
        "http://example.com/path/to/cat/2.jpg"
      ],
      "tags": [
        {
          "id": 1,
          "name": "cat"
        }
      ],
      "status": "available"
    },
    {
      "id": 2,
      "category": {
        "id": 2,
        "name": "dog"
      },
      "name": "puppy",
      "photoUrls": [
        "http://example.com/path/to/dog/1.jpg"
      ],
      "tags": [
        {
          "id": 2,
          "name": "dog"
        }
      ],
      "status": "available"
    }
  ]
}
```

**cURL Example:**
```bash
curl -X GET "http://petstore.swagger.io/v2/pet/findByStatus/singleExample?status=available" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json"
```

**Error Response (400 - Invalid Status Value):**
```json
{
  "status": "error",
  "message": "Invalid status value"
}
```

---

#### POST `/pet`
Add a new pet to the store.

**Request Body Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | No | Pet ID |
| `category` | object | No | Pet category with id and name |
| `name` | string | Yes | Pet name |
| `photoUrls` | array[string] | Yes | Array of photo URLs |
| `tags` | array[object] | No | Array of tags with id and name |
| `status` | string | No | Pet status. Enum: `available`, `pending`, `sold` |

**Request Body Examples:**

**Cat Example (JSON):**
```json
{
  "id": 1,
  "category": {
    "id": 1,
    "name": "cat"
  },
  "name": "fluffy",
  "photoUrls": [
    "http://example.com/path/to/cat/1.jpg",
    "http://example.com/path/to/cat/2.jpg"
  ],
  "tags": [
    {
      "id": 1,
      "name": "cat"
    }
  ],
  "status": "available"
}
```

**Cat Array Example (JSON):**
```json
[
  {
    "id": 1,
    "category": {
      "id": 1,
      "name": "cat"
    },
    "name": "fluffy",
    "photoUrls": [
      "http://example.com/path/to/cat/1.jpg",
      "http://example.com/path/to/cat/2.jpg"
    ],
    "tags": [
      {
        "id": 1,
        "name": "cat"
      }
    ],
    "status": "available"
  }
]
```

**Dog Example (XML):**
```xml
<xml></xml>
```

**cURL Example (JSON):**
```bash
curl -X POST "http://petstore.swagger.io/v2/pet" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "category": {
      "id": 1,
      "name": "cat"
    },
    "name": "fluffy",
    "photoUrls": [
      "http://example.com/path/to/cat/1.jpg",
      "http://example.com/path/to/cat/2.jpg"
    ],
    "tags": [
      {
        "id": 1,
        "name": "cat"
      }
    ],
    "status": "available"
  }'
```

**cURL Example (XML):**
```bash
curl -X POST "http://petstore.swagger.io/v2/pet" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/xml" \
  -d '<xml></xml>'
```

**Error Response (405 - Invalid Input):**
```json
{
  "status": "error",
  "message": "Invalid input"
}
```

---

## Data Models

### Pet
```json
{
  "type": "object",
  "required": ["name", "photoUrls"],
  "properties": {
    "id": {
      "type": "integer",
      "format": "int64"
    },
    "category": {
      "$ref": "#/components/schemas/Category"
    },
    "name": {
      "type": "string",
      "example": "doggie"
    },
    "photoUrls": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "tags": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Tag"
      }
    },
    "status": {
      "type": "string",
      "description": "pet status in the store",
      "enum": ["available", "pending", "sold"]
    }
  }
}
```

### Category
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "format": "int64"
    },
    "name": {
      "type": "string"
    }
  }
}
```

### Tag
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "format": "int64"
    },
    "name": {
      "type": "string"
    }
  }
}
```

---

## Status Codes
- `200 OK` - Successful operation
- `400 Bad Request` - Invalid status value
- `405 Method Not Allowed` - Invalid input

---

## External Documentation
Find out more about Swagger: http://swagger.io

---

## Common Error Example

### Invalid Status Value (400)
```bash
curl -X GET "http://petstore.swagger.io/v2/pet/findByStatus/MultipleExamples?status=invalid" \
  -H "Content-Type: application/json"
```

**Response:**
```json
{
  "status": "error",
  "message": "Invalid status value"
}
```

### Invalid Input (405)
```bash
curl -X POST "http://petstore.swagger.io/v2/pet" \
  -H "Content-Type: application/json" \
  -d '{"invalid": "data"}'
```

**Response:**
```json
{
  "status": "error",
  "message": "Invalid input"
}
```