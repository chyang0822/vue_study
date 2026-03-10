import axios, { AxiosInstance, AxiosError } from 'axios'

// 创建 axios 实例
const apiClient: AxiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// 请求拦截器
apiClient.interceptors.request.use(
  (config) => {
    // 可以在这里添加 token 等
    console.log('发送请求:', config.method?.toUpperCase(), config.url)
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 响应拦截器
apiClient.interceptors.response.use(
  (response) => {
    console.log('收到响应:', response.status, response.config.url)
    return response
  },
  (error: AxiosError) => {
    console.error('请求错误:', error.message)
    return Promise.reject(error)
  }
)

// 用户接口类型
export interface User {
  id?: number
  name: string
  email: string
  age?: number
  created_at?: string
}

export interface UserUpdate {
  name?: string
  email?: string
  age?: number
}

// 文章接口类型
export interface Post {
  id?: number
  title: string
  content: string
  author_id: number
  created_at?: string
}

// ==================== 用户 API ====================

// GET - 获取所有用户
export const getUsers = (skip = 0, limit = 10) => {
  return apiClient.get<User[]>('/users', {
    params: { skip, limit }
  })
}

// GET - 根据 ID 获取用户
export const getUserById = (id: number) => {
  return apiClient.get<User>(`/users/${id}`)
}

// GET - 搜索用户
export const searchUsers = (name?: string, email?: string) => {
  return apiClient.get<User[]>('/users/search/', {
    params: { name, email }
  })
}

// POST - 创建用户
export const createUser = (user: User) => {
  return apiClient.post<User>('/users', user)
}

// PUT - 完整更新用户
export const updateUser = (id: number, user: User) => {
  return apiClient.put<User>(`/users/${id}`, user)
}

// PATCH - 部分更新用户
export const partialUpdateUser = (id: number, user: UserUpdate) => {
  return apiClient.patch<User>(`/users/${id}`, user)
}

// DELETE - 删除用户
export const deleteUser = (id: number) => {
  return apiClient.delete(`/users/${id}`)
}

// ==================== 文章 API ====================

// GET - 获取所有文章
export const getPosts = () => {
  return apiClient.get<Post[]>('/posts')
}

// GET - 根据 ID 获取文章
export const getPostById = (id: number) => {
  return apiClient.get<Post>(`/posts/${id}`)
}

// POST - 创建文章
export const createPost = (post: Post) => {
  return apiClient.post<Post>('/posts', post)
}

// DELETE - 删除文章
export const deletePost = (id: number) => {
  return apiClient.delete(`/posts/${id}`)
}

// ==================== 测试 API ====================

// 慢速请求
export const getSlowResponse = () => {
  return apiClient.get('/slow')
}

// 错误请求
export const getErrorResponse = () => {
  return apiClient.get('/error')
}

export default apiClient
