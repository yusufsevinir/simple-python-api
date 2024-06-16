from fastapi import FastAPI, HTTPException, status
import requests

app = FastAPI()
url = "https://jsonplaceholder.typicode.com/posts"

@app.get("/status")
def read_status():
    return {"status":"ok"}

@app.get("/posts")
def get_posts():
    response = requests.get(url)
    return response.json()

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    response = requests.get(url, post_id)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail="Post not found")

@app.post("/posts", status_code= status.HTTP_201_CREATED)
def create_post(post: dict):
    response = requests.post(url, json=post)
    if response.status_code == 201:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to create post")
