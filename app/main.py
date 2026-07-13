from fastapi import FastAPI
from app.models import ItemCreate, Item
from app.repo import InMemoryRepo

app = FastAPI()
repo = InMemoryRepo()


@app.post("/items", status_code=201, response_model=Item)
def create_item(item: ItemCreate):
    return repo.add(item)


@app.get("/items", response_model=list[Item])
def list_items():
    return repo.list()


if __name__ == "__main__":
    # Default entrypoint to run the app on port 8001
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)
