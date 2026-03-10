<script setup lang="ts">
import { ref, reactive } from 'vue'

// 1. 基础列表渲染
const items = ref(['苹果', '香蕉', '橙子', '葡萄'])

// 2. 对象数组
const users = ref([
  { id: 1, name: '张三', age: 25 },
  { id: 2, name: '李四', age: 30 },
  { id: 3, name: '王五', age: 28 }
])

// 3. 对象遍历
const userInfo = reactive({
  name: '张三',
  age: 25,
  email: 'zhangsan@example.com',
  city: '北京'
})

// 4. 范围遍历
const n = ref(10)

// 5. template 上的 v-for
const categories = ref([
  {
    name: '水果',
    items: ['苹果', '香蕉', '橙子']
  },
  {
    name: '蔬菜',
    items: ['白菜', '萝卜', '西红柿']
  }
])

// 6. 数组变化侦测
const todoList = ref([
  { id: 1, text: '学习 Vue 3', done: false },
  { id: 2, text: '写代码', done: true },
  { id: 3, text: '运动', done: false }
])

let nextId = 4

function addTodo() {
  todoList.value.push({
    id: nextId++,
    text: `新任务 ${nextId - 1}`,
    done: false
  })
}

function removeTodo(id: number) {
  const index = todoList.value.findIndex(todo => todo.id === id)
  if (index > -1) {
    todoList.value.splice(index, 1)
  }
}

function sortTodos() {
  todoList.value.sort((a, b) => a.text.localeCompare(b.text))
}

function reverseTodos() {
  todoList.value.reverse()
}

function filterCompleted() {
  todoList.value = todoList.value.filter(todo => !todo.done)
}

// 7. 嵌套 v-for
const nestedData = ref([
  {
    id: 1,
    title: '第一组',
    children: [
      { id: 11, name: '项目 1-1' },
      { id: 12, name: '项目 1-2' }
    ]
  },
  {
    id: 2,
    title: '第二组',
    children: [
      { id: 21, name: '项目 2-1' },
      { id: 22, name: '项目 2-2' }
    ]
  }
])
</script>

<template>
  <div class="container">
    <h1>07 - 列表渲染</h1>

    <section class="demo-section">
      <h2>1. 基础列表渲染 (v-for)</h2>
      <p>使用 v-for 指令基于一个数组来渲染一个列表</p>
      <div class="example">
        <ul>
          <li v-for="(item, index) in items" :key="index">
            {{ index + 1 }}. {{ item }}
          </li>
        </ul>
      </div>
      <div class="code-note">
        v-for 语法：<code>item in items</code> 或 <code>(item, index) in items</code>
      </div>
    </section>

    <section class="demo-section">
      <h2>2. 对象数组渲染</h2>
      <p>渲染对象数组，使用唯一的 key 属性</p>
      <div class="example">
        <div class="user-list">
          <div v-for="user in users" :key="user.id" class="user-card">
            <h3>{{ user.name }}</h3>
            <p>年龄: {{ user.age }}</p>
            <p class="hint">ID: {{ user.id }}</p>
          </div>
        </div>
      </div>
      <div class="code-note">
        ⚠️ 建议在使用 v-for 时提供 key attribute，除非输出的 DOM 内容非常简单
      </div>
    </section>

    <section class="demo-section">
      <h2>3. 遍历对象</h2>
      <p>可以使用 v-for 来遍历一个对象的所有属性</p>
      <div class="example">
        <div class="info-list">
          <div v-for="(value, key, index) in userInfo" :key="key" class="info-item">
            <span class="label">{{ index + 1 }}. {{ key }}:</span>
            <span class="value">{{ value }}</span>
          </div>
        </div>
      </div>
      <div class="code-note">
        遍历对象：<code>(value, key, index) in object</code>
      </div>
    </section>

    <section class="demo-section">
      <h2>4. 范围值 (v-for)</h2>
      <p>v-for 可以直接接受一个整数值，会基于 1...n 的范围来渲染</p>
      <div class="example">
        <div class="number-grid">
          <span v-for="num in n" :key="num" class="number-box">
            {{ num }}
          </span>
        </div>
        <div style="margin-top: 1rem;">
          <label>
            数量: <input type="number" v-model.number="n" min="1" max="20">
          </label>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>5. template 上的 v-for</h2>
      <p>可以在 &lt;template&gt; 标签上使用 v-for 来渲染一个包含多个元素的块</p>
      <div class="example">
        <div v-for="category in categories" :key="category.name" class="category">
          <template v-for="item in category.items" :key="item">
            <h4>{{ category.name }}</h4>
            <p>{{ item }}</p>
          </template>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>6. 数组变化侦测</h2>
      <p>Vue 能够侦听响应式数组的变更方法，并在它们被调用时触发相关的更新</p>
      <div class="example">
        <div class="todo-list">
          <div v-for="todo in todoList" :key="todo.id" class="todo-item">
            <input type="checkbox" v-model="todo.done">
            <span :class="{ done: todo.done }">{{ todo.text }}</span>
            <button @click="removeTodo(todo.id)" class="btn-remove">删除</button>
          </div>
        </div>
        <div class="button-group">
          <button @click="addTodo">添加任务</button>
          <button @click="sortTodos">排序</button>
          <button @click="reverseTodos">反转</button>
          <button @click="filterCompleted">移除已完成</button>
        </div>
      </div>
      <div class="code-note">
        变更方法：push()、pop()、shift()、unshift()、splice()、sort()、reverse()
      </div>
    </section>

    <section class="demo-section">
      <h2>7. 嵌套 v-for</h2>
      <p>v-for 可以嵌套使用</p>
      <div class="example">
        <div v-for="group in nestedData" :key="group.id" class="nested-group">
          <h3>{{ group.title }}</h3>
          <ul>
            <li v-for="child in group.children" :key="child.id">
              {{ child.name }}
            </li>
          </ul>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>8. key 的重要性</h2>
      <div class="info-box">
        <h3>为什么需要 key？</h3>
        <ul>
          <li>key 帮助 Vue 识别哪些元素改变了</li>
          <li>提高列表渲染的性能</li>
          <li>确保组件状态正确</li>
          <li>key 必须是唯一的</li>
          <li>不推荐使用索引作为 key（在列表会重新排序时）</li>
        </ul>
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

