# Vue 3 教程 - 快速启动指南

## 🚀 快速开始

### 1. 安装依赖

选择以下任一方式安装所有项目的依赖：

#### 方式一：使用安装脚本（推荐）

```bash
# 在 vue_study 目录下执行
./install-all.sh
```

#### 方式二：手动批量安装

```bash
# 在 vue_study 目录下执行
for dir in 01-* 02-* 03-* 04-* 05-* 06-* 07-* 08-* 09-* 10-* 11-* 12-*; do
  echo "Installing $dir..."
  cd "$dir" && yarn install && cd ..
done
```

#### 方式三：逐个安装

```bash
cd 01-快速开始 && yarn install
cd ../02-模板语法 && yarn install
# ... 依此类推
```

### 2. 运行项目

```bash
# 进入任意项目目录
cd 01-快速开始

# 启动开发服务器
yarn dev

# 浏览器会自动打开 http://localhost:5173
```

### 3. 学习路径

按照以下顺序学习效果最佳：

```
01-快速开始 → 02-模板语法 → 03-响应式基础 → 04-计算属性
    ↓
05-类与样式绑定 → 06-条件渲染 → 07-列表渲染
    ↓
08-事件处理 → 09-表单输入绑定
    ↓
10-生命周期 → 11-侦听器 → 12-组件基础
```

## 📚 项目列表

| 编号 | 项目名称 | 学习内容 | 难度 |
|------|---------|---------|------|
| 01 | 快速开始 | 声明式渲染、响应式、事件监听 | ⭐ |
| 02 | 模板语法 | 插值、指令、表达式、修饰符 | ⭐ |
| 03 | 响应式基础 | ref、reactive、toRefs | ⭐⭐ |
| 04 | 计算属性 | computed、缓存机制 | ⭐⭐ |
| 05 | 类与样式绑定 | 动态 class、动态 style | ⭐⭐ |
| 06 | 条件渲染 | v-if、v-show、条件判断 | ⭐ |
| 07 | 列表渲染 | v-for、key、数组方法 | ⭐⭐ |
| 08 | 事件处理 | 事件监听、修饰符、按键 | ⭐⭐ |
| 09 | 表单输入绑定 | v-model、表单元素 | ⭐⭐ |
| 10 | 生命周期 | 生命周期钩子、副作用清理 | ⭐⭐⭐ |
| 11 | 侦听器 | watch、watchEffect | ⭐⭐⭐ |
| 12 | 组件基础 | Props、事件、插槽 | ⭐⭐⭐ |

## 💡 学习建议

### 每个项目的学习步骤

1. **阅读 README** - 了解学习目标
2. **运行项目** - 启动开发服务器，查看效果
3. **阅读代码** - 仔细阅读 `src/App.vue` 中的示例
4. **动手修改** - 尝试修改代码，观察变化
5. **做笔记** - 记录重点和疑问
6. **查阅文档** - 参考官方文档深入理解

### 实践建议

- ✅ 每个示例都运行一遍
- ✅ 尝试修改参数和逻辑
- ✅ 打开浏览器开发者工具观察
- ✅ 使用 Vue DevTools 调试
- ✅ 完成后尝试自己实现类似功能

## 🛠️ 常用命令

```bash
# 启动开发服务器
yarn dev

# 构建生产版本
yarn build

# 预览生产构建
yarn preview

# 类型检查
yarn type-check
```

## 📖 参考资源

- [Vue.js 官方文档](https://cn.vuejs.org/)
- [Vue.js 官方教程](https://cn.vuejs.org/tutorial/)
- [Composition API 文档](https://cn.vuejs.org/guide/extras/composition-api-faq.html)
- [Vue DevTools](https://devtools.vuejs.org/)

## ❓ 常见问题

### Q: 如何在项目间切换？

A: 停止当前项目（Ctrl+C），进入新项目目录，运行 `yarn dev`

### Q: 端口被占用怎么办？

A: Vite 会自动使用下一个可用端口（5174、5175...）

### Q: 如何查看更多示例？

A: 每个项目的 `src/App.vue` 包含多个详细示例

### Q: TypeScript 报错怎么办？

A: 确保已安装依赖，运行 `yarn type-check` 检查类型错误

## 🎯 学习目标

完成所有项目后，你将掌握：

- ✅ Vue 3 核心概念和 API
- ✅ 组合式 API (Composition API)
- ✅ 响应式系统原理
- ✅ 组件化开发思想
- ✅ TypeScript 在 Vue 中的应用
- ✅ 现代前端开发工作流

## 🚀 下一步

学完基础后，继续学习：

1. **Vue Router** - 单页应用路由
2. **Pinia** - 状态管理
3. **组件库** - Element Plus、Ant Design Vue
4. **构建工具** - Vite 深入、打包优化
5. **测试** - Vitest、Vue Test Utils

---

**祝学习愉快！💪**
