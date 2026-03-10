<script setup lang="ts">
import { ref, reactive, watch, watchEffect } from 'vue'

// 1. watch 基础
const count = ref(0)
const watchLog = ref<string[]>([])

watch(count, (newValue, oldValue) => {
  watchLog.value.push(`count 从 ${oldValue} 变为 ${newValue}`)
})

// 2. 侦听多个源
const x = ref(0)
const y = ref(0)
const multiWatchLog = ref<string[]>([])

watch([x, y], ([newX, newY], [oldX, oldY]) => {
  multiWatchLog.value.push(`x: ${oldX} → ${newX}, y: ${oldY} → ${newY}`)
})

// 3. 深层侦听
const user = reactive({
  name: '张三',
  profile: {
    age: 25,
    city: '北京'
  }
})
const deepWatchLog = ref<string[]>([])

watch(user, (newValue) => {
  deepWatchLog.value.push(`user 对象发生变化: ${JSON.stringify(newValue)}`)
}, { deep: true })

// 4. immediate 选项
const message = ref('Hello')
const immediateLog = ref<string[]>([])

watch(message, (newValue) => {
  immediateLog.value.push(`message: ${newValue}`)
}, { immediate: true })

// 5. watchEffect
const firstName = ref('张')
const lastName = ref('三')
const watchEffectLog = ref<string[]>([])

watchEffect(() => {
  watchEffectLog.value.push(`全名: ${firstName.value}${lastName.value}`)
})

// 6. 停止侦听器
const autoCount = ref(0)
const stopWatchLog = ref<string[]>([])
let stopHandle: (() => void) | null = null

function startWatch() {
  if (stopHandle) return
  
  stopHandle = watch(autoCount, (newValue) => {
    stopWatchLog.value.push(`autoCount: ${newValue}`)
  })
  
  stopWatchLog.value.push('侦听器已启动')
}

function stopWatch() {
  if (stopHandle) {
    stopHandle()
    stopHandle = null
    stopWatchLog.value.push('侦听器已停止')
  }
}

// 7. 实际应用：搜索
const searchText = ref('')
const searchResults = ref<string[]>([])
const isSearching = ref(false)

const allItems = [
  'Vue.js', 'React', 'Angular', 'Svelte', 'Ember',
  'Backbone', 'Knockout', 'Polymer', 'Aurelia', 'Meteor'
]

watch(searchText, async (newValue) => {
  if (!newValue) {
    searchResults.value = []
    return
  }
  
  isSearching.value = true
  
  // 模拟 API 调用延迟
  await new Promise(resolve => setTimeout(resolve, 500))
  
  searchResults.value = allItems.filter(item =>
    item.toLowerCase().includes(newValue.toLowerCase())
  )
  
  isSearching.value = false
})

// 8. 回调的触发时机
const flushLog = ref<string[]>([])
const flushCount = ref(0)

watch(flushCount, () => {
  flushLog.value.push('watch 回调执行')
}, { flush: 'post' })

function clearLogs() {
  watchLog.value = []
  multiWatchLog.value = []
  deepWatchLog.value = []
  immediateLog.value = []
  watchEffectLog.value = []
  stopWatchLog.value = []
  flushLog.value = []
}
</script>

