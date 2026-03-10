# HTTP 请求快速启动指南

## 🚀 快速开始

### 1. 安装前端依赖
```bash
yarn install
```

### 2. 安装后端依赖
```bash
cd backend
pip install -r requirements.txt
```

### 3. 启动后端（终端1）
```bash
cd backend
uvicorn main:app --reload
```

后端运行在: http://localhost:8000

### 4. 启动前端（终端2）
```bash
yarn dev
```

前端运行在: http://localhost:5173

## 📚 API 文档

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🎯 学习内容

### 请求类型
- ✅ GET - 获取数据
- ✅ POST - 创建数据
- ✅ PUT - 完整更新
- ✅ PATCH - 部分更新
- ✅ DELETE - 删除数据

### 参数类型
- ✅ Query 参数 - URL 查询参数
- ✅ Path 参数 - URL 路径参数
- ✅ Body 参数 - 请求体参数

### 高级功能
- ✅ 请求拦截器
- ✅ 响应拦截器
- ✅ 错误处理
- ✅ Loading 状态
- ✅ 超时设置

## 💡 使用示例

### GET 请求
```typescript
// 获取所有用户
const response = await api.getUsers()

// 获取单个用户
const response = await api.getUserById(1)

// 带查询参数
const response = await api.searchUsers('张三', 'zhangsan@example.com')
```

### POST 请求
```typescript
const newUser = {
  name: '张三',
  email: 'zhangsan@example.com',
  age: 25
}
const response = await api.createUser(newUser)
```

### PUT 请求
```typescript
const updatedUser = {
  name: '张三',
  email: 'zhangsan@example.com',
  age: 26
}
const response = await api.updateUser(1, updatedUser)
```

### PATCH 请求
```typescript
const partialUpdate = {
  age: 26
}
const response = await api.partialUpdateUser(1, partialUpdate)
```

### DELETE 请求
```typescript
await api.deleteUser(1)
```

## 🔧 故障排除

### 后端无法启动
- 检查 Python 版本（需要 3.8+）
- 确保已安装所有依赖
- 检查 8000 端口是否被占用

### 前端请求失败
- 确保后端已启动
- 检查 CORS 配置
- 查看浏览器控制台错误信息

### 跨域问题
- 后端已配置 CORS
- Vite 已配置代理
- 确保使用正确的 API 地址

## 📖 相关资源

- [Axios 文档](https://axios-http.com/zh/)
- [FastAPI 文档](https://fastapi.tiangolo.com/zh/)
- [Vue 3 文档](https://cn.vuejs.org/)
