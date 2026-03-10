<script setup lang="ts">
import { ref, reactive, toRefs, isRef, isReactive, toRef } from 'vue'

// 1. ref() - 创建响应式引用
const count = ref(0)
const message = ref('Hello Vue!')

// 2. reactive() - 创建响应式对象
const state = reactive({
  name: '张三',
  age: 25,
  hobbies: ['读书', '运动', '编程']
})

// 3. 深层响应性
const deepState = reactive({
  nested: {
    count: 0
  }
})

// 4. toRefs() - 将响应式对象转换为普通对象，其中每个属性都是 ref
const stateRefs = toRefs(state)

// 5. toRef() - 为响应式对象的单个属性创建 ref
const ageRef = toRef(state, 'age')

// 方法
function increment() {
  count.value++
}

function incrementDeep() {
  deepState.nested.count++
}

function addHobby() {
  state.hobbies.push(`爱好${state.hobbies.length + 1}`)
}
</script>

<template>
  <div class="container">
    <h1>03 - 响应式基础</h1>

    <section class="demo-section">
      <h2>1. ref() - 响应式引用</h2>
      <p>ref() 接收一个内部值，返回一个响应式的、可更改的 ref 对象，此对象只有一个指向其内部值的属性 .value</p>
      <div class="example">
        <p>计数: {{ count }}</p>
        <button @click="increment">增加</button>
        <button @click="count = 0">重置</button>
        
        <p style="margin-top: 1rem;">消息: {{ message }}</p>
        <input v-model="message" placeholder="修改消息">
      </div>
      <div class="code-note">
        在模板中使用 ref 时，会自动解包，不需要 .value
      </div>
    </section>

    <section class="demo-section">
      <h2>2. reactive() - 响应式对象</h2>
      <p>reactive() 返回一个对象的响应式代理，响应式转换是"深层"的</p>
      <div class="example">
        <p>姓名: {{ state.name }}</p>
        <p>年龄: {{ state.age }}</p>
        <p>爱好: {{ state.hobbies.join(', ') }}</p>
        
        <div style="margin-top: 1rem;">
          <input v-model="state.name" placeholder="修改姓名">
          <input type="number" v-model.number="state.age" placeholder="修改年龄" style="width: 100px; margin-left: 0.5rem;">
          <button @click="addHobby" style="margin-left: 0.5rem;">添加爱好</button>
        </div>
      </div>
      <div class="code-note">
        reactive() 只能用于对象类型（对象、数组和 Map、Set 这样的集合类型）
      </div>
    </section>

    <section class="demo-section">
      <h2>3. 深层响应性</h2>
      <p>reactive() 创建的对象是深层响应式的，嵌套对象的变化也会被追踪</p>
      <div class="example">
        <p>嵌套计数: {{ deepState.nested.count }}</p>
        <button @click="incrementDeep">增加嵌套计数</button>
      </div>
    </section>

    <section class="demo-section">
      <h2>4. ref vs reactive</h2>
      <div class="comparison">
        <div class="comparison-item">
          <h3>ref()</h3>
          <ul>
            <li>可以存储任何值类型</li>
            <li>需要通过 .value 访问</li>
            <li>在模板中自动解包</li>
            <li>可以重新赋值整个对象</li>
          </ul>
        </div>
        <div class="comparison-item">
          <h3>reactive()</h3>
          <ul>
            <li>只能用于对象类型</li>
            <li>直接访问属性</li>
            <li>深层响应式</li>
            <li>不能替换整个对象</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>5. toRefs() - 解构响应式对象</h2>
      <p>将响应式对象转换为普通对象，其中每个属性都是指向原对象相应属性的 ref</p>
      <div class="example">
        <p>通过 toRefs 解构的姓名: {{ stateRefs.name.value }}</p>
        <p>通过 toRefs 解构的年龄: {{ stateRefs.age.value }}</p>
        <p class="hint">这样可以在解构时保持响应性</p>
      </div>
    </section>

    <section class="demo-section">
      <h2>6. toRef() - 单个属性转 ref</h2>
      <p>为响应式对象的单个属性创建 ref，保持与源对象的响应式连接</p>
      <div class="example">
        <p>原始年龄: {{ state.age }}</p>
        <p>toRef 年龄: {{ ageRef }}</p>
        <button @click="ageRef++">通过 ref 增加年龄</button>
        <button @click="state.age++">通过原对象增加年龄</button>
      </div>
    </section>

    <section class="demo-section">
      <h2>7. 响应式判断</h2>
      <div class="example">
        <p>count 是 ref: {{ isRef(count) ? '是' : '否' }}</p>
        <p>state 是 reactive: {{ isReactive(state) ? '是' : '否' }}</p>
        <p>message 是 ref: {{ isRef(message) ? '是' : '否' }}</p>
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

.hint {
  color: #7f8c8d;
  font-size: 0.9rem;
  font-style: italic;
  margin-top: 0.5rem;
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
}

.comparison-item li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #42b983;
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
</style>
