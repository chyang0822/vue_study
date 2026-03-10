<script setup lang="ts">
import { ref, computed } from 'vue'

// 1. 基础计算属性
const firstName = ref('张')
const lastName = ref('三')

// 只读计算属性
const fullName = computed(() => {
  return firstName.value + lastName.value
})

// 2. 可写计算属性
const fullNameWritable = computed({
  get() {
    return firstName.value + lastName.value
  },
  set(newValue) {
    const names = newValue.split(' ')
    firstName.value = names[0] || ''
    lastName.value = names[1] || ''
  }
})

// 3. 计算属性 vs 方法
const count = ref(0)
const doubleCount = computed(() => {
  console.log('计算属性被计算')
  return count.value * 2
})

function getDoubleCount() {
  console.log('方法被调用')
  return count.value * 2
}

// 4. 购物车示例
const items = ref([
  { name: '苹果', price: 5, quantity: 3 },
  { name: '香蕉', price: 3, quantity: 5 },
  { name: '橙子', price: 4, quantity: 2 }
])

const totalPrice = computed(() => {
  return items.value.reduce((sum, item) => sum + item.price * item.quantity, 0)
})

const itemCount = computed(() => {
  return items.value.reduce((sum, item) => sum + item.quantity, 0)
})

// 5. 过滤和排序
const searchText = ref('')
const sortBy = ref('name')

const filteredItems = computed(() => {
  let result = items.value.filter(item => 
    item.name.includes(searchText.value)
  )
  
  if (sortBy.value === 'price') {
    result.sort((a, b) => a.price - b.price)
  } else if (sortBy.value === 'quantity') {
    result.sort((a, b) => a.quantity - b.quantity)
  }
  
  return result
})

// 方法
function addItem() {
  items.value.push({
    name: `商品${items.value.length + 1}`,
    price: Math.floor(Math.random() * 10) + 1,
    quantity: Math.floor(Math.random() * 5) + 1
  })
}

function removeItem(index: number) {
  items.value.splice(index, 1)
}
</script>

