<script setup lang="ts">
import { ref } from 'vue'
import ButtonCounter from './components/ButtonCounter.vue'
import AlertBox from './components/AlertBox.vue'
import BlogPost from './components/BlogPost.vue'
import TabButton from './components/TabButton.vue'

// 1. 组件使用
const message = ref('Hello from Parent!')

// 2. Props 传递
const posts = ref([
  { id: 1, title: 'Vue 3 入门教程', author: '张三' },
  { id: 2, title: 'Composition API 详解', author: '李四' },
  { id: 3, title: '响应式系统原理', author: '王五' }
])

// 3. 监听事件
const notifications = ref<string[]>([])

function handleIncrement(count: number) {
  notifications.value.push(`按钮被点击了 ${count} 次`)
}

function handlePostClick(title: string) {
  notifications.value.push(`点击了文章: ${title}`)
}

// 4. 动态组件
const currentTab = ref('home')
const tabs = ['home', 'posts', 'archive']
</script>

<template>
  <div class="container">
    <h1>12 - 组件基础</h1>

    <section class="demo-section">
      <h2>1. 定义和使用组件</h2>
      <p>组件允许我们将 UI 划分为独立、可复用的部分</p>
      <div class="example">
        <h3>使用 ButtonCounter 组件</h3>
        <ButtonCounter />
        <ButtonCounter />
        <ButtonCounter />
        <p class="hint">每个组件都维护着自己的状态</p>
      </div>
      <div class="code-note">
        组件是可复用的 Vue 实例，拥有自己的数据、方法和生命周期
      </div>
    </section>

    <section class="demo-section">
      <h2>2. Props - 父传子</h2>
      <p>Props 是组件的自定义属性，用于从父组件向子组件传递数据</p>
      <div class="example">
        <h3>博客文章列表</h3>
        <BlogPost
          v-for="post in posts"
          :key="post.id"
          :title="post.title"
          :author="post.author"
          @click="handlePostClick"
        />
      </div>
      <div class="code-note">
        使用 <code>:prop-name</code> 语法传递动态 props
      </div>
    </section>

    <section class="demo-section">
      <h2>3. 监听事件 - 子传父</h2>
      <p>子组件可以通过 emit 触发事件，父组件通过 @ 监听</p>
      <div class="example">
        <h3>计数器组件（带事件）</h3>
        <ButtonCounter @increment="handleIncrement" />
        
        <div v-if="notifications.length > 0" class="notifications">
          <h4>通知:</h4>
          <div v-for="(notif, index) in notifications.slice(-5)" :key="index" class="notification">
            {{ notif }}
          </div>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>4. 插槽 (Slots)</h2>
      <p>插槽允许父组件向子组件传递模板内容</p>
      <div class="example">
        <AlertBox type="success">
          <strong>成功!</strong> 操作已完成。
        </AlertBox>
        
        <AlertBox type="warning">
          <strong>警告!</strong> 请注意这个操作。
        </AlertBox>
        
        <AlertBox type="error">
          <strong>错误!</strong> 操作失败，请重试。
        </AlertBox>
      </div>
      <div class="code-note">
        使用 <code>&lt;slot&gt;</code> 标签定义插槽位置
      </div>
    </section>

    <section class="demo-section">
      <h2>5. 动态组件</h2>
      <p>使用 component 元素和 :is 属性来动态切换组件</p>
      <div class="example">
        <div class="tabs">
          <button
            v-for="tab in tabs"
            :key="tab"
            :class="{ active: currentTab === tab }"
            @click="currentTab = tab"
          >
            {{ tab }}
          </button>
        </div>
        
        <div class="tab-content">
          <component :is="currentTab === 'home' ? 'div' : currentTab === 'posts' ? 'div' : 'div'">
            <div v-if="currentTab === 'home'">
              <h3>首页</h3>
              <p>欢迎来到首页！</p>
            </div>
            <div v-else-if="currentTab === 'posts'">
              <h3>文章</h3>
              <BlogPost
                v-for="post in posts"
                :key="post.id"
                :title="post.title"
                :author="post.author"
              />
            </div>
            <div v-else>
              <h3>归档</h3>
              <p>这里是归档内容。</p>
            </div>
          </component>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>6. 组件注册</h2>
      <div class="info-box">
        <h4>全局注册 vs 局部注册</h4>
        <div class="comparison-grid">
          <div>
            <h5>全局注册</h5>
            <ul>
              <li>在 main.ts 中使用 app.component()</li>
              <li>可以在任何组件中使用</li>
              <li>会增加打包体积</li>
            </ul>
          </div>
          <div>
            <h5>局部注册（推荐）</h5>
            <ul>
              <li>在组件中直接 import</li>
              <li>只在当前组件可用</li>
              <li>支持 Tree-shaking</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>7. 组件通信方式总结</h2>
      <div class="communication-methods">
        <div class="method-item">
          <h4>1. Props（父 → 子）</h4>
          <p>通过属性传递数据</p>
        </div>
        <div class="method-item">
          <h4>2. Events（子 → 父）</h4>
          <p>通过事件传递消息</p>
        </div>
        <div class="method-item">
          <h4>3. Slots（父 → 子）</h4>
          <p>传递模板内容</p>
        </div>
        <div class="method-item">
          <h4>4. Provide/Inject（祖先 → 后代）</h4>
          <p>跨层级传递数据</p>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>8. 最佳实践</h2>
      <div class="best-practices">
        <div class="practice-item">
          <h3>✓ 单一职责原则</h3>
          <p>每个组件应该只负责一个功能</p>
        </div>
        <div class="practice-item">
          <h3>✓ Props 验证</h3>
          <p>为 props 定义类型和验证规则</p>
        </div>
        <div class="practice-item">
          <h3>✓ 命名规范</h3>
          <p>组件名使用 PascalCase，事件名使用 kebab-case</p>
        </div>
        <div class="practice-item">
          <h3>✓ 避免直接修改 Props</h3>
          <p>Props 是单向数据流，不应在子组件中修改</p>
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
  margin-top: 1rem;
}

