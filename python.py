from fastapi import FastAPI 
from pydantic import BaseModel,Field 
from uuid import UUID 
app = FastAPI() 
Books = []  
class Book (BaseModel):
     id:UUID  
     title: str= Field(min_length=1)
     author: str= Field(min_length=1,max_length=100) 
     rating: int= Field(gt=-1,lt=101) 
@app.get("/") 
def root():  
    return {"hello":"Nidhish"}      
@app.post("/posts") 
def create_book(book: Book):
     Books.append(book) 
     return book   