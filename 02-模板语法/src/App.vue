<script setup lang="ts">
import { ref } from 'vue'

// 响应式数据
const message = ref('Hello Vue!')
const rawHtml = ref('<span style="color: red; font-weight: bold;">这是红色粗体文本</span>')
const dynamicId = ref('my-element')
const isDisabled = ref(false)
const url = ref('https://cn.vuejs.org')
const number = ref(10)
const ok = ref(true)
const attributeName = ref('id')
const eventName = ref('click')
const clickCount = ref(0)

// 方法
function handleDynamicEvent() {
  clickCount.value++
}
</script>

<template>
  <div class="container">
    <h1>02 - 模板语法</h1>

    <section class="demo-section">
      <h2>1. 文本插值 (Mustache 语法)</h2>
      <p>最基本的数据绑定形式是文本插值，使用 "Mustache" 语法（双大括号）：</p>
      <div class="example">
        <p>消息: {{ message }}</p>
        <input v-model="message" placeholder="修改消息">
      </div>
      <div class="code-note">
        <code>{{ "{{ message }}" }}</code> 会被替换为相应组件实例中 message 属性的值
      </div>
    </section>

    <section class="demo-section">
      <h2>2. 原始 HTML (v-html)</h2>
      <p>双大括号会将数据解释为纯文本。若想插入 HTML，需要使用 v-html 指令：</p>
      <div class="example">
        <p>使用文本插值: {{ rawHtml }}</p>
        <p>使用 v-html: <span v-html="rawHtml"></span></p>
      </div>
      <div class="warning">
        ⚠️ 警告：在网站上动态渲染任意 HTML 是非常危险的，容易导致 XSS 攻击。
        请仅在内容安全可信时使用 v-html。
      </div>
    </section>

    <section class="demo-section">
      <h2>3. Attribute 绑定 (v-bind)</h2>
      <p>双大括号不能在 HTML attributes 中使用。想要响应式地绑定一个 attribute，应该使用 v-bind 指令：</p>
      <div class="example">
        <div :id="dynamicId" class="dynamic-box">
          这个 div 的 id 是动态的: {{ dynamicId }}
        </div>
        <input v-model="dynamicId" placeholder="修改 ID">
        
        <div style="margin-top: 1rem;">
          <button :disabled="isDisabled">按钮</button>
          <label style="margin-left: 1rem;">
            <input type="checkbox" v-model="isDisabled"> 禁用按钮
          </label>
        </div>
      </div>
      <div class="code-note">
        简写：<code>v-bind:id</code> 可以简写为 <code>:id</code>
      </div>
    </section>

    <section class="demo-section">
      <h2>4. JavaScript 表达式</h2>
      <p>Vue 在所有的数据绑定中都支持完整的 JavaScript 表达式：</p>
      <div class="example">
        <p>数字: {{ number }}</p>
        <p>数字 + 1: {{ number + 1 }}</p>
        <p>三元表达式: {{ ok ? '是' : '否' }}</p>
        <p>方法调用: {{ message.split('').reverse().join('') }}</p>
        <p>模板字符串: {{ `消息是: ${message}` }}</p>
        
        <div style="margin-top: 1rem;">
          <input type="number" v-model.number="number" style="width: 100px;">
          <label style="margin-left: 1rem;">
            <input type="checkbox" v-model="ok"> OK 状态
          </label>
        </div>
      </div>
      <div class="code-note">
        注意：每个绑定仅支持单一表达式，语句和控制流不会生效
      </div>
    </section>

    <section class="demo-section">
      <h2>5. 指令 (Directives)</h2>
      <p>指令是带有 v- 前缀的特殊 attribute。指令的值预期是一个 JavaScript 表达式：</p>
      <div class="example">
        <a :href="url" target="_blank">访问 Vue.js 官网</a>
        <p style="margin-top: 1rem;">
          <input v-model="url" placeholder="修改链接" style="width: 300px;">
        </p>
      </div>
      <div class="code-note">
        <code>v-bind:href="url"</code> 将元素的 href attribute 与表达式 url 的值绑定
      </div>
    </section>

    <section class="demo-section">
      <h2>6. 动态参数</h2>
      <p>可以在指令参数上使用一个 JavaScript 表达式，需要包含在一对方括号内：</p>
      <div class="example">
        <div :[attributeName]="'dynamic-value'" class="dynamic-box">
          动态 attribute 名称: {{ attributeName }}
        </div>
        <p>
          <input v-model="attributeName" placeholder="修改 attribute 名称">
        </p>
        
        <button @[eventName]="handleDynamicEvent" style="margin-top: 1rem;">
          动态事件: {{ eventName }}
        </button>
        <p>点击次数: {{ clickCount }}</p>
        <p>
          <input v-model="eventName" placeholder="修改事件名称">
        </p>
      </div>
      <div class="code-note">
        动态参数值应当是一个字符串，或者是 null（用于移除绑定）
      </div>
    </section>

    <section class="demo-section">
      <h2>7. 修饰符 (Modifiers)</h2>
      <p>修饰符是以点开头的特殊后缀，表明指令需要以一些特殊的方式被绑定：</p>
      <div class="example">
        <form @submit.prevent="handleDynamicEvent">
          <input type="text" placeholder="按回车提交">
          <button type="submit">提交 (阻止默认行为)</button>
        </form>
        <p>提交次数: {{ clickCount }}</p>
      </div>
      <div class="code-note">
        <code>.prevent</code> 修饰符会调用 event.preventDefault()
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

.dynamic-box {
  background: #e8f5e9;
  padding: 1rem;
  border-radius: 4px;
  margin-bottom: 1rem;
  border: 2px dashed #42b983;
}

.code-note {
  background: #fff3cd;
  padding: 0.75rem;
  border-radius: 4px;
  border-left: 3px solid #ffc107;
  font-size: 0.9rem;
  margin-top: 1rem;
}

.code-note code {
  background: #fff;
  padding: 0.2rem 0.4rem;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  color: #e83e8c;
}

.warning {
  background: #fff3cd;
  border: 1px solid #ffc107;
  padding: 1rem;
  border-radius: 4px;
  margin-top: 1rem;
  color: #856404;
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

button:hover:not(:disabled) {
  background: #35a372;
}

button:disabled {
  background: #ccc;
  cursor: not-allowed;
}

input[type="text"],
input[type="number"],
input:not([type]) {
  padding: 0.5rem;
  border: 2px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

input:focus {
  outline: none;
  border-color: #42b983;
}

a {
  color: #42b983;
  text-decoration: none;
  font-weight: bold;
}

a:hover {
  text-decoration: underline;
}

form {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}
</style>
