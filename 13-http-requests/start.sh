#!/bin/bash

# 13-HTTP请求项目启动脚本

echo "======================================"
echo "13-HTTP请求项目启动"
echo "======================================"
echo ""

# 检查是否在正确的目录
if [ ! -f "package.json" ]; then
    echo "❌ 错误：请在项目根目录运行此脚本"
    exit 1
fi

# 检查 Python 是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误：未找到 Python 3"
    echo "请先安装 Python 3.8 或更高版本"
    exit 1
fi

# 检查后端依赖
if [ ! -d "backend/__pycache__" ] && [ ! -f "backend/.installed" ]; then
    echo "📦 首次运行，正在安装后端依赖..."
    cd backend
    pip install -r requirements.txt
    touch .installed
    cd ..
    echo "✅ 后端依赖安装完成"
    echo ""
fi

# 检查前端依赖
if [ ! -d "node_modules" ]; then
    echo "📦 正在安装前端依赖..."
    yarn install
    echo "✅ 前端依赖安装完成"
    echo ""
fi

echo "🚀 启动服务..."
echo ""
echo "后端服务: http://localhost:8000"
echo "前端服务: http://localhost:5173"
echo "API 文档: http://localhost:8000/docs"
echo ""
echo "按 Ctrl+C 停止所有服务"
echo ""

# 启动后端（后台运行）
cd backend
python3 -m uvicorn main:app --reload &
BACKEND_PID=$!
cd ..

# 等待后端启动
sleep 2

# 启动前端
yarn dev &
FRONTEND_PID=$!

# 捕获退出信号
trap "echo ''; echo '正在停止服务...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT TERM

# 等待
wait
