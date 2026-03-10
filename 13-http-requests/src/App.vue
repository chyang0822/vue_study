<script setup lang="ts">
import { ref } from 'vue'
import * as api from './api'
import type { User, Post } from './api'

// ==================== 状态管理 ====================
const users = ref<User[]>([])
const posts = ref<Post[]>([])
const selectedUser = ref<User | null>(null)
const loading = ref(false)
const error = ref('')

// 表单数据
const newUser = ref<User>({
  name: '',
  email: '',
  age: undefined
})

const updateUserData = ref<User>({
  name: '',
  email: '',
  age: undefined
})

const newPost = ref<Post>({
  title: '',
  content: '',
  author_id: 1
})

// 搜索参数
const searchName = ref('')
const searchEmail = ref('')

// ==================== GET 请求 ====================

// 获取所有用户
async function fetchUsers() {
  loading.value = true
  error.value = ''
  try {
    const response = await api.getUsers()
    users.value = response.data
    console.log('获取用户成功:', users.value)
  } catch (err: any) {
    error.value = err.message || '获取用户失败'
    console.error('获取用户失败:', err)
  } finally {
    loading.value = false
  }
}

// 根据 ID 获取用户
async function fetchUserById(id: number) {
  loading.value = true
  error.value = ''
  try {
    const response = await api.getUserById(id)
    selectedUser.value = response.data
    console.log('获取用户详情:', selectedUser.value)
  } catch (err: any) {
    error.value = err.message || '获取用户详情失败'
    console.error('获取用户详情失败:', err)
  } finally {
    loading.value = false
  }
}

// 搜索用户
async function searchUsersHandler() {
  loading.value = true
  error.value = ''
  try {
    const response = await api.searchUsers(
      searchName.value || undefined,
      searchEmail.value || undefined
    )
    users.value = response.data
    console.log('搜索结果:', users.value)
  } catch (err: any) {
    error.value = err.message || '搜索失败'
    console.error('搜索失败:', err)
  } finally {
    loading.value = false
  }
}

// ==================== POST 请求 ====================

// 创建用户
async function createUser() {
  if (!newUser.value.name || !newUser.value.email) {
    error.value = '请填写必填字段'
    return
  }

  loading.value = true
  error.value = ''
  try {
    const response = await api.createUser(newUser.value)
    console.log('创建用户成功:', response.data)
    
    // 重置表单
    newUser.value = { name: '', email: '', age: undefined }
    
    // 刷新列表
    await fetchUsers()
  } catch (err: any) {
    error.value = err.response?.data?.detail || '创建用户失败'
    console.error('创建用户失败:', err)
  } finally {
    loading.value = false
  }
}

// ==================== PUT 请求 ====================

// 完整更新用户
async function updateUser(id: number) {
  if (!updateUserData.value.name || !updateUserData.value.email) {
    error.value = '请填写必填字段'
    return
  }

  loading.value = true
  error.value = ''
  try {
    const response = await api.updateUser(id, updateUserData.value)
    console.log('更新用户成功:', response.data)
    await fetchUsers()
  } catch (err: any) {
    error.value = err.response?.data?.detail || '更新用户失败'
    console.error('更新用户失败:', err)
  } finally {
    loading.value = false
  }
}

// ==================== PATCH 请求 ====================

// 部分更新用户
async function partialUpdateUser(id: number, field: 'name' | 'email' | 'age', value: any) {
  loading.value = true
  error.value = ''
  try {
    const updateData = { [field]: value }
    const response = await api.partialUpdateUser(id, updateData)
    console.log('部分更新成功:', response.data)
    await fetchUsers()
  } catch (err: any) {
    error.value = err.response?.data?.detail || '更新失败'
    console.error('更新失败:', err)
  } finally {
    loading.value = false
  }
}

// ==================== DELETE 请求 ====================

// 删除用户
async function deleteUser(id: number) {
  if (!confirm('确定要删除这个用户吗？')) return

  loading.value = true
  error.value = ''
  try {
    await api.deleteUser(id)
    console.log('删除用户成功')
    await fetchUsers()
  } catch (err: any) {
    error.value = err.response?.data?.detail || '删除用户失败'
    console.error('删除用户失败:', err)
  } finally {
    loading.value = false
  }
}