<template>
  <div class="container">
    <h1>04 - 计算属性</h1>

    <section class="demo-section">
      <h2>1. 基础计算属性</h2>
      <p>计算属性值会基于其响应式依赖被缓存，只有依赖发生改变时才会重新计算</p>
      <div class="example">
        <div>
          <label>姓: <input v-model="firstName"></label>
          <label style="margin-left: 1rem;">名: <input v-model="lastName"></label>
        </div>
        <p style="margin-top: 1rem;">全名: {{ fullName }}</p>
      </div>
      <div class="code-note">
        计算属性默认是只读的，返回一个计算属性 ref
      </div>
    </section>

    <section class="demo-section">
      <h2>2. 可写计算属性</h2>
      <p>可以通过提供 getter 和 setter 来创建可写的计算属性</p>
      <div class="example">
        <p>当前全名: {{ fullNameWritable }}</p>
        <input v-model="fullNameWritable" placeholder="输入全名（用空格分隔）">
        <p style="margin-top: 0.5rem;" class="hint">
          姓: {{ firstName }}, 名: {{ lastName }}
        </p>
      </div>
    </section>

    <section class="demo-section">
      <h2>3. 计算属性 vs 方法</h2>
      <p>计算属性会被缓存，而方法每次调用都会执行。打开控制台查看区别</p>
      <div class="example">
        <p>计数: {{ count }}</p>
        <button @click="count++">增加</button>
        
        <div style="margin-top: 1rem;">
          <p>计算属性（有缓存）: {{ doubleCount }}</p>
          <p>计算属性（再次访问）: {{ doubleCount }}</p>
          <p>方法调用: {{ getDoubleCount() }}</p>
          <p>方法调用（再次调用）: {{ getDoubleCount() }}</p>
        </div>
      </div>
      <div class="code-note">
        查看控制台：计算属性只计算一次，方法每次都执行
      </div>
    </section>

    <section class="demo-section">
      <h2>4. 购物车示例</h2>
      <p>使用计算属性自动计算总价和商品数量</p>
      <div class="example">
        <div class="cart-summary">
          <div class="summary-item">
            <span class="label">商品总数:</span>
            <span class="value">{{ itemCount }}</span>
          </div>
          <div class="summary-item">
            <span class="label">总价:</span>
            <span class="value">¥{{ totalPrice }}</span>
          </div>
        </div>
        
        <div class="cart-items">
          <div v-for="(item, index) in items" :key="index" class="cart-item">
            <span class="item-name">{{ item.name }}</span>
            <span class="item-detail">¥{{ item.price }} × {{ item.quantity }}</span>
            <span class="item-total">= ¥{{ item.price * item.quantity }}</span>
            <button @click="removeItem(index)" class="btn-remove">删除</button>
          </div>
        </div>
        
        <button @click="addItem" style="margin-top: 1rem;">添加商品</button>
      </div>
    </section>

    <section class="demo-section">
      <h2>5. 过滤和排序</h2>
      <p>使用计算属性实现列表的过滤和排序</p>
      <div class="example">
        <div class="filters">
          <input v-model="searchText" placeholder="搜索商品名称">
          <select v-model="sortBy">
            <option value="name">按名称排序</option>
            <option value="price">按价格排序</option>
            <option value="quantity">按数量排序</option>
          </select>
        </div>
        
        <div class="cart-items" style="margin-top: 1rem;">
          <div v-for="(item, index) in filteredItems" :key="index" class="cart-item">
            <span class="item-name">{{ item.name }}</span>
            <span class="item-detail">价格: ¥{{ item.price }}</span>
            <span class="item-detail">数量: {{ item.quantity }}</span>
          </div>
        </div>
        
        <p class="hint" style="margin-top: 1rem;">
          显示 {{ filteredItems.length }} / {{ items.length }} 个商品
        </p>
      </div>
    </section>

    <section class="demo-section">
      <h2>6. 最佳实践</h2>
      <div class="best-practices">
        <div class="practice-item">
          <h3>✓ Getter 不应有副作用</h3>
          <p>计算属性的 getter 应该只做计算而没有其他副作用</p>
        </div>
        <div class="practice-item">
          <h3>✓ 避免直接修改计算属性值</h3>
          <p>除非提供了 setter，否则不要尝试修改计算属性的值</p>
        </div>
        <div class="practice-item">
          <h3>✓ 计算属性 vs 方法</h3>
          <p>需要缓存时用计算属性，不需要缓存时用方法</p>
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
}

.cart-summary {
  display: flex;
  gap: 2rem;
  padding: 1rem;
  background: #e8f5e9;
  border-radius: 6px;
  margin-bottom: 1rem;
}

.summary-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.summary-item .label {
  color: #5a6c7d;
  font-size: 0.9rem;
}

.summary-item .value {
  font-size: 1.5rem;
  font-weight: bold;
  color: #42b983;
}

.cart-items {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.cart-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.75rem;
  background: #f8f9fa;
  border-radius: 4px;
  border: 1px solid #e1e8ed;
}

.item-name {
  font-weight: bold;
  min-width: 80px;
}

.item-detail {
  color: #5a6c7d;
}

.item-total {
  margin-left: auto;
  font-weight: bold;
  color: #42b983;
}

.btn-remove {
  background: #e74c3c;
  padding: 0.25rem 0.75rem;
  font-size: 0.9rem;
}

.btn-remove:hover {
  background: #c0392b;
}

.filters {
  display: flex;
  gap: 1rem;
}

.filters input,
.filters select {
  flex: 1;
}

.best-practices {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 1rem;
}

.practice-item {
  background: white;
  padding: 1rem;
  border-radius: 6px;
  border: 1px solid #e1e8ed;
}

.practice-item h3 {
  color: #42b983;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.practice-item p {
  color: #5a6c7d;
  margin: 0;
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

input,
select {
  padding: 0.5rem;
  border: 2px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

input:focus,
select:focus {
  outline: none;
  border-color: #42b983;
}

label {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}
</style>
