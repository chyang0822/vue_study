# 项目13：网络请求演示

这是一个完整的Vue 3 + FastAPI项目，演示了不同的HTTP请求方法（GET、POST、PUT、PATCH、DELETE）的使用。

## 项目结构

```
13-network-requests/
├── src/                    # Vue前端源代码
│   ├── App.vue            # 主应用组件
│   ├── api.ts             # API服务层
│   ├── main.ts            # 应用入口
│   └── assets/
│       └── main.css       # 全局样式
├── backend/               # FastAPI后端
│   ├── main.py            # 后端应用
│   └── requirements.txt    # Python依赖
├── index.html             # HTML入口
├── package.json           # 前端依赖
├── vite.config.ts         # Vite配置
├── tsconfig.json          # TypeScript配置
└── README.md              # 本文件
```

## 功能特性

### 前端（Vue 3）
- ✅ GET请求：获取所有用户、获取指定用户
- ✅ POST请求：创建新用户
- ✅ PUT请求：完全更新用户信息
- ✅ PATCH请求：部分更新用户信息
- ✅ DELETE请求：删除用户
- ✅ 错误处理和加载状态
- ✅ 响应式设计
- ✅ 现代化UI界面

### 后端（FastAPI）
- ✅ RESTful API设计
- ✅ CORS支持
- ✅ 数据验证（Pydantic）
- ✅ 错误处理
- ✅ 模拟数据库

## 快速开始

### 1. 安装前端依赖

```bash
cd 13-network-requests
npm install
```

### 2. 安装后端依赖

```bash
cd backend
pip install -r requirements.txt
```

### 3. 启动后端服务

```bash
cd backend
python main.py
```

后端将在 `http://localhost:8000` 运行

### 4. 启动前端开发服务器

在新的终端窗口中：

```bash
npm run dev
```

前端将在 `http://localhost:5173` 运行

## API端点

### GET请求
- `GET /users` - 获取所有用户
- `GET /users/{id}` - 获取指定用户

### POST请求
- `POST /users` - 创建新用户
  ```json
  {
    "name": "用户名",
    "email": "邮箱@example.com",
    "age": 25
  }
  ```

### PUT请求
- `PUT /users/{id}` - 完全更新用户（所有字段必须提供）
  ```json
  {
    "name": "新名字",
    "email": "新邮箱@example.com",
    "age": 30
  }
  ```

### PATCH请求
- `PATCH /users/{id}` - 部分更新用户（只更新提供的字段）
  ```json
  {
    "name": "新名字"
  }
  ```

### DELETE请求
- `DELETE /users/{id}` - 删除用户

## 初始数据

后端预置了3个用户：

1. **张三** - zhangsan@example.com, 28岁
2. **李四** - lisi@example.com, 32岁
3. **王五** - wangwu@example.com, 25岁

## 技术栈

### 前端
- Vue 3 (Composition API)
- TypeScript
- Axios (HTTP客户端)
- Vite (构建工具)

### 后端
- FastAPI
- Pydantic (数据验证)
- Uvicorn (ASGI服务器)

## 学习要点

1. **HTTP方法的区别**
   - GET：获取资源
   - POST：创建资源
   - PUT：完全替换资源
   - PATCH：部分更新资源
   - DELETE：删除资源

2. **前端API调用**
   - 使用Axios进行HTTP请求
   - 错误处理和加载状态管理
   - 响应数据处理

3. **后端API设计**
   - RESTful设计原则
   - 数据验证和错误处理
   - CORS配置

4. **Vue 3特性**
   - Composition API
   - 响应式数据
   - 条件渲染和列表渲染
   - 事件处理

## 常见问题

### Q: 前端无法连接到后端？
A: 确保后端运行在 `http://localhost:8000`，并且CORS已正确配置。

### Q: 如何修改后端端口？
A: 在 `backend/main.py` 的最后一行修改 `port=8000`。

### Q: 如何修改前端代理配置？
A: 在 `vite.config.ts` 中修改 `proxy` 配置。

## 扩展建议

1. 添加用户认证（JWT）
2. 添加数据库（SQLite/PostgreSQL）
3. 添加分页功能
4. 添加搜索和过滤
5. 添加单元测试
6. 添加E2E测试

## 许可证

MIT
