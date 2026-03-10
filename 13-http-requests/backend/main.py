from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Vue 3 HTTP Requests API", version="1.0.0")

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue 开发服务器地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据模型
class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    age: Optional[int] = None
    created_at: Optional[str] = None

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

class Post(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    author_id: int
    created_at: Optional[str] = None

# 模拟数据库
users_db = [
    {"id": 1, "name": "张三", "email": "zhangsan@example.com", "age": 25, "created_at": "2024-01-01T10:00:00"},
    {"id": 2, "name": "李四", "email": "lisi@example.com", "age": 30, "created_at": "2024-01-02T10:00:00"},
    {"id": 3, "name": "王五", "email": "wangwu@example.com", "age": 28, "created_at": "2024-01-03T10:00:00"},
]

posts_db = [
    {"id": 1, "title": "Vue 3 入门", "content": "Vue 3 是一个渐进式框架...", "author_id": 1, "created_at": "2024-01-01T10:00:00"},
    {"id": 2, "title": "FastAPI 教程", "content": "FastAPI 是一个现代化的 Python Web 框架...", "author_id": 2, "created_at": "2024-01-02T10:00:00"},
]

# 根路由
@app.get("/")
def read_root():
    return {
        "message": "Welcome to Vue 3 HTTP Requests API",
        "docs": "/docs",
        "version": "1.0.0"
    }

# ==================== 用户相关接口 ====================

# GET - 获取所有用户
@app.get("/api/users", response_model=List[User])
def get_users(skip: int = 0, limit: int = 10):
    """获取用户列表（支持分页）"""
    return users_db[skip : skip + limit]

# GET - 根据 ID 获取用户
@app.get("/api/users/{user_id}", response_model=User)
def get_user(user_id: int):
    """根据 ID 获取单个用户"""
    user = next((u for u in users_db if u["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user

# GET - 搜索用户
@app.get("/api/users/search/", response_model=List[User])
def search_users(name: Optional[str] = None, email: Optional[str] = None):
    """搜索用户（支持按名称或邮箱搜索）"""
    results = users_db
    if name:
        results = [u for u in results if name.lower() in u["name"].lower()]
    if email:
        results = [u for u in results if email.lower() in u["email"].lower()]
    return results

# POST - 创建用户
@app.post("/api/users", response_model=User, status_code=201)
def create_user(user: User):
    """创建新用户"""
    # 生成新 ID
    new_id = max([u["id"] for u in users_db]) + 1 if users_db else 1
    
    # 创建用户对象
    new_user = {
        "id": new_id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "created_at": datetime.now().isoformat()
    }
    
    # 检查邮箱是否已存在
    if any(u["email"] == user.email for u in users_db):
        raise HTTPException(status_code=400, detail="邮箱已存在")
    
    users_db.append(new_user)
    return new_user

# PUT - 完整更新用户
@app.put("/api/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    """完整更新用户信息"""
    user_index = next((i for i, u in enumerate(users_db) if u["id"] == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="用户不存在")
    
    updated_user = {
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "created_at": users_db[user_index]["created_at"]
    }
    
    users_db[user_index] = updated_user
    return updated_user

# PATCH - 部分更新用户
@app.patch("/api/users/{user_id}", response_model=User)
def partial_update_user(user_id: int, user: UserUpdate):
    """部分更新用户信息"""
    user_index = next((i for i, u in enumerate(users_db) if u["id"] == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="用户不存在")
    
    current_user = users_db[user_index]
    
    # 只更新提供的字段
    if user.name is not None:
        current_user["name"] = user.name
    if user.email is not None:
        current_user["email"] = user.email
    if user.age is not None:
        current_user["age"] = user.age
    
    return current_user

# DELETE - 删除用户
@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    """删除用户"""
    user_index = next((i for i, u in enumerate(users_db) if u["id"] == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="用户不存在")
    
    deleted_user = users_db.pop(user_index)
    return {"message": "用户已删除", "user": deleted_user}

# ==================== 文章相关接口 ====================

# GET - 获取所有文章
@app.get("/api/posts", response_model=List[Post])
def get_posts():
    """获取所有文章"""
    return posts_db

# GET - 根据 ID 获取文章
@app.get("/api/posts/{post_id}", response_model=Post)
def get_post(post_id: int):
    """根据 ID 获取单个文章"""
    post = next((p for p in posts_db if p["id"] == post_id), None)
    if post is None:
        raise HTTPException(status_code=404, detail="文章不存在")
    return post

# POST - 创建文章
@app.post("/api/posts", response_model=Post, status_code=201)
def create_post(post: Post):
    """创建新文章"""
    new_id = max([p["id"] for p in posts_db]) + 1 if posts_db else 1
    
    new_post = {
        "id": new_id,
        "title": post.title,
        "content": post.content,
        "author_id": post.author_id,
        "created_at": datetime.now().isoformat()
    }
    
    posts_db.append(new_post)
    return new_post

# DELETE - 删除文章
@app.delete("/api/posts/{post_id}")
def delete_post(post_id: int):
    """删除文章"""
    post_index = next((i for i, p in enumerate(posts_db) if p["id"] == post_id), None)
    if post_index is None:
        raise HTTPException(status_code=404, detail="文章不存在")
    
    deleted_post = posts_db.pop(post_index)
    return {"message": "文章已删除", "post": deleted_post}

# ==================== 测试接口 ====================

# 模拟延迟响应
@app.get("/api/slow")
async def slow_endpoint():
    """模拟慢速响应（用于测试 loading 状态）"""
    import asyncio
    await asyncio.sleep(2)
    return {"message": "这是一个延迟 2 秒的响应"}

# 模拟错误响应
@app.get("/api/error")
def error_endpoint():
    """模拟错误响应（用于测试错误处理）"""
    raise HTTPException(status_code=500, detail="这是一个模拟的服务器错误")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
