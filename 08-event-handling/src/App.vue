<script setup lang="ts">
import { ref } from 'vue'

// 1. 监听事件
const count = ref(0)

// 2. 内联事件处理器
const message = ref('')

// 3. 方法事件处理器
function greet(event: Event) {
  alert(`Hello! 事件类型: ${event.type}`)
}

function say(msg: string) {
  alert(msg)
}

// 4. 在内联处理器中访问事件对象
function warn(msg: string, event: Event) {
  if (event) {
    event.preventDefault()
  }
  alert(msg)
}

// 5. 事件修饰符示例
const clickCount = ref(0)
const submitCount = ref(0)

function handleClick() {
  clickCount.value++
}

function handleSubmit() {
  submitCount.value++
  alert('表单已提交！')
}

// 6. 按键修饰符
const keyInput = ref('')
const enterPressed = ref(0)
const ctrlEnterPressed = ref(0)

function onEnter() {
  enterPressed.value++
}

function onCtrlEnter() {
  ctrlEnterPressed.value++
}

// 7. 鼠标按键修饰符
const leftClicks = ref(0)
const rightClicks = ref(0)
const middleClicks = ref(0)
</script>

<template>
  <div class="container">
    <h1>08 - 事件处理</h1>

    <section class="demo-section">
      <h2>1. 监听事件 (v-on / @)</h2>
      <p>使用 v-on 指令（简写为 @）来监听 DOM 事件</p>
      <div class="example">
        <p>计数: {{ count }}</p>
        <button @click="count++">增加 1</button>
        <button @click="count--">减少 1</button>
        <button @click="count = 0">重置</button>
      </div>
      <div class="code-note">
        <code>v-on:click</code> 可以简写为 <code>@click</code>
      </div>
    </section>

    <section class="demo-section">
      <h2>2. 内联事件处理器</h2>
      <p>直接在模板中编写 JavaScript 语句</p>
      <div class="example">
        <input v-model="message" placeholder="输入消息">
        <button @click="alert(message || '没有消息')">显示消息</button>
      </div>
    </section>

    <section class="demo-section">
      <h2>3. 方法事件处理器</h2>
      <p>指向组件上定义的方法</p>
      <div class="example">
        <button @click="greet">问候</button>
        <button @click="say('你好')">说你好</button>
        <button @click="say('再见')">说再见</button>
      </div>
    </section>

    <section class="demo-section">
      <h2>4. 在内联处理器中访问事件对象</h2>
      <p>使用特殊的 $event 变量或使用箭头函数</p>
      <div class="example">
        <button @click="warn('警告信息', $event)">
          使用 $event
        </button>
        <button @click="(event) => warn('另一个警告', event)">
          使用箭头函数
        </button>
      </div>
    </section>

    <section class="demo-section">
      <h2>5. 事件修饰符</h2>
      <p>Vue 为 v-on 提供了事件修饰符，用点表示的指令后缀</p>
      
      <div class="example">
        <h3>.stop - 阻止事件冒泡</h3>
        <div @click="handleClick" class="outer-box">
          外层 (点击次数: {{ clickCount }})
          <button @click.stop="handleClick" class="inner-button">
            内层按钮 (阻止冒泡)
          </button>
        </div>
      </div>

      <div class="example">
        <h3>.prevent - 阻止默认行为</h3>
        <form @submit.prevent="handleSubmit">
          <input type="text" placeholder="输入内容">
          <button type="submit">提交 (阻止页面刷新)</button>
        </form>
        <p>提交次数: {{ submitCount }}</p>
      </div>

      <div class="example">
        <h3>.once - 只触发一次</h3>
        <button @click.once="alert('只会触发一次！')">
          点击我（只触发一次）
        </button>
      </div>

      <div class="example">
        <h3>.self - 只在事件从元素本身触发时才触发</h3>
        <div @click.self="handleClick" class="outer-box">
          只有点击这个区域才会触发 ({{ clickCount }})
          <button class="inner-button">点击我不会触发外层</button>
        </div>
      </div>

      <div class="info-box">
        <h4>修饰符可以链式调用</h4>
        <p><code>@click.stop.prevent</code> - 同时阻止冒泡和默认行为</p>
        <p><code>@click.prevent.self</code> - 只在点击元素本身时阻止默认行为</p>
      </div>
    </section>

    <section class="demo-section">
      <h2>6. 按键修饰符</h2>
      <p>监听键盘事件时，可以使用按键修饰符</p>
      
      <div class="example">
        <h3>.enter - 回车键</h3>
        <input 
          v-model="keyInput" 
          @keyup.enter="onEnter"
          placeholder="按回车键"
        >
        <p>回车次数: {{ enterPressed }}</p>
      </div>

      <div class="example">
        <h3>组合按键 - Ctrl + Enter</h3>
        <input 
          v-model="keyInput" 
          @keyup.ctrl.enter="onCtrlEnter"
          placeholder="按 Ctrl + Enter"
        >
        <p>Ctrl+Enter 次数: {{ ctrlEnterPressed }}</p>
      </div>

      <div class="info-box">
        <h4>常用按键修饰符</h4>
        <ul>
          <li><code>.enter</code> - 回车键</li>
          <li><code>.tab</code> - Tab 键</li>
          <li><code>.delete</code> - 删除/退格键</li>
          <li><code>.esc</code> - Esc 键</li>
          <li><code>.space</code> - 空格键</li>
          <li><code>.up / .down / .left / .right</code> - 方向键</li>
        </ul>
      </div>
    </section>

    <section class="demo-section">
      <h2>7. 系统按键修饰符</h2>
      <div class="info-box">
        <h4>系统修饰键</h4>
        <ul>
          <li><code>.ctrl</code> - Ctrl 键</li>
          <li><code>.alt</code> - Alt 键</li>
          <li><code>.shift</code> - Shift 键</li>
          <li><code>.meta</code> - Meta 键（Mac 的 Command 键，Windows 的徽标键）</li>
        </ul>
        <p style="margin-top: 0.5rem;">示例: <code>@click.ctrl</code> - 只在按住 Ctrl 时触发</p>
      </div>
    </section>

    <section class="demo-section">
      <h2>8. 鼠标按键修饰符</h2>
      <p>限制处理程序监听特定鼠标按键触发的事件</p>
      <div class="example">
        <div 
          class="mouse-box"
          @click.left="leftClicks++"
          @click.right.prevent="rightClicks++"
          @click.middle.prevent="middleClicks++"
        >
          <p>左键点击: {{ leftClicks }}</p>
          <p>右键点击: {{ rightClicks }}</p>
          <p>中键点击: {{ middleClicks }}</p>
          <p class="hint">在这个区域尝试不同的鼠标按键</p>
        </div>
      </div>
      <div class="info-box">
        <ul>
          <li><code>.left</code> - 鼠标左键</li>
          <li><code>.right</code> - 鼠标右键</li>
          <li><code>.middle</code> - 鼠标中键</li>
        </ul>
      </div>
    </section>

    <section class="demo-section">
      <h2>9. .exact 修饰符</h2>
      <div class="info-box">
        <p><code>.exact</code> 修饰符允许控制触发事件所需的确定组合的系统按键修饰符</p>
        <div class="code-example">
          <p><code>@click.ctrl</code> - 按住 Ctrl 时点击（可以同时按其他键）</p>
          <p><code>@click.ctrl.exact</code> - 只按住 Ctrl 时点击（不能按其他键）</p>
          <p><code>@click.exact</code> - 没有按任何系统键时点击</p>
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
}

