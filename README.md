# Vue 3 教程项目集合

基于 Vue.js 官方中文文档的完整教程示例项目集合。每个项目对应一个核心概念，包含详细的示例代码和说明。

## 项目结构

```
vue_study/
├── 00-demo/                    # 初始模板项目
├── 01-快速开始/                # Vue 3 快速入门
├── 02-模板语法/                # 模板语法详解
├── 03-reactivity-fundamentals/ # 响应式基础
├── 04-computed/                # 计算属性
├── 05-class-and-style/         # Class 与 Style 绑定
├── 06-conditional/             # 条件渲染
├── 07-list/                    # 列表渲染
├── 08-event-handling/          # 事件处理
├── 09-form-input/              # 表单输入绑定
├── 10-lifecycle/               # 生命周期
├── 11-watchers/                # 侦听器
└── 12-components/              # 组件基础
```

## 学习路径

### 基础部分

1. **01-快速开始** - 了解 Vue 3 的基本概念
   - 声明式渲染
   - 响应式基础
   - Attribute 绑定
   - 事件监听

2. **02-模板语法** - 掌握模板语法
   - 文本插值 `{{ }}`
   - 原始 HTML `v-html`
   - Attribute 绑定 `v-bind` / `:`
   - JavaScript 表达式
   - 指令和修饰符

3. **03-响应式基础** - 理解响应式系统
   - `ref()` - 基本类型响应式
   - `reactive()` - 对象响应式
   - `toRefs()` / `toRef()`
   - 响应式判断

4. **04-计算属性** - 使用计算属性
   - 只读计算属性
   - 可写计算属性
   - 计算属性 vs 方法
   - 缓存机制

5. **05-类与样式绑定** - 动态样式
   - Class 对象语法
   - Class 数组语法
   - 内联样式绑定
   - 多重样式

### 核心功能

6. **06-条件渲染** - 条件显示内容
   - `v-if` / `v-else` / `v-else-if`
   - `v-show`
   - `v-if` vs `v-show`

7. **07-列表渲染** - 渲染列表
   - `v-for` 基础
   - 遍历数组和对象
   - `key` 的重要性
   - 数组变化侦测

8. **08-事件处理** - 处理用户交互
   - 监听事件 `v-on` / `@`
   - 事件修饰符
   - 按键修饰符
   - 系统按键修饰符

9. **09-表单输入绑定** - 表单处理
   - `v-model` 双向绑定
   - 各种表单元素
   - 修饰符 `.lazy` `.number` `.trim`

### 进阶概念

10. **10-生命周期** - 组件生命周期
    - `onMounted` / `onUpdated` / `onUnmounted`
    - 生命周期钩子的使用场景
    - 清理副作用

11. **11-侦听器** - 响应数据变化
    - `watch` 基础
    - 深层侦听
    - `watchEffect`
    - 停止侦听器

12. **12-组件基础** - 组件化开发
    - 定义和使用组件
    - Props 传递
    - 事件通信
    - 插槽 (Slots)

## 快速开始

### 安装所有项目的依赖

```bash
# 方法1: 逐个安装
cd 01-快速开始 && yarn install
cd ../02-模板语法 && yarn install
cd ../03-reactivity-fundamentals && yarn install
cd ../04-computed && yarn install
cd ../05-class-and-style && yarn install
cd ../06-conditional && yarn install
cd ../07-list && yarn install
cd ../08-event-handling && yarn install
cd ../09-form-input && yarn install
cd ../10-lifecycle && yarn install
cd ../11-watchers && yarn install
cd ../12-components && yarn install

# 方法2: 使用脚本批量安装（推荐）
# 在 vue_study 目录下执行
for dir in 01-* 02-* 03-* 04-* 05-* 06-* 07-* 08-* 09-* 10-* 11-* 12-*; do
  echo "Installing dependencies in $dir..."
  cd "$dir" && yarn install && cd ..
done
```

### 运行单个项目

```bash
# 进入任意项目目录
cd 01-快速开始

# 启动开发服务器
yarn dev

# 构建生产版本
yarn build
```

## 技术栈

- **Vue 3.5.29** - 渐进式 JavaScript 框架
- **TypeScript 5.9.3** - 类型安全
- **Vite 7.3.1** - 快速的开发构建工具
- **Vue DevTools** - 开发调试工具

## 项目特点

✅ **完整示例** - 每个概念都有完整的可运行示例  
✅ **中文注释** - 详细的中文注释和说明  
✅ **TypeScript** - 使用 TypeScript 提供类型安全  
✅ **最佳实践** - 遵循 Vue 3 官方推荐的最佳实践  
✅ **独立运行** - 每个项目都可以独立运行和学习  
✅ **渐进式学习** - 按照由浅入深的顺序组织

## 学习建议

1. **按顺序学习** - 建议按照项目编号顺序学习，每个概念都建立在前面的基础上
2. **动手实践** - 运行每个项目，修改代码，观察效果
3. **查看源码** - 仔细阅读 `src/App.vue` 中的示例代码和注释
4. **参考文档** - 每个项目的 README 都包含官方文档链接
5. **做笔记** - 记录重点和疑问，加深理解

## 常见问题

### 如何切换项目？

每个项目都是独立的，只需要：
1. 停止当前运行的项目（Ctrl+C）
2. 进入新的项目目录
3. 运行 `yarn dev`

### 端口冲突怎么办？

Vite 默认使用 5173 端口，如果端口被占用，会自动使用下一个可用端口。

### 如何查看更多示例？

每个项目的 `src/App.vue` 包含多个示例，建议完整阅读代码。

## 参考资源

- [Vue.js 官方文档（中文）](https://cn.vuejs.org/)
- [Vue.js 官方教程](https://cn.vuejs.org/tutorial/)
- [Vite 官方文档](https://cn.vitejs.dev/)
- [TypeScript 官方文档](https://www.typescriptlang.org/zh/)

## 下一步学习

完成这些基础教程后，可以继续学习：

- **组合式 API 深入** - 更高级的 Composition API 用法
- **组件进阶** - 组件通信、插槽、动态组件等
- **路由** - Vue Router 实现单页应用
- **状态管理** - Pinia 管理全局状态
- **工具链** - 构建工具、测试、部署等

## 许可证

本项目仅用于学习目的。

---

**开始学习 Vue 3 吧！🚀**
