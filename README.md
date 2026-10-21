# API-REST Process Documented

This repository was created to reinforce my knowledge, practice, and explore web application structures from the ground up. Every step is documented to serve as a clean guide for understanding how APIs, backends, and databases interconnect from an engineering perspective.

In this project, I utilize **FastAPI** (a modern, high-performance web framework based on Python) and **SQLite** (a lightweight, file-based relational database).

---

## Project Architecture

To implement clean software engineering principles, the system is strictly decoupled into four independent operational layers. This isolation makes it easier to audit network flows and apply security measures:

```text
API_Practice/
│
├── data_base/          # Physical Persistence (Data models and disk connection)
│   └── conections.py
│
├── api/                 # Network Contracts (JSON validation schemas and endpoints)
│   └── route_scheme.py
│
├── backend/             # System Infrastructure (Server startup, middlewares, and CORS)
│   └── main.py
│
└── frontend/            # The Client (Browser interface and HTTP interaction)
    └── index.html
```

### 1. Data Base Layer

This layer is **exclusively responsible for disk persistence**. It serves as an Object-Relational Mapper (ORM) that translates Python source code into physical database records, completely decoupled from networking logic.

### 2. API Layer

This layer defines the **communication contract**. It handles HTTP verbs (`GET`, `POST`), validates the integrity of payloads traveling across the network using Pydantic schemas, and serializes server responses into clean JSON streams.

### 3. Backend Layer

The core engine and infrastructure of the system. It initializes the web server via **Uvicorn**, orchestrates automated database schema generation upon startup, mounts security rules (such as **CORS** configurations), and routes incoming network packets to their respective destinations.

### 4. Frontend Layer

An isolated client-side environment running natively inside the user's browser. It interacts with the backend strictly through HTTP requests using the browser's networking stack (`fetch` API).

---

## Infrastructure & Environment Setup

Since this project is developed on an **Arch Linux** environment under **PEP 668** guidelines, system-wide packet installations via `pip` are blocked to preserve OS stability. A virtual environment (`venv`) must be deployed.

### 1. Initialize and Activate the Environment

If you are using standard shells (Bash/Zsh):

```bash
python -m venv .venv
source .venv/bin/activate
```

If you are running **Fish Shell** (due to syntax handling regarding built-in blocks):

```bash
source .venv/bin/activate.fish
```

### 2. Install Dependencies Locally

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

### 3. Launch the Server

```bash
uvicorn backend.main:app --reload
```

* Note: The module parameter uses Python dot notation (`backend.main`), not file system paths (`backend/main`). The service binds to the loopback interface (`127.0.0.1:8000`)

---

## Networking & Security Footprint (Roadmap)

As a systems engineering student focusing on infrastructure and cybersecurity, this project will be incrementally hardened to document and practice:

- **Input Sanitization:** Utilizing Pydantic type-enforcement to stop malformed data at the perimeter.
- **CORS Policies:** Restricting cross-origin network operations to mitigate unauthorized interface injections.
- **Route Hardening & Session Security:** Future implementation of JWT (JSON Web Tokens) and password hashing to secure endpoints.



## Interface & Verification

To verify that the API contracts, routing, and relational database connections are fully operational, you can audit the endpoints natively via the auto-generated Swagger interactive interface. 


## API Endpoint Reference (v0.1)

| Method | Endpoint           | Payload Type | Description                                                                           |
|:------ |:------------------ |:------------ |:------------------------------------------------------------------------------------- |
| `GET`  | `/api/v1/usuarios` | `None`       | Queries the SQLite ORM and fetches all registered records.                            |
| `POST` | `/api/v1/usuarios` | `JSON`       | Validates data fields (`name`, `email`, `password`) and injects a new user into disk. |

---

## Next Milestones: Moving into Cybersecurity (v0.2 Roadmap)

As this project scales up from a developmental base to a security-hardened infrastructure, the next iterative improvements will implement:

1. **Password Hashing:** Replacing plain-text storage with `Bcrypt` cryptographic salting and hashing.
2. **Access Control:** Hardening routes through stateful **JWT (JSON Web Tokens)** Bearer authentications.
3. **API Logging:** Building an automated audit trail to track network activities, suspicious source IPs, and response statuses.
