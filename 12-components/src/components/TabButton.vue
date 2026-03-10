<script setup lang="ts">
defineProps<{
  active?: boolean
}>()
</script>

<template>
  <button :class="{ active }">
    <slot></slot>
  </button>
</template>

<style scoped>
button {
  background: #f8f9fa;
  color: #5a6c7d;
  border: 2px solid #e1e8ed;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.3s;
}

button:hover {
  background: #e8f5e9;
  border-color: #42b983;
}

button.active {
  background: #42b983;
  color: white;
  border-color: #42b983;
}
</style>