<template>
  <div class="container">
    <h1>11 - 侦听器</h1>

    <section class="demo-section">
      <h2>1. watch 基础</h2>
      <p>watch 函数用来侦听一个或多个响应式数据源，并在数据源变化时调用所给的回调函数</p>
      <div class="example">
        <p>计数: {{ count }}</p>
        <button @click="count++">增加</button>
        <button @click="count--">减少</button>
        
        <div class="log-box">
          <h4>侦听日志:</h4>
          <div v-for="(log, index) in watchLog" :key="index" class="log-item">
            {{ log }}
          </div>
        </div>
      </div>
      <div class="code-note">
        <code>watch(source, callback)</code> - 侦听单个数据源
      </div>
    </section>

    <section class="demo-section">
      <h2>2. 侦听多个源</h2>
      <p>可以用一个数组同时侦听多个源</p>
      <div class="example">
        <div class="input-group">
          <label>X: <input type="number" v-model.number="x"></label>
          <label>Y: <input type="number" v-model.number="y"></label>
        </div>
        
        <div class="log-box">
          <h4>侦听日志:</h4>
          <div v-for="(log, index) in multiWatchLog" :key="index" class="log-item">
            {{ log }}
          </div>
        </div>
      </div>
      <div class="code-note">
        <code>watch([x, y], callback)</code> - 侦听多个数据源
      </div>
    </section>

    <section class="demo-section">
      <h2>3. 深层侦听 (deep)</h2>
      <p>直接给 watch 传入一个响应式对象，会隐式地创建一个深层侦听器</p>
      <div class="example">
        <div class="input-group">
          <label>姓名: <input v-model="user.name"></label>
          <label>年龄: <input type="number" v-model.number="user.profile.age"></label>
          <label>城市: <input v-model="user.profile.city"></label>
        </div>
        
        <div class="log-box">
          <h4>侦听日志:</h4>
          <div v-for="(log, index) in deepWatchLog.slice(-3)" :key="index" class="log-item">
            {{ log }}
          </div>
        </div>
      </div>
      <div class="code-note">
        使用 <code>{ deep: true }</code> 选项强制深层侦听
      </div>
    </section>

    <section class="demo-section">
      <h2>4. 即时回调 (immediate)</h2>
      <p>watch 默认是懒执行的，使用 immediate 选项可以在创建侦听器时立即执行一次回调</p>
      <div class="example">
        <input v-model="message" placeholder="修改消息">
        
        <div class="log-box">
          <h4>侦听日志:</h4>
          <div v-for="(log, index) in immediateLog" :key="index" class="log-item">
            {{ log }}
          </div>
          <p class="hint">注意第一条日志是在组件创建时立即执行的</p>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>5. watchEffect</h2>
      <p>watchEffect 会立即执行一遍回调函数，并自动追踪回调中使用的响应式依赖</p>
      <div class="example">
        <div class="input-group">
          <label>姓: <input v-model="firstName"></label>
          <label>名: <input v-model="lastName"></label>
        </div>
        
        <div class="log-box">
          <h4>侦听日志:</h4>
          <div v-for="(log, index) in watchEffectLog" :key="index" class="log-item">
            {{ log }}
          </div>
        </div>
      </div>
      <div class="code-note">
        watchEffect 会自动追踪依赖，不需要显式指定侦听源
      </div>
    </section>

    <section class="demo-section">
      <h2>6. 停止侦听器</h2>
      <p>调用 watch 或 watchEffect 返回的函数可以停止侦听</p>
      <div class="example">
        <p>自动计数: {{ autoCount }}</p>
        <div class="button-group">
          <button @click="startWatch">启动侦听器</button>
          <button @click="stopWatch">停止侦听器</button>
          <button @click="autoCount++">增加计数</button>
        </div>
        
        <div class="log-box">
          <h4>侦听日志:</h4>
          <div v-for="(log, index) in stopWatchLog" :key="index" class="log-item">
            {{ log }}
          </div>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>7. 实际应用：搜索功能</h2>
      <p>使用 watch 实现实时搜索</p>
      <div class="example">
        <div class="search-box">
          <input 
            v-model="searchText" 
            placeholder="搜索框架..."
            class="search-input"
          >
          <div v-if="isSearching" class="searching">搜索中...</div>
        </div>
        
        <div class="search-results">
          <div v-if="searchResults.length > 0">
            <h4>搜索结果 ({{ searchResults.length }}):</h4>
            <div v-for="item in searchResults" :key="item" class="result-item">
              {{ item }}
            </div>
          </div>
          <div v-else-if="searchText && !isSearching" class="no-results">
            没有找到匹配的结果
          </div>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>8. watch vs watchEffect</h2>
      <div class="comparison">
        <div class="comparison-item">
          <h3>watch</h3>
          <ul>
            <li>需要明确指定侦听源</li>
            <li>可以访问新值和旧值</li>
            <li>默认懒执行</li>
            <li>更精确地控制何时触发</li>
          </ul>
        </div>
        <div class="comparison-item">
          <h3>watchEffect</h3>
          <ul>
            <li>自动追踪依赖</li>
            <li>无法访问旧值</li>
            <li>立即执行</li>
            <li>代码更简洁</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>9. 最佳实践</h2>
      <div class="best-practices">
        <div class="practice-item">
          <h3>✓ 避免在侦听器中修改被侦听的数据</h3>
          <p>可能导致无限循环</p>
        </div>
        <div class="practice-item">
          <h3>✓ 清理副作用</h3>
          <p>在组件卸载时停止侦听器，避免内存泄漏</p>
        </div>
        <div class="practice-item">
          <h3>✓ 使用防抖/节流</h3>
          <p>对于频繁触发的侦听器（如搜索），考虑使用防抖或节流</p>
        </div>
      </div>
    </section>

    <div class="clear-button">
      <button @click="clearLogs">清空所有日志</button>
    </div>
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
  margin-top: 0.5rem;
}

.log-box {
  margin-top: 1rem;
  padding: 1rem;
  background: #2c3e50;
  border-radius: 6px;
  max-height: 200px;
  overflow-y: auto;
}

.log-box h4 {
  color: #42b983;
  margin-bottom: 0.5rem;
  font-size: 1rem;
}

.log-item {
  color: #42b983;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
  padding: 0.25rem 0;
  border-bottom: 1px solid #34495e;
}

.log-item:last-child {
  border-bottom: none;
}

.input-group {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1rem;
}

.button-group {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 1rem;
}

.search-box {
  position: relative;
  margin-bottom: 1rem;
}

.search-input {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
}

.search-input:focus {
  outline: none;
  border-color: #42b983;
}

.searching {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #42b983;
  font-size: 0.9rem;
}

.search-results {
  min-height: 100px;
}

.search-results h4 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.result-item {
  padding: 0.75rem;
  background: #e8f5e9;
  border-radius: 4px;
  margin-bottom: 0.5rem;
  border-left: 3px solid #42b983;
}

.no-results {
  padding: 2rem;
  text-align: center;
  color: #7f8c8d;
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

.best-practices {
  display: flex;
  flex-direction: column;
  gap: 1rem;
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

.clear-button {
  text-align: center;
  margin-top: 2rem;
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
</style>