.notifications {
  margin-top: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 6px;
}

.notifications h4 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.notification {
  padding: 0.5rem;
  background: #e8f5e9;
  border-left: 3px solid #42b983;
  border-radius: 4px;
  margin-bottom: 0.5rem;
}

.tabs {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
  border-bottom: 2px solid #e1e8ed;
  padding-bottom: 0.5rem;
}

.tabs button {
  background: transparent;
  color: #5a6c7d;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  font-size: 1rem;
  border-radius: 4px 4px 0 0;
  transition: all 0.3s;
}

.tabs button:hover {
  background: #f8f9fa;
}

.tabs button.active {
  background: #42b983;
  color: white;
}

.tab-content {
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 6px;
  min-height: 200px;
}

.info-box {
  background: #e3f2fd;
  padding: 1rem;
  border-radius: 6px;
  border-left: 3px solid #2196f3;
}

.info-box h4 {
  color: #1565c0;
  margin-bottom: 1rem;
}

.comparison-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.comparison-grid h5 {
  color: #1565c0;
  margin-bottom: 0.5rem;
}

.comparison-grid ul {
  list-style: none;
  padding: 0;
}

.comparison-grid li {
  padding: 0.25rem 0;
  padding-left: 1.5rem;
  position: relative;
  color: #1565c0;
}

.comparison-grid li::before {
  content: '•';
  position: absolute;
  left: 0;
  font-weight: bold;
}

.communication-methods {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.method-item {
  background: white;
  padding: 1rem;
  border-radius: 6px;
  border: 1px solid #e1e8ed;
}

.method-item h4 {
  color: #42b983;
  margin-bottom: 0.5rem;
  font-size: 1rem;
}

.method-item p {
  color: #5a6c7d;
  margin: 0;
  font-size: 0.9rem;
}

.best-practices {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
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
</style>
