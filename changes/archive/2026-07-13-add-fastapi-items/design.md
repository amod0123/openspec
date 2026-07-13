# Design: Simple FastAPI Items Service

## Overview

The service is a small FastAPI application that exposes two primary endpoints:

- `POST /items` — create an item
- `GET /items` — list all items

We'll start with an in-memory repository and a Pydantic model for validation.

## Project Layout

- `app/`
  - `main.py` — FastAPI app and route registration
  - `models.py` — Pydantic models (`Item`, `ItemCreate`)
  - `repo.py` — in-memory repository abstraction (thread-safe)
  - `schemas/` — optional place for more schemas if needed
- `tests/` — pytest tests for endpoints and repo
- `requirements.txt` / `pyproject.toml`

## Data Model

- `ItemCreate` (input): `name: str`, `description: Optional[str]`
- `Item` (output): `id: int`, `name: str`, `description: Optional[str]`

IDs will be generated in-memory (simple increment) until persistent storage is added.

## Repository

- Implement a small `InMemoryRepo` class that holds a list and a `threading.Lock` to protect mutations.
- Provide `add(item_create)` -> `Item` and `list()` -> `List[Item]`.

## Endpoints

- POST /items
  - Validate body as `ItemCreate`.
  - Call `repo.add(...)` and return `201 Created` with the created item.

- GET /items
  - Return `200 OK` with list from `repo.list()`.

## Error handling & validation

- Rely on FastAPI/Pydantic validation for request bodies.
- Return appropriate HTTP statuses for malformed inputs.

## Observability & Dev ergonomics

- FastAPI provides interactive docs at `/docs`.
- Add simple logging to stdout for requests and errors.

## Future considerations

- Replace `InMemoryRepo` with a DB-backed repo (SQLite/Postgres) behind the same interface.
- Add authentication and rate-limiting if exposed publicly.
