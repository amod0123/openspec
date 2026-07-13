# Simple FastAPI Items Service

Run the API locally (default port 8001):

```bash
pip install -r requirements.txt
# run via python module entrypoint (defaults to port 8001)
python -m app.main
# or with uvicorn explicitly:
uvicorn app.main:app --reload --port 8001
```

Endpoints:
- `POST /items` — create item (JSON body with `name` and optional `description`)
- `GET /items` — list all items

Run tests:

```bash
pytest -q
```
