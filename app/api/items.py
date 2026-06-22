from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field


router = APIRouter()


class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=255)


class Item(ItemCreate):
    id: int


items: dict[int, Item] = {
    1: Item(id=1, name="First item", description="A sample REST resource"),
}
next_item_id = 2


@router.get("/", response_model=list[Item])
async def list_items():
    return list(items.values())


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(payload: ItemCreate):
    global next_item_id

    item = Item(id=next_item_id, **payload.model_dump())
    items[item.id] = item
    next_item_id += 1

    return item


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = items.get(item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )

    return item


@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, payload: ItemCreate):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )

    item = Item(id=item_id, **payload.model_dump())
    items[item_id] = item

    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )

    del items[item_id]
