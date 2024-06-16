from fastapi.testclient import TestClient
from main import app
import requests
from unittest.mock import patch

client = TestClient(app)

def test_read_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
def test_get_posts():
    with patch('requests.get') as mocked_get_posts:
        mocked_get_posts.return_value.status_code = 200
        mocked_get_posts.return_value.json.return_value = [
            {"id": 1, "title": "Post 1", "body": "Content 1", "userId": 1},
            {"id": 2, "title": "Post 2", "body": "Content 2", "userId": 2}
        ]
        response = client.get("/posts")
        posts = response.json()
        
        print(f"Response JSON: {posts}")
        assert response.status_code == 200
        assert len(posts) == 2
        assert isinstance(posts, list)

def test_get_post():
    with patch('requests.get') as mocked_get_post:
        mocked_get_post.return_value.status_code = 200
        mocked_get_post.return_value.json.return_value = [
            {"id": 1, "title": "Post 1", "body": "Content 1", "userId": 1},
        ]
        response = client.get("/posts/1")
        post = response.json()
        
        print(f"Response JSON: {post}")
        assert response.status_code == 200
        assert len(post) == 1
        assert isinstance(post, object)
        
        mocked_get_post.return_value.status_code = 404
        response = client.get("/posts/99")
        assert response.status_code == 404
        assert response.json() == {"detail":"Post not found"}
        
def test_create_post():
    with patch('requests.post') as mocked_post:
        post = {"title": "Post 355", "body": "Content 355", "userId": 355}
        mocked_post.return_value.status_code = 201
        mocked_post.return_value.json.return_value = {
            "id": 101,
            "title": "Post 355",
            "body": "Content 355",
            "userId": 355
        }
        
        response = client.post("/posts", json=post)
        created_post = response.json()
        print(f"Response JSON: {created_post}")

        assert response.status_code == 201
        assert created_post["id"] == 101
        
        mocked_post.return_value.status_code = 404
        response = client.post("/posts", json=post)
        
        assert response.status_code == 404
        assert response.json() == {"detail":"Failed to create post"}