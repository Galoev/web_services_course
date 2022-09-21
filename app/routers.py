from fastapi import APIRouter
from app import contracts

router = APIRouter()

@router.get("/")
def index():
    return {"message": "hello world"}

@router.get("/path/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@router.get("/query/")
async def read_name(name: str):
    return {"name": name}

@router.get("/items/")
async def create_item(item: contracts.Item):
    item_dict = item.dict()
    return item_dict