// ==================== 文章相关 ====================

// 获取所有文章
async function fetchPosts() {
  loading.value = true
  error.value = ''
  try {
    const response = await api.getPosts()
    posts.value = response.data
    console.log('获取文章成功:', posts.value)
  } catch (err: any) {
    error.value = err.message || '获取文章失败'
    console.error('获取文章失败:', err)
  } finally {
    loading.value = false
  }
}

// 创建文章
async function createPost() {
  if (!newPost.value.title || !newPost.value.content) {
    error.value = '请填写标题和内容'
    return
  }

  loading.value = true
  error.value = ''
  try {
    const response = await api.createPost(newPost.value)
    console.log('创建文章成功:', response.data)
    
    // 重置表单
    newPost.value = { title: '', content: '', author_id: 1 }
    
    // 刷新列表
    await fetchPosts()
  } catch (err: any) {
    error.value = err.response?.data?.detail || '创建文章失败'
    console.error('创建文章失败:', err)
  } finally {
    loading.value = false
  }
}

// 删除文章
async function deletePost(id: number) {
  if (!confirm('确定要删除这篇文章吗？')) return

  loading.value = true
  error.value = ''
  try {
    await api.deletePost(id)
    console.log('删除文章成功')
    await fetchPosts()
  } catch (err: any) {
    error.value = err.response?.data?.detail || '删除文章失败'
    console.error('删除文章失败:', err)
  } finally {
    loading.value = false
  }
}

// ==================== 测试接口 ====================

// 测试慢速请求
async function testSlowRequest() {
  loading.value = true
  error.value = ''
  try {
    const response = await api.getSlowResponse()
    console.log('慢速请求响应:', response.data)
    alert(response.data.message)
  } catch (err: any) {
    error.value = err.message || '请求失败'
    console.error('请求失败:', err)
  } finally {
    loading.value = false
  }
}

// 测试错误请求
async function testErrorRequest() {
  loading.value = true
  error.value = ''
  try {
    await api.getErrorResponse()
  } catch (err: any) {
    error.value = err.response?.data?.detail || '服务器错误'
    console.error('错误请求:', err)
  } finally {
    loading.value = false
  }
}

// 页面加载时获取数据
fetchUsers()
fetchPosts()
</script>

