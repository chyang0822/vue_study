<script setup lang="ts">
import { ref } from 'vue'

// 1. 文本输入
const message = ref('')
const multilineText = ref('')

// 2. 复选框
const checked = ref(false)
const checkedNames = ref<string[]>([])

// 3. 单选按钮
const picked = ref('')

// 4. 选择器
const selected = ref('')
const multiSelected = ref<string[]>([])

// 5. 修饰符示例
const lazyValue = ref('')
const numberValue = ref(0)
const trimValue = ref('')

// 6. 完整表单示例
const formData = ref({
  username: '',
  email: '',
  password: '',
  gender: '',
  hobbies: [] as string[],
  country: '',
  agree: false,
  bio: ''
})

function submitForm() {
  console.log('表单数据:', formData.value)
  alert('表单已提交！查看控制台')
}

function resetForm() {
  formData.value = {
    username: '',
    email: '',
    password: '',
    gender: '',
    hobbies: [],
    country: '',
    agree: false,
    bio: ''
  }
}
</script>

<template>
  <div class="container">
    <h1>09 - 表单输入绑定</h1>

    <section class="demo-section">
      <h2>1. 文本输入 (v-model)</h2>
      <p>v-model 在表单输入元素上创建双向数据绑定</p>
      <div class="example">
        <h3>单行文本</h3>
        <input v-model="message" placeholder="输入消息">
        <p>消息是: {{ message }}</p>

        <h3 style="margin-top: 1.5rem;">多行文本</h3>
        <textarea v-model="multilineText" placeholder="输入多行文本" rows="4"></textarea>
        <p style="white-space: pre-line;">{{ multilineText }}</p>
      </div>
      <div class="code-note">
        v-model 会忽略表单元素上的 value、checked、selected 等初始值
      </div>
    </section>

    <section class="demo-section">
      <h2>2. 复选框</h2>
      <div class="example">
        <h3>单个复选框</h3>
        <label>
          <input type="checkbox" v-model="checked">
          {{ checked ? '已选中' : '未选中' }}
        </label>

        <h3 style="margin-top: 1.5rem;">多个复选框</h3>
        <div class="checkbox-group">
          <label>
            <input type="checkbox" value="Vue" v-model="checkedNames">
            Vue
          </label>
          <label>
            <input type="checkbox" value="React" v-model="checkedNames">
            React
          </label>
          <label>
            <input type="checkbox" value="Angular" v-model="checkedNames">
            Angular
          </label>
        </div>
        <p>选中的: {{ checkedNames.join(', ') }}</p>
      </div>
    </section>

    <section class="demo-section">
      <h2>3. 单选按钮</h2>
      <div class="example">
        <div class="radio-group">
          <label>
            <input type="radio" value="Vue" v-model="picked">
            Vue
          </label>
          <label>
            <input type="radio" value="React" v-model="picked">
            React
          </label>
          <label>
            <input type="radio" value="Angular" v-model="picked">
            Angular
          </label>
        </div>
        <p>选中的: {{ picked }}</p>
      </div>
    </section>

    <section class="demo-section">
      <h2>4. 选择器</h2>
      <div class="example">
        <h3>单选</h3>
        <select v-model="selected">
          <option disabled value="">请选择</option>
          <option>Vue</option>
          <option>React</option>
          <option>Angular</option>
        </select>
        <p>选中的: {{ selected }}</p>

        <h3 style="margin-top: 1.5rem;">多选</h3>
        <select v-model="multiSelected" multiple style="height: 100px;">
          <option>Vue</option>
          <option>React</option>
          <option>Angular</option>
          <option>Svelte</option>
        </select>
        <p>选中的: {{ multiSelected.join(', ') }}</p>
      </div>
    </section>

    <section class="demo-section">
      <h2>5. 修饰符</h2>
      <div class="example">
        <h3>.lazy - 在 change 事件后同步</h3>
        <input v-model.lazy="lazyValue" placeholder="失去焦点后更新">
        <p>值: {{ lazyValue }}</p>

        <h3 style="margin-top: 1.5rem;">.number - 自动转换为数字</h3>
        <input v-model.number="numberValue" type="number">
        <p>值: {{ numberValue }} (类型: {{ typeof numberValue }})</p>

        <h3 style="margin-top: 1.5rem;">.trim - 自动去除首尾空格</h3>
        <input v-model.trim="trimValue" placeholder="输入带空格的文本">
        <p>值: "{{ trimValue }}"</p>
      </div>
    </section>

    <section class="demo-section">
      <h2>6. 完整表单示例</h2>
      <div class="example">
        <form @submit.prevent="submitForm" class="form">
          <div class="form-group">
            <label>用户名:</label>
            <input v-model="formData.username" required>
          </div>

          <div class="form-group">
            <label>邮箱:</label>
            <input v-model="formData.email" type="email" required>
          </div>

          <div class="form-group">
            <label>密码:</label>
            <input v-model="formData.password" type="password" required>
          </div>

          <div class="form-group">
            <label>性别:</label>
            <div class="radio-group">
              <label>
                <input type="radio" value="male" v-model="formData.gender">
                男
              </label>
              <label>
                <input type="radio" value="female" v-model="formData.gender">
                女
              </label>
            </div>
          </div>

          <div class="form-group">
            <label>爱好:</label>
            <div class="checkbox-group">
              <label>
                <input type="checkbox" value="reading" v-model="formData.hobbies">
                阅读
              </label>
              <label>
                <input type="checkbox" value="sports" v-model="formData.hobbies">
                运动
              </label>
              <label>
                <input type="checkbox" value="music" v-model="formData.hobbies">
                音乐
              </label>
            </div>
          </div>

          <div class="form-group">
            <label>国家:</label>
            <select v-model="formData.country" required>
              <option value="">请选择</option>
              <option value="cn">中国</option>
              <option value="us">美国</option>
              <option value="jp">日本</option>
            </select>
          </div>

          <div class="form-group">
            <label>个人简介:</label>
            <textarea v-model="formData.bio" rows="4"></textarea>
          </div>

          <div class="form-group">
            <label>
              <input type="checkbox" v-model="formData.agree" required>
              我同意服务条款
            </label>
          </div>

          <div class="button-group">
            <button type="submit">提交</button>
            <button type="button" @click="resetForm">重置</button>
          </div>
        </form>

        <div class="form-preview">
          <h3>表单数据预览:</h3>
          <pre>{{ JSON.stringify(formData, null, 2) }}</pre>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.container {
  max-width: 900px;
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

.demo-section > p {
  color: #5a6c7d;
  margin-bottom: 1rem;
  line-height: 1.6;
}

.example {
  background: white;
  padding: 1.5rem;
  border-radius: 6px;
  margin: 1rem 0;
  border: 1px solid #e1e8ed;
}

.code-note {
  background: #fff3cd;
  padding: 0.75rem;
  border-radius: 4px;
  border-left: 3px solid #ffc107;
  font-size: 0.9rem;
  margin-top: 1rem;
}

.checkbox-group,
.radio-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form {
  max-width: 500px;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group > label:first-child {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #2c3e50;
}

.form-preview {
  margin-top: 2rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 6px;
}

.form-preview h3 {
  color: #42b983;
  margin-bottom: 0.5rem;
}

.form-preview pre {
  background: #2c3e50;
  color: #42b983;
  padding: 1rem;
  border-radius: 4px;
  overflow-x: auto;
  font-size: 0.9rem;
}

.button-group {
  display: flex;
  gap: 0.5rem;
}

button {
  background: #42b983;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.3s;
}

button:hover {
  background: #35a372;
}

button[type="button"] {
  background: #7f8c8d;
}

button[type="button"]:hover {
  background: #5a6c7d;
}

input[type="text"],
input[type="email"],
input[type="password"],
input[type="number"],
input:not([type]),
textarea,
select {
  width: 100%;
  padding: 0.5rem;
  border: 2px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  font-family: inherit;
}

input:focus,
textarea:focus,
select:focus {
  outline: none;
  border-color: #42b983;
}

label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}

input[type="checkbox"],
input[type="radio"] {
  width: auto;
  cursor: pointer;
}
</style>
