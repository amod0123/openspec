# Proposal: Simple FastAPI Items Service

## What

Create a small HTTP API using FastAPI that allows clients to:

- Add an item (POST /items)
- Retrieve all items (GET /items)

Each item will have at minimum a `name` and an optional `description`.

## Why

- Provide a minimal, documented service for demos, POCs, or local automation.
- Keep the surface area small so we can iterate on persistence, validation, and auth later.

## Scope

- Implement an in-memory repository for items (no DB required for MVP).
- Input validation using Pydantic models.
- OpenAPI docs available via FastAPI (`/docs`).
- Basic tests covering endpoint behavior.

## Non-goals (MVP)

- No authentication or authorization.
- No production-grade persistence (later tasks can add DB support).

## Dependencies

- `fastapi`
- `uvicorn[standard]` (for running)
- `pydantic` (included via FastAPI)
- `pytest` (for tests)

## Success Criteria

- POST /items accepts a JSON item and returns 201 with the created item (including an `id`).
- GET /items returns an array of all items added so far.
- Tests pass locally.
