# Tasks: Implementation Steps


1. [x] Create project skeleton
   - Add `app/` folder and `tests/` folder
   - Add `requirements.txt` with `fastapi`, `uvicorn[standard]`, `pytest`

2. [x] Implement models
   - `app/models.py`: `ItemCreate`, `Item` Pydantic models

3. [x] Implement repository
   - `app/repo.py`: `InMemoryRepo` with `add()` and `list()` methods, thread-safe

4. [x] Implement API
   - `app/main.py`: create FastAPI app, wire endpoints `POST /items` and `GET /items`

5. [x] Add tests
   - `tests/test_api.py`: test adding items and retrieving them (use `httpx` or FastAPI's TestClient)

6. [x] Add README and run instructions
   - How to start: `uvicorn app.main:app --reload`

7. Optional: Dockerfile for containerizing the service

8. Optional: Add persistence (SQLite) and migrations
