from typing import Optional
from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title1", "content": "content1", "id": 1}, {"title": "title2", "content": "content2", "id": 2}]

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    # print(new_post.title)
    # print(new_post.content)
    # print(post)
    # print(post.dict())
    post_dict = post.dict()
    post_dict["id"] = randrange(1, 1000)
    my_posts.append(post_dict)
    return {"data": post_dict}


# @app.post("/createposts")
# async def create_posts(payload: dict = Body(...)):
#     print(payload)
#     # return {"message": "successfully created posts"}
#     return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}

@app.get("/posts/{id}")
def get_post(id):
    print(id)
    return {"post_detail": f"Here is post {id}"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

