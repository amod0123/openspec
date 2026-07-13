from fastapi import FastAPI, HTTPException, Response
from app.models import ItemCreate, Item, ItemUpdate
from app.repo import InMemoryRepo

app = FastAPI()
repo = InMemoryRepo()


@app.post("/items", status_code=201, response_model=Item)
def create_item(item: ItemCreate):
    return repo.add(item)


@app.get("/items", response_model=list[Item])
def list_items():
    print("Listing items")
    return repo.list()


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate):
    try:
        return repo.update(item_id, item)
    except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    try:
        repo.delete(item_id)
        return Response(status_code=204)
    except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    # Default entrypoint to run the app on port 8001
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)
