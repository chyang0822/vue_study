import axios from 'axios'

const API_BASE_URL = '/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 5000
})

export const apiService = {
  // GET 请求
  getUsers() {
    return api.get('/users')
  },

  getUserById(id: number) {
    return api.get(`/users/${id}`)
  },

  // POST 请求
  createUser(data: { name: string; email: string; age: number }) {
    return api.post('/users', data)
  },

  // PUT 请求
  updateUser(id: number, data: { name: string; email: string; age: number }) {
    return api.put(`/users/${id}`, data)
  },

  // DELETE 请求
  deleteUser(id: number) {
    return api.delete(`/users/${id}`)
  },

  // PATCH 请求
  patchUser(id: number, data: Partial<{ name: string; email: string; age: number }>) {
    return api.patch(`/users/${id}`, data)
  }
}
