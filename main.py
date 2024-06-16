from fastapi import FastAPI, HttpException
import requests

app = FastAPI()
url = "https://jsonplaceholder.typicode.com/posts"

@app.get("/status")
def read_status():
    return {"status":"ok"}

@app.get("/posts")
def get_posts():
    response = requests.get(url)
    return response.json

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    response = requests.get(url, post_id)
    if response.status_code == 200:
        return response.json
    else:
        raise HttpException(status_code=404, detail="Post not found")

@app.post("posts/")    
def create_post(posts: dict):
    response = requests.post(url, posts)
    if response.status_code == 201:
        return response.json
    else:
        raise HttpException(status_code=404, detail="can not create post")
    

