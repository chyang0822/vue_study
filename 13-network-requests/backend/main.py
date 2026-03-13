from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

app = FastAPI(title="Network Requests API", version="1.0.0")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据模型
class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    age: int
    created_at: Optional[str] = None

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

# 模拟数据库
users_db: dict = {
    1: {
        "id": 1,
        "name": "张三",
        "email": "zhangsan@example.com",
        "age": 28,
        "created_at": "2024-01-15T10:30:00"
    },
    2: {
        "id": 2,
        "name": "李四",
        "email": "lisi@example.com",
        "age": 32,
        "created_at": "2024-01-16T14:20:00"
    },
    3: {
        "id": 3,
        "name": "王五",
        "email": "wangwu@example.com",
        "age": 25,
        "created_at": "2024-01-17T09:15:00"
    }
}

next_id = 4

# GET - 获取所有用户
@app.get("/users", response_model=List[dict])
async def get_users():
    """获取所有用户列表"""
    return list(users_db.values())

# GET - 获取指定用户
@app.get("/users/{user_id}", response_model=dict)
async def get_user(user_id: int):
    """根据ID获取指定用户"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail=f"用户ID {user_id} 不存在")
    return users_db[user_id]

# POST - 创建用户
@app.post("/users", response_model=dict)
async def create_user(user: User):
    """创建新用户"""
    global next_id
    
    # 验证邮箱唯一性
    for existing_user in users_db.values():
        if existing_user["email"] == user.email:
            raise HTTPException(status_code=400, detail="邮箱已存在")
    
    # 验证年龄
    if user.age < 0 or user.age > 150:
        raise HTTPException(status_code=400, detail="年龄必须在0-150之间")
    
    new_user = {
        "id": next_id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "created_at": datetime.now().isoformat()
    }
    
    users_db[next_id] = new_user
    next_id += 1
    
    return {
        "message": "用户创建成功",
        "data": new_user
    }

# PUT - 完全更新用户
@app.put("/users/{user_id}", response_model=dict)
async def update_user(user_id: int, user: User):
    """完全更新用户信息（所有字段必须提供）"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail=f"用户ID {user_id} 不存在")
    
    # 验证邮箱唯一性（排除当前用户）
    for uid, existing_user in users_db.items():
        if uid != user_id and existing_user["email"] == user.email:
            raise HTTPException(status_code=400, detail="邮箱已存在")
    
    # 验证年龄
    if user.age < 0 or user.age > 150:
        raise HTTPException(status_code=400, detail="年龄必须在0-150之间")
    
    updated_user = {
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "created_at": users_db[user_id].get("created_at", datetime.now().isoformat())
    }
    
    users_db[user_id] = updated_user
    
    return {
        "message": f"用户ID {user_id} 更新成功",
        "data": updated_user
    }

# PATCH - 部分更新用户
@app.patch("/users/{user_id}", response_model=dict)
async def patch_user(user_id: int, user_update: UserUpdate):
    """部分更新用户信息（只更新提供的字段）"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail=f"用户ID {user_id} 不存在")
    
    existing_user = users_db[user_id]
    
    # 验证邮箱唯一性
    if user_update.email:
        for uid, other_user in users_db.items():
            if uid != user_id and other_user["email"] == user_update.email:
                raise HTTPException(status_code=400, detail="邮箱已存在")
    
    # 验证年龄
    if user_update.age is not None:
        if user_update.age < 0 or user_update.age > 150:
            raise HTTPException(status_code=400, detail="年龄必须在0-150之间")
    
    # 只更新提供的字段
    if user_update.name is not None:
        existing_user["name"] = user_update.name
    if user_update.email is not None:
        existing_user["email"] = user_update.email
    if user_update.age is not None:
        existing_user["age"] = user_update.age
    
    return {
        "message": f"用户ID {user_id} 部分更新成功",
        "data": existing_user
    }

# DELETE - 删除用户
@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    """删除指定用户"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail=f"用户ID {user_id} 不存在")
    
    deleted_user = users_db.pop(user_id)
    
    return {
        "message": f"用户ID {user_id} 删除成功",
        "data": deleted_user
    }

# 健康检查
@app.get("/health")
async def health_check():
    """健康检查端点"""
    return {"status": "ok", "message": "API运行正常"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
