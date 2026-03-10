<script setup lang="ts">
defineProps<{
  title: string
  author: string
}>()

const emit = defineEmits<{
  click: [title: string]
}>()
</script>

<template>
  <article class="blog-post" @click="emit('click', title)">
    <h3>{{ title }}</h3>
    <p class="author">作者: {{ author }}</p>
  </article>
</template>

<style scoped>
.blog-post {
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 6px;
  margin-bottom: 1rem;
  border-left: 4px solid #42b983;
  cursor: pointer;
  transition: all 0.3s;
}

.blog-post:hover {
  background: #e8f5e9;
  transform: translateX(4px);
}

.blog-post h3 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.author {
  color: #7f8c8d;
  font-size: 0.9rem;
  margin: 0;
}
</style>
