# 13 - HTTP 请求

Vue 3 + FastAPI 网络请求完整示例

## 学习内容

1. **Axios 基础** - HTTP 客户端库
2. **GET 请求** - 获取数据
3. **POST 请求** - 创建数据
4. **PUT/PATCH 请求** - 更新数据
5. **DELETE 请求** - 删除数据
6. **请求参数** - Query、Path、Body 参数
7. **错误处理** - 异常捕获和处理
8. **Loading 状态** - 加载状态管理
9. **拦截器** - 请求/响应拦截
10. **实战应用** - 完整的 CRUD 示例

## 项目结构

```
13-http-requests/
├── backend/              # FastAPI 后端
│   ├── main.py          # 后端主文件
│   └── requirements.txt # Python 依赖
├── src/                 # Vue 前端
│   ├── api/            # API 接口封装
│   ├── components/     # 组件
│   └── App.vue         # 主应用
└── README.md
```

## 快速开始

### 1. 安装前端依赖

```sh
yarn install
```

### 2. 安装后端依赖

```sh
cd backend
pip install -r requirements.txt
```

### 3. 启动后端服务

```sh
# 在 backend 目录下
uvicorn main:app --reload

# 或者在项目根目录
yarn backend
```

后端将运行在 http://localhost:8000

### 4. 启动前端服务

```sh
# 在项目根目录
yarn dev
```

前端将运行在 http://localhost:5173

## API 文档

后端启动后，访问以下地址查看 API 文档：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 技术栈

### 前端
- Vue 3.5.29
- Axios 1.6.7
- TypeScript 5.9.3
- Vite 7.3.1

### 后端
- FastAPI
- Python 3.8+
- Uvicorn

## 学习建议

1. 先启动后端服务
2. 访问 API 文档了解接口
3. 运行前端项目
4. 查看代码和注释
5. 尝试修改请求参数

## 参考文档

- [Axios 文档](https://axios-http.com/zh/)
- [FastAPI 文档](https://fastapi.tiangolo.com/zh/)
- [Vue 3 文档](https://cn.vuejs.org/)
