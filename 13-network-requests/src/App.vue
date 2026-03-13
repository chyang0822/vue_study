<template>
  <div class="container">
    <header class="header">
      <h1>🌐 网络请求演示</h1>
      <p>Vue 3 + FastAPI 不同HTTP方法示例</p>
    </header>

    <main class="main-content">
      <!-- 左侧：操作面板 -->
      <section class="panel operations-panel">
        <h2>操作面板</h2>
        
        <!-- GET 请求 -->
        <div class="operation-group">
          <h3>📥 GET 请求</h3>
          <button @click="fetchAllUsers" :disabled="loading" class="btn btn-primary">
            {{ loading ? '加载中...' : '获取所有用户' }}
          </button>
          <div class="input-group">
            <input v-model.number="userId" type="number" placeholder="输入用户ID" />
            <button @click="fetchUserById" :disabled="loading || !userId" class="btn btn-primary">
              获取指定用户
            </button>
          </div>
        </div>

        <!-- POST 请求 -->
        <div class="operation-group">
          <h3>➕ POST 请求</h3>
          <div class="form-group">
            <input v-model="newUser.name" placeholder="姓名" class="input-field" />
            <input v-model="newUser.email" placeholder="邮箱" class="input-field" />
            <input v-model.number="newUser.age" type="number" placeholder="年龄" class="input-field" />
            <button @click="createUser" :disabled="loading" class="btn btn-success">
              创建用户
            </button>
          </div>
        </div>

        <!-- PUT 请求 -->
        <div class="operation-group">
          <h3>✏️ PUT 请求</h3>
          <div class="form-group">
            <input v-model.number="updateData.id" type="number" placeholder="用户ID" class="input-field" />
            <input v-model="updateData.name" placeholder="新姓名" class="input-field" />
            <input v-model="updateData.email" placeholder="新邮箱" class="input-field" />
            <input v-model.number="updateData.age" type="number" placeholder="新年龄" class="input-field" />
            <button @click="updateUser" :disabled="loading || !updateData.id" class="btn btn-warning">
              更新用户
            </button>
          </div>
        </div>

        <!-- PATCH 请求 -->
        <div class="operation-group">
          <h3>🔧 PATCH 请求</h3>
          <div class="form-group">
            <input v-model.number="patchData.id" type="number" placeholder="用户ID" class="input-field" />
            <input v-model="patchData.name" placeholder="新姓名（可选）" class="input-field" />
            <button @click="patchUser" :disabled="loading || !patchData.id" class="btn btn-info">
              部分更新用户
            </button>
          </div>
        </div>

        <!-- DELETE 请求 -->
        <div class="operation-group">
          <h3>🗑️ DELETE 请求</h3>
          <div class="input-group">
            <input v-model.number="deleteId" type="number" placeholder="输入要删除的用户ID" />
            <button @click="deleteUser" :disabled="loading || !deleteId" class="btn btn-danger">
              删除用户
            </button>
          </div>
        </div>
      </section>

      <!-- 右侧：响应显示 -->
      <section class="panel response-panel">
        <h2>响应结果</h2>
        
        <!-- 错误信息 -->
        <div v-if="error" class="alert alert-error">
          <strong>❌ 错误：</strong> {{ error }}
        </div>

        <!-- 成功信息 -->
        <div v-if="successMessage" class="alert alert-success">
          <strong>✅ 成功：</strong> {{ successMessage }}
        </div>

        <!-- 响应数据 -->
        <div v-if="responseData" class="response-content">
          <h3>📊 数据响应</h3>
          <pre>{{ JSON.stringify(responseData, null, 2) }}</pre>
        </div>

        <!-- 加载状态 -->
        <div v-if="loading" class="loading">
          <div class="spinner"></div>
          <p>请求处理中...</p>
        </div>

        <!-- 空状态 -->
        <div v-if="!loading && !responseData && !error && !successMessage" class="empty-state">
          <p>👈 选择操作开始发送请求</p>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { apiService } from './api'

// 状态
const loading = ref(false)
const error = ref('')
const successMessage = ref('')
const responseData = ref<any>(null)

// 表单数据
const userId = ref<number | null>(null)
const deleteId = ref<number | null>(null)

const newUser = ref({
  name: '',
  email: '',
  age: null as number | null
})

const updateData = ref({
  id: null as number | null,
  name: '',
  email: '',
  age: null as number | null
})

const patchData = ref({
  id: null as number | null,
  name: ''
})

// 清除消息
const clearMessages = () => {
  error.value = ''
  successMessage.value = ''
}

// GET - 获取所有用户
const fetchAllUsers = async () => {
  clearMessages()
  loading.value = true
  try {
    const response = await apiService.getUsers()
    responseData.value = response.data
    successMessage.value = '成功获取所有用户'
  } catch (err: any) {
    error.value = err.response?.data?.detail || err.message || '获取用户失败'
  } finally {
    loading.value = false
  }
}

// GET - 获取指定用户
const fetchUserById = async () => {
  if (!userId.value) return
  clearMessages()
  loading.value = true
  try {
    const response = await apiService.getUserById(userId.value)
    responseData.value = response.data
    successMessage.value = `成功获取用户 ID: ${userId.value}`
  } catch (err: any) {
    error.value = err.response?.data?.detail || err.message || '获取用户失败'
  } finally {
    loading.value = false
  }
}