<template>
  <div class="container">
    <h1>13 - HTTP 请求示例</h1>

    <!-- Loading 和 Error 提示 -->
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>加载中...</p>
    </div>

    <div v-if="error" class="error-message">
      ❌ {{ error }}
      <button @click="error = ''" class="btn-close">×</button>
    </div>

    <!-- GET 请求示例 -->
    <section class="demo-section">
      <h2>1. GET 请求 - 获取数据</h2>
      
      <div class="example">
        <h3>获取所有用户</h3>
        <button @click="fetchUsers" :disabled="loading">刷新用户列表</button>
        
        <div class="user-list">
          <div v-for="user in users" :key="user.id" class="user-card">
            <h4>{{ user.name }}</h4>
            <p>📧 {{ user.email }}</p>
            <p v-if="user.age">🎂 {{ user.age }} 岁</p>
            <div class="button-group">
              <button @click="fetchUserById(user.id!)" class="btn-small">查看详情</button>
              <button @click="deleteUser(user.id!)" class="btn-small btn-danger">删除</button>
            </div>
          </div>
        </div>
      </div>

      <div class="example">
        <h3>搜索用户（带查询参数）</h3>
        <div class="search-form">
          <input v-model="searchName" placeholder="按名称搜索">
          <input v-model="searchEmail" placeholder="按邮箱搜索">
          <button @click="searchUsersHandler">搜索</button>
          <button @click="searchName = ''; searchEmail = ''; fetchUsers()">重置</button>
        </div>
      </div>

      <div v-if="selectedUser" class="example">
        <h3>用户详情</h3>
        <div class="user-detail">
          <p><strong>ID:</strong> {{ selectedUser.id }}</p>
          <p><strong>姓名:</strong> {{ selectedUser.name }}</p>
          <p><strong>邮箱:</strong> {{ selectedUser.email }}</p>
          <p><strong>年龄:</strong> {{ selectedUser.age || '未设置' }}</p>
          <p><strong>创建时间:</strong> {{ selectedUser.created_at }}</p>
        </div>
      </div>
    </section>

    <!-- POST 请求示例 -->
    <section class="demo-section">
      <h2>2. POST 请求 - 创建数据</h2>
      
      <div class="example">
        <h3>创建新用户</h3>
        <form @submit.prevent="createUser" class="form">
          <div class="form-group">
            <label>姓名 *</label>
            <input v-model="newUser.name" required>
          </div>
          <div class="form-group">
            <label>邮箱 *</label>
            <input v-model="newUser.email" type="email" required>
          </div>
          <div class="form-group">
            <label>年龄</label>
            <input v-model.number="newUser.age" type="number">
          </div>
          <button type="submit" :disabled="loading">创建用户</button>
        </form>
      </div>
    </section>

    <!-- PUT/PATCH 请求示例 -->
    <section class="demo-section">
      <h2>3. PUT/PATCH 请求 - 更新数据</h2>
      
      <div class="example">
        <h3>PUT - 完整更新用户</h3>
        <p class="hint">选择一个用户进行完整更新（需要提供所有字段）</p>
        <select v-model.number="updateUserData.id" @change="(e: any) => {
          const user = users.find(u => u.id === Number(e.target.value));
          if (user) {
            updateUserData.name = user.name;
            updateUserData.email = user.email;
            updateUserData.age = user.age;
          }
        }">
          <option value="">选择用户</option>
          <option v-for="user in users" :key="user.id" :value="user.id">
            {{ user.name }}
          </option>
        </select>
        
        <form v-if="updateUserData.id" @submit.prevent="updateUser(updateUserData.id!)" class="form">
          <div class="form-group">
            <label>姓名</label>
            <input v-model="updateUserData.name" required>
          </div>
          <div class="form-group">
            <label>邮箱</label>
            <input v-model="updateUserData.email" type="email" required>
          </div>
          <div class="form-group">
            <label>年龄</label>
            <input v-model.number="updateUserData.age" type="number">
          </div>
          <button type="submit" :disabled="loading">更新用户</button>
        </form>
      </div>

      <div class="example">
        <h3>PATCH - 部分更新用户</h3>
        <p class="hint">只更新单个字段（其他字段保持不变）</p>
        <div v-for="user in users" :key="user.id" class="patch-item">
          <strong>{{ user.name }}</strong>
          <div class="patch-controls">
            <input :value="user.name" @blur="(e: any) => partialUpdateUser(user.id!, 'name', e.target.value)" placeholder="修改名称">
            <input :value="user.age" @blur="(e: any) => partialUpdateUser(user.id!, 'age', Number(e.target.value))" type="number" placeholder="修改年龄">
          </div>
        </div>
      </div>
    </section>

    <!-- DELETE 请求示例 -->
    <section class="demo-section">
      <h2>4. DELETE 请求 - 删除数据</h2>
      
      <div class="example">
        <h3>删除用户</h3>
        <p class="hint">点击用户列表中的"删除"按钮即可删除用户</p>
        <div class="info-box">
          <p>💡 提示：删除操作会弹出确认对话框</p>
        </div>
      </div>
    </section>

    <!-- 文章 CRUD 示例 -->
    <section class="demo-section">
      <h2>5. 完整 CRUD 示例 - 文章管理</h2>
      
      <div class="example">
        <h3>创建文章</h3>
        <form @submit.prevent="createPost" class="form">
          <div class="form-group">
            <label>标题</label>
            <input v-model="newPost.title" required>
          </div>
          <div class="form-group">
            <label>内容</label>
            <textarea v-model="newPost.content" rows="4" required></textarea>
          </div>
          <div class="form-group">
            <label>作者 ID</label>
            <input v-model.number="newPost.author_id" type="number" required>
          </div>
          <button type="submit" :disabled="loading">发布文章</button>
        </form>
      </div>

      <div class="example">
        <h3>文章列表</h3>
        <button @click="fetchPosts" :disabled="loading">刷新文章列表</button>
        
        <div class="post-list">
          <div v-for="post in posts" :key="post.id" class="post-card">
            <h4>{{ post.title }}</h4>
            <p class="post-content">{{ post.content }}</p>
            <div class="post-meta">
              <span>作者 ID: {{ post.author_id }}</span>
              <span>{{ post.created_at }}</span>
            </div>
            <button @click="deletePost(post.id!)" class="btn-small btn-danger">删除</button>
          </div>
        </div>
      </div>
    </section>

    <!-- 错误处理和 Loading 示例 -->
    <section class="demo-section">
      <h2>6. 错误处理和 Loading 状态</h2>
      
      <div class="example">
        <h3>测试不同场景</h3>
        <div class="button-group">
          <button @click="testSlowRequest" :disabled="loading">
            测试慢速请求（2秒延迟）
          </button>
          <button @click="testErrorRequest" :disabled="loading">
            测试错误请求（500错误）
          </button>
        </div>
        <p class="hint">观察 Loading 状态和错误提示</p>
      </div>
    </section>

    <!-- API 文档链接 -->
    <section class="demo-section">
      <h2>7. API 文档</h2>
      <div class="example">
        <p>后端 API 文档（需要先启动后端服务）：</p>
        <div class="button-group">
          <a href="http://localhost:8000/docs" target="_blank" class="btn-link">
            Swagger UI 文档
          </a>
          <a href="http://localhost:8000/redoc" target="_blank" class="btn-link">
            ReDoc 文档
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
  color: #42b983;
  margin-bottom: 2rem;
  font-size: 2.5rem;
}

