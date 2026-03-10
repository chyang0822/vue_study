<script setup lang="ts">
import { ref } from 'vue'

// 1. v-if 条件渲染
const show = ref(true)
const type = ref('A')

// 2. v-else
const awesome = ref(true)

// 3. v-else-if
const score = ref(85)

// 4. v-show
const showWithVShow = ref(true)

// 5. 登录状态示例
const isLoggedIn = ref(false)
const username = ref('游客')

function login() {
  isLoggedIn.value = true
  username.value = '张三'
}

function logout() {
  isLoggedIn.value = false
  username.value = '游客'
}
</script>

<template>
  <div class="container">
    <h1>06 - 条件渲染</h1>

    <section class="demo-section">
      <h2>1. v-if 指令</h2>
      <p>v-if 指令用于条件性地渲染一块内容。这块内容只会在指令的表达式返回真值时才被渲染</p>
      <div class="example">
        <p v-if="show" class="message success">✓ 内容可见</p>
        <button @click="show = !show">切换显示</button>
      </div>
      <div class="code-note">
        当前状态: {{ show ? '显示' : '隐藏' }}
      </div>
    </section>

    <section class="demo-section">
      <h2>2. v-else 指令</h2>
      <p>可以使用 v-else 为 v-if 添加一个"else 区块"</p>
      <div class="example">
        <div v-if="awesome" class="message success">
          Vue 很棒！
        </div>
        <div v-else class="message info">
          哦不 😢
        </div>
        <button @click="awesome = !awesome">切换</button>
      </div>
    </section>

    <section class="demo-section">
      <h2>3. v-else-if 指令</h2>
      <p>v-else-if 提供的是相应于 v-if 的"else if 区块"，可以连续多次重复使用</p>
      <div class="example">
        <div class="score-input">
          <label>分数: <input type="number" v-model.number="score" min="0" max="100"></label>
        </div>
        <div v-if="score >= 90" class="message success">
          优秀！🎉
        </div>
        <div v-else-if="score >= 80" class="message success">
          良好！👍
        </div>
        <div v-else-if="score >= 60" class="message warning">
          及格 ✓
        </div>
        <div v-else class="message error">
          不及格 ✗
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>4. template 上的 v-if</h2>
      <p>可以在 &lt;template&gt; 元素上使用 v-if，这只是一个不可见的包装器元素，最后渲染的结果并不会包含这个元素</p>
      <div class="example">
        <button @click="type = type === 'A' ? 'B' : 'A'">切换类型 (当前: {{ type }})</button>
        <template v-if="type === 'A'">
          <h3>类型 A</h3>
          <p>这是类型 A 的内容</p>
          <p>可以包含多个元素</p>
        </template>
        <template v-else>
          <h3>类型 B</h3>
          <p>这是类型 B 的内容</p>
          <p>也可以包含多个元素</p>
        </template>
      </div>
    </section>

    <section class="demo-section">
      <h2>5. v-show 指令</h2>
      <p>v-show 会在 DOM 渲染中保留该元素，仅切换 display CSS 属性</p>
      <div class="example">
        <p v-show="showWithVShow" class="message info">
          使用 v-show 控制显示
        </p>
        <button @click="showWithVShow = !showWithVShow">切换 v-show</button>
      </div>
      <div class="code-note">
        v-show 不支持在 &lt;template&gt; 元素上使用，也不能和 v-else 搭配使用
      </div>
    </section>

    <section class="demo-section">
      <h2>6. v-if vs v-show</h2>
      <div class="comparison">
        <div class="comparison-item">
          <h3>v-if</h3>
          <ul>
            <li>"真实的"按条件渲染</li>
            <li>切换时元素会被销毁和重建</li>
            <li>惰性的：初始条件为假时不渲染</li>
            <li>有更高的切换开销</li>
            <li>适合条件很少改变的场景</li>
          </ul>
        </div>
        <div class="comparison-item">
          <h3>v-show</h3>
          <ul>
            <li>基于 CSS 的切换</li>
            <li>元素始终会被渲染</li>
            <li>不管初始条件如何都会渲染</li>
            <li>有更高的初始渲染开销</li>
            <li>适合频繁切换的场景</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>7. 实际应用：登录状态</h2>
      <div class="example">
        <div class="login-demo">
          <div v-if="isLoggedIn" class="user-info">
            <p>欢迎回来，{{ username }}！</p>
            <button @click="logout">退出登录</button>
          </div>
          <div v-else class="login-prompt">
            <p>您还未登录</p>
            <button @click="login">登录</button>
          </div>
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

.message {
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 1rem;
  font-weight: 500;
}

.message.success {
  background: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.message.info {
  background: #d1ecf1;
  color: #0c5460;
  border: 1px solid #bee5eb;
}

.message.warning {
  background: #fff3cd;
  color: #856404;
  border: 1px solid #ffeaa7;
}

.message.error {
  background: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.code-note {
  background: #fff3cd;
  padding: 0.75rem;
  border-radius: 4px;
  border-left: 3px solid #ffc107;
  font-size: 0.9rem;
  margin-top: 1rem;
}

.score-input {
  margin-bottom: 1rem;
}

.score-input input {
  width: 100px;
}

.comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-top: 1rem;
}

.comparison-item {
  background: white;
  padding: 1.5rem;
  border-radius: 6px;
  border: 1px solid #e1e8ed;
}

.comparison-item h3 {
  color: #42b983;
  margin-bottom: 1rem;
  font-size: 1.2rem;
}

.comparison-item ul {
  list-style: none;
  padding: 0;
}

.comparison-item li {
  padding: 0.5rem 0;
  padding-left: 1.5rem;
  position: relative;
  color: #5a6c7d;
}

.comparison-item li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: #42b983;
  font-weight: bold;
  font-size: 1.2rem;
}

.login-demo {
  text-align: center;
}

.user-info,
.login-prompt {
  padding: 2rem;
}

button {
  background: #42b983;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  margin-right: 0.5rem;
  transition: background 0.3s;
}

button:hover {
  background: #35a372;
}

input {
  padding: 0.5rem;
  border: 2px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

input:focus {
  outline: none;
  border-color: #42b983;
}

label {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

h3 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}
</style>
