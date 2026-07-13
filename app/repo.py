from threading import Lock
from typing import List
from app.models import ItemCreate, Item


class InMemoryRepo:
    def __init__(self):
        self._items: List[Item] = []
        self._lock = Lock()
        self._next_id = 1

    def add(self, item_create: ItemCreate) -> Item:
        with self._lock:
            item = Item(id=self._next_id, name=item_create.name, description=item_create.description)
            self._items.append(item)
            self._next_id += 1
            return item

    def list(self) -> List[Item]:
        with self._lock:
            return list(self._items)
