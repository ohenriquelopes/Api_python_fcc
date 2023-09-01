from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    # published: bool

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/posts")
async def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
async def create_posts(payload: dict = Body(...)):
    print(payload)
    # return {"message": "successfully created posts"}
    return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

