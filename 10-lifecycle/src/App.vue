<script setup lang="ts">
import { ref, onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted } from 'vue'

// 生命周期日志
const logs = ref<string[]>([])
const count = ref(0)
const showChild = ref(true)

// 定时器示例
const timer = ref(0)
let intervalId: number | null = null

function addLog(message: string) {
  const timestamp = new Date().toLocaleTimeString()
  logs.value.push(`[${timestamp}] ${message}`)
}

// 生命周期钩子
onBeforeMount(() => {
  addLog('onBeforeMount: 组件挂载前')
})

onMounted(() => {
  addLog('onMounted: 组件已挂载到 DOM')
  
  // 启动定时器
  intervalId = window.setInterval(() => {
    timer.value++
  }, 1000)
})

onBeforeUpdate(() => {
  addLog('onBeforeUpdate: 组件更新前')
})

onUpdated(() => {
  addLog('onUpdated: 组件已更新')
})

onBeforeUnmount(() => {
  addLog('onBeforeUnmount: 组件卸载前')
  
  // 清理定时器
  if (intervalId) {
    clearInterval(intervalId)
  }
})

onUnmounted(() => {
  addLog('onUnmounted: 组件已卸载')
})

function clearLogs() {
  logs.value = []
}
</script>

<template>
  <div class="container">
    <h1>10 - 生命周期</h1>

    <section class="demo-section">
      <h2>1. 生命周期概述</h2>
      <div class="info-box">
        <p>每个 Vue 组件实例在创建时都需要经历一系列的初始化步骤，在此过程中会运行被称为生命周期钩子的函数。</p>
        <h4 style="margin-top: 1rem;">主要生命周期钩子：</h4>
        <ul>
          <li><strong>onBeforeMount</strong> - 在组件被挂载之前调用</li>
          <li><strong>onMounted</strong> - 在组件被挂载之后调用</li>
          <li><strong>onBeforeUpdate</strong> - 在组件即将因为响应式状态变更而更新其 DOM 树之前调用</li>
          <li><strong>onUpdated</strong> - 在组件因为响应式状态变更而更新其 DOM 树之后调用</li>
          <li><strong>onBeforeUnmount</strong> - 在组件实例被卸载之前调用</li>
          <li><strong>onUnmounted</strong> - 在组件实例被卸载之后调用</li>
        </ul>
      </div>
    </section>

    <section class="demo-section">
      <h2>2. 生命周期日志</h2>
      <p>观察组件生命周期的执行顺序</p>
      <div class="example">
        <div class="log-container">
          <div v-for="(log, index) in logs" :key="index" class="log-item">
            {{ log }}
          </div>
          <div v-if="logs.length === 0" class="log-empty">
            暂无日志
          </div>
        </div>
        <button @click="clearLogs">清空日志</button>
      </div>
    </section>

    <section class="demo-section">
      <h2>3. 触发更新</h2>
      <p>修改响应式数据会触发 onBeforeUpdate 和 onUpdated</p>
      <div class="example">
        <p>计数: {{ count }}</p>
        <button @click="count++">增加计数（触发更新）</button>
      </div>
      <div class="code-note">
        每次点击按钮都会触发组件更新，查看日志中的 onBeforeUpdate 和 onUpdated
      </div>
    </section>

    <section class="demo-section">
      <h2>4. onMounted 实际应用</h2>
      <p>onMounted 常用于：DOM 操作、启动定时器、发送 API 请求等</p>
      <div class="example">
        <div class="timer-display">
          <h3>定时器运行时间</h3>
          <p class="timer">{{ timer }} 秒</p>
          <p class="hint">定时器在 onMounted 中启动，在 onBeforeUnmount 中清理</p>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>5. 子组件生命周期</h2>
      <p>观察子组件的挂载和卸载</p>
      <div class="example">
        <button @click="showChild = !showChild">
          {{ showChild ? '卸载' : '挂载' }}子组件
        </button>
        
        <ChildComponent v-if="showChild" @log="addLog" />
      </div>
      <div class="code-note">
        切换子组件的显示状态，观察 onBeforeUnmount 和 onUnmounted 的执行
      </div>
    </section>

    <section class="demo-section">
      <h2>6. 生命周期图示</h2>
      <div class="lifecycle-diagram">
        <div class="lifecycle-stage">
          <div class="stage-box creation">创建阶段</div>
          <div class="hook-box">onBeforeMount</div>
          <div class="hook-box">onMounted</div>
        </div>
        <div class="lifecycle-arrow">↓</div>
        <div class="lifecycle-stage">
          <div class="stage-box update">更新阶段</div>
          <div class="hook-box">onBeforeUpdate</div>
          <div class="hook-box">onUpdated</div>
        </div>
        <div class="lifecycle-arrow">↓</div>
        <div class="lifecycle-stage">
          <div class="stage-box unmount">卸载阶段</div>
          <div class="hook-box">onBeforeUnmount</div>
          <div class="hook-box">onUnmounted</div>
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>7. 最佳实践</h2>
      <div class="best-practices">
        <div class="practice-item">
          <h3>✓ 在 onMounted 中进行 DOM 操作</h3>
          <p>此时组件已经挂载到 DOM，可以安全地访问 DOM 元素</p>
        </div>
        <div class="practice-item">
          <h3>✓ 在 onBeforeUnmount 中清理副作用</h3>
          <p>清理定时器、取消网络请求、移除事件监听器等</p>
        </div>
        <div class="practice-item">
          <h3>✓ 避免在 onUpdated 中修改状态</h3>
          <p>可能导致无限更新循环</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onBeforeMount, onMounted, onBeforeUnmount, onUnmounted } from 'vue'

