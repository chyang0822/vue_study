<script setup lang="ts">
import { ref } from 'vue'

// 响应式状态
const message = ref('Hello Vue 3!')
const count = ref(0)

// 方法
function increment() {
  count.value++
}
</script>

<template>
  <div class="container">
    <h1>01 - 快速开始</h1>
    
    <section class="demo-section">
      <h2>1. 声明式渲染</h2>
      <p>{{ message }}</p>
      <p>计数器: {{ count }}</p>
      <button @click="increment">增加</button>
    </section>

    <section class="demo-section">
      <h2>2. 响应式基础</h2>
      <p>Vue 会自动跟踪 JavaScript 状态并在其发生变化时响应式地更新 DOM</p>
      <input v-model="message" placeholder="修改消息">
      <p>你输入的是: {{ message }}</p>
    </section>

    <section class="demo-section">
      <h2>3. Attribute 绑定</h2>
      <p :id="'dynamic-' + count" :class="{ active: count > 5 }">
        这个段落的 ID 是动态的: dynamic-{{ count }}
      </p>
      <p class="hint">当计数大于 5 时，上面的文字会变成红色</p>
    </section>

    <section class="demo-section">
      <h2>4. 事件监听</h2>
      <button @click="count++">点击次数: {{ count }}</button>
      <button @click="count = 0">重置</button>
    </section>
  </div>
</template>

<style scoped>
.container {
  max-width: 800px;
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
  width: 300px;
  margin-bottom: 0.5rem;
}

input:focus {
  outline: none;
  border-color: #42b983;
}

.active {
  color: #e74c3c;
  font-weight: bold;
}

.hint {
  color: #7f8c8d;
  font-size: 0.9rem;
  font-style: italic;
}
</style>
