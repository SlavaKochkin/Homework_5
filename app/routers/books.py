from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()


class Book(BaseModel):
    id: int | None = None
    title: str
    author: str
    year: int


books_db: List[Book] = [
    Book(id=1, title="1984", author="George Orwell", year=1949),
    Book(id=2, title="Всадник без головы", author="Томас Майн Рид", year=1865)
]
next_id = 3


@router.get("/", response_model=List[Book])
async def get_books():
    return books_db


@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")


@router.post("/", response_model=Book)
async def create_book(book: Book):
    global next_id
    book.id = next_id
    next_id += 1
    books_db.append(book)
    return book


@router.put("/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
    for i, b in enumerate(books_db):
        if b.id == book_id:
            book.id = book_id
            books_db[i] = book
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")


@router.delete("/{book_id}")
async def delete_book(book_id: int):
    for i, book in enumerate(books_db):
        if book.id == book_id:
            del books_db[i]
            return {"message": "Книга удалена"}
    raise HTTPException(status_code=404, detail="Книга не найдена")
