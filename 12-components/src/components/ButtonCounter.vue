<script setup lang="ts">
import { ref } from 'vue'

const count = ref(0)

defineEmits<{
  increment: [count: number]
}>()

function handleClick() {
  count.value++
}
</script>

<template>
  <button @click="handleClick" class="counter-button">
    点击次数: {{ count }}
  </button>
</template>

<style scoped>
.counter-button {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
  margin: 0.5rem;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.counter-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.counter-button:active {
  transform: translateY(0);
}
</style>