// POST - 创建用户
const createUser = async () => {
  if (!newUser.value.name || !newUser.value.email || !newUser.value.age) {
    error.value = '请填写所有字段'
    return
  }
  clearMessages()
  loading.value = true
  try {
    const response = await apiService.createUser(newUser.value)
    responseData.value = response.data
    successMessage.value = '用户创建成功'
    newUser.value = { name: '', email: '', age: null }
  } catch (err: any) {
    error.value = err.response?.data?.detail || err.message || '创建用户失败'
  } finally {
    loading.value = false
  }
}

// PUT - 更新用户
const updateUser = async () => {
  if (!updateData.value.id || !updateData.value.name || !updateData.value.email || !updateData.value.age) {
    error.value = '请填写所有字段'
    return
  }
  clearMessages()
  loading.value = true
  try {
    const { id, ...data } = updateData.value
    const response = await apiService.updateUser(id!, data)
    responseData.value = response.data
    successMessage.value = `用户 ID: ${id} 更新成功`
    updateData.value = { id: null, name: '', email: '', age: null }
  } catch (err: any) {
    error.value = err.response?.data?.detail || err.message || '更新用户失败'
  } finally {
    loading.value = false
  }
}

// PATCH - 部分更新用户
const patchUser = async () => {
  if (!patchData.value.id) {
    error.value = '请输入用户ID'
    return
  }
  clearMessages()
  loading.value = true
  try {
    const { id, ...data } = patchData.value
    const response = await apiService.patchUser(id!, data)
    responseData.value = response.data
    successMessage.value = `用户 ID: ${id} 部分更新成功`
    patchData.value = { id: null, name: '' }
  } catch (err: any) {
    error.value = err.response?.data?.detail || err.message || '更新用户失败'
  } finally {
    loading.value = false
  }
}

// DELETE - 删除用户
const deleteUser = async () => {
  if (!deleteId.value) return
  clearMessages()
  loading.value = true
  try {
    const response = await apiService.deleteUser(deleteId.value)
    responseData.value = response.data
    successMessage.value = `用户 ID: ${deleteId.value} 删除成功`
    deleteId.value = null
  } catch (err: any) {
    error.value = err.response?.data?.detail || err.message || '删除用户失败'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.container {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.header {
  text-align: center;
  color: white;
  margin-bottom: 30px;
  animation: slideDown 0.6s ease-out;
}

.header h1 {
  font-size: 2.5em;
  margin-bottom: 10px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.header p {
  font-size: 1.1em;
  opacity: 0.9;
}

.main-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  max-width: 1400px;
  margin: 0 auto;
}

.panel {
  background: white;
  border-radius: 12px;
  padding: 25px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  animation: fadeIn 0.6s ease-out;
}

.panel h2 {
  color: #333;
  margin-bottom: 20px;
  font-size: 1.5em;
  border-bottom: 3px solid #667eea;
  padding-bottom: 10px;
}

.panel h3 {
  color: #555;
  margin-top: 20px;
  margin-bottom: 12px;
  font-size: 1.1em;
}

.operation-group {
  margin-bottom: 20px;
  padding: 15px;
  background: #f8f9fa;
  border-radius: 8px;
  border-left: 4px solid #667eea;
}

.form-group,
.input-group {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.input-field {
  padding: 10px 12px;
  border: 2px solid #e0e0e0;
  border-radius: 6px;
  font-size: 0.95em;
  transition: all 0.3s ease;
}

.input-field:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.btn {
  padding: 10px 16px;
  border: none;
  border-radius: 6px;
  font-size: 0.95em;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-primary {
  background: #667eea;
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background: #5568d3;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.btn-success {
  background: #48bb78;
  color: white;
}

.btn-success:hover:not(:disabled) {
  background: #38a169;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(72, 187, 120, 0.4);
}

.btn-warning {
  background: #ed8936;
  color: white;
}

.btn-warning:hover:not(:disabled) {
  background: #dd6b20;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(237, 137, 54, 0.4);
}

.btn-info {
  background: #4299e1;
  color: white;
}

.btn-info:hover:not(:disabled) {
  background: #3182ce;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(66, 153, 225, 0.4);
}

.btn-danger {
  background: #f56565;
  color: white;
}

.btn-danger:hover:not(:disabled) {
  background: #e53e3e;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(245, 101, 101, 0.4);
}

.response-panel {
  max-height: 600px;
  overflow-y: auto;
}

.alert {
  padding: 15px;
  border-radius: 6px;
  margin-bottom: 15px;
  font-size: 0.95em;
  animation: slideIn 0.3s ease-out;
}

.alert-error {
  background: #fed7d7;
  color: #c53030;
  border-left: 4px solid #f56565;
}

.alert-success {
  background: #c6f6d5;
  color: #22543d;
  border-left: 4px solid #48bb78;
}

.response-content {
  background: #f8f9fa;
  border-radius: 6px;
  padding: 15px;
  margin-bottom: 15px;
}

.response-content h3 {
  margin-top: 0;
  color: #333;
}

.response-content pre {
  background: #2d3748;
  color: #e2e8f0;
  padding: 12px;
  border-radius: 4px;
  overflow-x: auto;
  font-size: 0.85em;
  line-height: 1.5;
}

.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 15px;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #e0e0e0;
  border-top-color: #667eea;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

.empty-state {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  color: #999;
  font-size: 1.1em;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .main-content {
    grid-template-columns: 1fr;
  }

  .header h1 {
    font-size: 2em;
  }
}

@media (max-width: 640px) {
  .container {
    padding: 10px;
  }

  .panel {
    padding: 15px;
  }

  .header h1 {
    font-size: 1.5em;
  }

  .form-group,
  .input-group {
    flex-direction: column;
  }

  .btn {
    width: 100%;
  }
}
</style>