.outer-box {
  background: #e8f5e9;
  padding: 2rem;
  border-radius: 6px;
  border: 2px solid #42b983;
  cursor: pointer;
  text-align: center;
}

.inner-button {
  margin-top: 1rem;
}

.mouse-box {
  background: #e3f2fd;
  padding: 2rem;
  border-radius: 6px;
  border: 2px dashed #2196f3;
  text-align: center;
  cursor: pointer;
  user-select: none;
}

.info-box {
  background: #e3f2fd;
  padding: 1rem;
  border-radius: 6px;
  border-left: 3px solid #2196f3;
  margin-top: 1rem;
}

.info-box h4 {
  color: #1565c0;
  margin-bottom: 0.5rem;
}

.info-box p {
  color: #1565c0;
  margin: 0.25rem 0;
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

.code-example {
  background: #fff;
  padding: 0.75rem;
  border-radius: 4px;
  margin-top: 0.5rem;
}

.code-example p {
  margin: 0.25rem 0;
}

.code-example code {
  color: #e83e8c;
  font-family: 'Courier New', monospace;
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
  margin-bottom: 0.5rem;
  transition: background 0.3s;
}

button:hover {
  background: #35a372;
}

input[type="text"] {
  padding: 0.5rem;
  border: 2px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  margin-right: 0.5rem;
  width: 300px;
}

input[type="text"]:focus {
  outline: none;
  border-color: #42b983;
}

form {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}
</style>
