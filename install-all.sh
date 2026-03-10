#!/bin/bash

# Vue 3 教程项目 - 批量安装依赖脚本

echo "======================================"
echo "Vue 3 教程项目 - 批量安装依赖"
echo "======================================"
echo ""

# 项目列表
projects=(
  "01-快速开始"
  "02-模板语法"
  "03-reactivity-fundamentals"
  "04-computed"
  "05-class-and-style"
  "06-conditional"
  "07-list"
  "08-event-handling"
  "09-form-input"
  "10-lifecycle"
  "11-watchers"
  "12-components"
)

# 计数器
total=${#projects[@]}
current=0
success=0
failed=0

# 遍历安装
for project in "${projects[@]}"; do
  current=$((current + 1))
  echo "[$current/$total] 正在安装 $project 的依赖..."
  
  if [ -d "$project" ]; then
    cd "$project"
    
    if yarn install --silent; then
      echo "✓ $project 安装成功"
      success=$((success + 1))
    else
      echo "✗ $project 安装失败"
      failed=$((failed + 1))
    fi
    
    cd ..
  else
    echo "✗ 目录 $project 不存在"
    failed=$((failed + 1))
  fi
  
  echo ""
done

# 总结
echo "======================================"
echo "安装完成！"
echo "======================================"
echo "总计: $total 个项目"
echo "成功: $success 个"
echo "失败: $failed 个"
echo ""

if [ $failed -eq 0 ]; then
  echo "🎉 所有项目依赖安装成功！"
  echo ""
  echo "运行示例："
  echo "  cd 01-快速开始"
  echo "  yarn dev"
else
  echo "⚠️  部分项目安装失败，请检查错误信息"
fi