.hint {
  color: #7f8c8d;
  font-size: 0.9rem;
  font-style: italic;
}

.user-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

.user-card {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 6px;
  border: 1px solid #e1e8ed;
}

.user-card h3 {
  color: #42b983;
  margin-bottom: 0.5rem;
}

.info-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.info-item {
  display: flex;
  justify-content: space-between;
  padding: 0.75rem;
  background: #f8f9fa;
  border-radius: 4px;
}

.info-item .label {
  font-weight: bold;
  color: #5a6c7d;
}

.info-item .value {
  color: #2c3e50;
}

.number-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(50px, 1fr));
  gap: 0.5rem;
}

.number-box {
  background: #42b983;
  color: white;
  padding: 1rem;
  text-align: center;
  border-radius: 4px;
  font-weight: bold;
}

.category {
  margin-bottom: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 6px;
}

.category h4 {
  color: #42b983;
  margin-bottom: 0.5rem;
}

.todo-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.todo-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem;
  background: #f8f9fa;
  border-radius: 4px;
}

.todo-item span {
  flex: 1;
}

.todo-item span.done {
  text-decoration: line-through;
  color: #7f8c8d;
}

.btn-remove {
  background: #e74c3c;
  padding: 0.25rem 0.75rem;
  font-size: 0.9rem;
}

.btn-remove:hover {
  background: #c0392b;
}

.button-group {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.nested-group {
  margin-bottom: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 6px;
}

.nested-group h3 {
  color: #42b983;
  margin-bottom: 0.5rem;
}

.nested-group ul {
  list-style: none;
  padding-left: 1rem;
}

.nested-group li {
  padding: 0.25rem 0;
  color: #5a6c7d;
}

.info-box {
  background: #e3f2fd;
  padding: 1rem;
  border-radius: 6px;
  border-left: 3px solid #2196f3;
}

.info-box h3 {
  color: #1565c0;
  margin-bottom: 0.5rem;
}

.info-box ul {
  list-style: none;
  padding: 0;
}

.info-box li {
  padding: 0.25rem 0;
  padding-left: 1.5rem;
  position: relative;
  color: #1565c0;
}

.info-box li::before {
  content: '✓';
  position: absolute;
  left: 0;
  font-weight: bold;
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

input[type="number"] {
  padding: 0.5rem;
  border: 2px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  width: 100px;
}

input[type="number"]:focus {
  outline: none;
  border-color: #42b983;
}

label {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

ul {
  list-style-position: inside;
}
</style>
