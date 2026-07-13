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

    def update(self, item_id: int, item_update) -> Item:
        """Update an existing item. `item_update` may have optional attributes."""
        with self._lock:
            for idx, it in enumerate(self._items):
                if it.id == item_id:
                    # apply provided fields
                    name = getattr(item_update, "name", None)
                    if name is not None:
                        it.name = name
                    if hasattr(item_update, "description"):
                        it.description = item_update.description
                    self._items[idx] = it
                    return it
            raise KeyError("item not found")