.demo-section {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  border-left: 4px solid #42b983;
}

.demo-section h2 {
  color: #2c3e50;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.demo-section h3 {
  color: #42b983;
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.example {
  background: white;
  padding: 1.5rem;
  border-radius: 6px;
  margin: 1rem 0;
  border: 1px solid #e1e8ed;
}

.loading {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(255, 255, 255, 0.95);
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  text-align: center;
  z-index: 1000;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #42b983;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error-message {
  background: #fee;
  color: #c33;
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 1rem;
  border-left: 4px solid #c33;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.btn-close {
  background: transparent;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0;
  width: 30px;
  height: 30px;
  color: #c33;
}

.user-list, .post-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.user-card, .post-card {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 6px;
  border: 1px solid #e1e8ed;
}

.user-card h4, .post-card h4 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.post-content {
  color: #5a6c7d;
  margin: 0.5rem 0;
  line-height: 1.6;
}

.post-meta {
  display: flex;
  justify-content: space-between;
  font-size: 0.85rem;
  color: #7f8c8d;
  margin: 0.5rem 0;
}

.user-detail {
  background: #e8f5e9;
  padding: 1rem;
  border-radius: 6px;
}

.user-detail p {
  margin: 0.5rem 0;
}

.form {
  max-width: 500px;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #2c3e50;
}

.search-form {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.patch-item {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 0.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.patch-controls {
  display: flex;
  gap: 0.5rem;
}

.patch-controls input {
  width: 150px;
}

.button-group {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-top: 0.5rem;
}

.info-box {
  background: #e3f2fd;
  padding: 1rem;
  border-radius: 6px;
  border-left: 3px solid #2196f3;
  margin-top: 1rem;
}

.hint {
  color: #7f8c8d;
  font-size: 0.9rem;
  font-style: italic;
  margin-bottom: 1rem;
}

button, .btn-link {
  background: #42b983;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.3s;
  text-decoration: none;
  display: inline-block;
}

button:hover, .btn-link:hover {
  background: #35a372;
}

button:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.btn-small {
  padding: 0.25rem 0.75rem;
  font-size: 0.9rem;
}

.btn-danger {
  background: #e74c3c;
}

.btn-danger:hover {
  background: #c0392b;
}

input, textarea, select {
  width: 100%;
  padding: 0.5rem;
  border: 2px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  font-family: inherit;
}

input:focus, textarea:focus, select:focus {
  outline: none;
  border-color: #42b983;
}

select {
  cursor: pointer;
}
</style>
