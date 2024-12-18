# from fastapi import FastAPI 
# from pydantic import BaseModel,Field 
# from uuid import UUID 
# app = FastAPI() 
# Books = []  
# class Book (BaseModel):
#      id:UUID  
#      title: str= Field(min_length=1)
#      author: str= Field(min_length=1,max_length=100) 
#      rating: int= Field(gt=-1,lt=101) 
# @app.get("/") 
# def root():  
#     return {"hello":"Nidhish"}      
# @app.post("/posts") 
# def create_book(book: Book):
#      Books.append(book) 
#      return book   
from openai import AzureOpenAI
import base64
import os
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-08-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
image_path = (
    r"C:\Users\nidhi\OneDrive\Desktop\pexels-chokniti-khongchum-1197604-2280547.jpg"
)
if __name__ == "__main__":
    conversation_log = []
    base64_image = encode_image(image_path)
    conversation_log.append(
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You have to be kind and heplful assistant.You will be given an image and user may ask questions related to image",
                },
            ],
        }
    )  
    conversation_log.append( {
            "role": "user", 
            "content": [
                { 
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ], 
        }) 
    while True:
        user_input = input("YOU: ")
        if user_input.lower() == "quit":
            break
        conversation_log.append({"role": "user", "content": user_input})
        assistant_response = client.chat.completions.create(
            model="gpt-4o", messages=conversation_log
        ) 
        assistant_response = assistant_response.choices[0].message.content
        conversation_log.append({"role": "assistant", "content": assistant_response})
        print("Chatbot:", assistant_response)