// 子组件
const ChildComponent = defineComponent({
  name: 'ChildComponent',
  emits: ['log'],
  setup(props, { emit }) {
    const childCount = ref(0)

    onBeforeMount(() => {
      emit('log', '子组件 onBeforeMount')
    })

    onMounted(() => {
      emit('log', '子组件 onMounted')
    })

    onBeforeUnmount(() => {
      emit('log', '子组件 onBeforeUnmount')
    })

    onUnmounted(() => {
      emit('log', '子组件 onUnmounted')
    })

    return { childCount }
  },
  template: `
    <div class="child-component">
      <h3>子组件</h3>
      <p>子组件计数: {{ childCount }}</p>
      <button @click="childCount++">增加子组件计数</button>
    </div>
  `
})

export default {
  components: {
    ChildComponent
  }
}
</script>

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

.info-box {
  background: #e3f2fd;
  padding: 1rem;
  border-radius: 6px;
  border-left: 3px solid #2196f3;
}

.info-box p {
  color: #1565c0;
  margin: 0;
}

.info-box h4 {
  color: #1565c0;
  margin-bottom: 0.5rem;
}

.info-box ul {
  list-style: none;
  padding: 0;
  margin-top: 0.5rem;
}

.info-box li {
  padding: 0.25rem 0;
  padding-left: 1.5rem;
  position: relative;
  color: #1565c0;
}

.info-box li::before {
  content: '•';
  position: absolute;
  left: 0;
  font-weight: bold;
}

.log-container {
  background: #2c3e50;
  color: #42b983;
  padding: 1rem;
  border-radius: 6px;
  max-height: 300px;
  overflow-y: auto;
  margin-bottom: 1rem;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
}

.log-item {
  padding: 0.25rem 0;
  border-bottom: 1px solid #34495e;
}

.log-item:last-child {
  border-bottom: none;
}

.log-empty {
  color: #7f8c8d;
  text-align: center;
  padding: 2rem;
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

.timer-display {
  text-align: center;
  padding: 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 8px;
  color: white;
}

.timer-display h3 {
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.timer {
  font-size: 3rem;
  font-weight: bold;
  margin: 1rem 0;
}

.child-component {
  margin-top: 1rem;
  padding: 1.5rem;
  background: #e8f5e9;
  border-radius: 6px;
  border: 2px solid #42b983;
}

.child-component h3 {
  color: #42b983;
  margin-bottom: 0.5rem;
}

.lifecycle-diagram {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  background: white;
  border-radius: 6px;
}

.lifecycle-stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  width: 100%;
  max-width: 300px;
}

.stage-box {
  padding: 1rem 2rem;
  border-radius: 6px;
  color: white;
  font-weight: bold;
  width: 100%;
  text-align: center;
}

.stage-box.creation {
  background: #42b983;
}

.stage-box.update {
  background: #3498db;
}

.stage-box.unmount {
  background: #e74c3c;
}

.hook-box {
  padding: 0.75rem 1.5rem;
  background: #f8f9fa;
  border: 2px solid #e1e8ed;
  border-radius: 4px;
  width: 100%;
  text-align: center;
  font-family: 'Courier New', monospace;
  color: #2c3e50;
}

.lifecycle-arrow {
  font-size: 2rem;
  color: #7f8c8d;
  margin: 0.5rem 0;
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
</style>
