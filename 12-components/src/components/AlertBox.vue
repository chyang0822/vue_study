<script setup lang="ts">
defineProps<{
  type?: 'success' | 'warning' | 'error'
}>()
</script>

<template>
  <div :class="['alert-box', type]">
    <slot></slot>
  </div>
</template>

<style scoped>
.alert-box {
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 1rem;
  border-left: 4px solid;
}

.alert-box.success {
  background: #d4edda;
  color: #155724;
  border-color: #28a745;
}

.alert-box.warning {
  background: #fff3cd;
  color: #856404;
  border-color: #ffc107;
}

.alert-box.error {
  background: #f8d7da;
  color: #721c24;
  border-color: #dc3545;
}
</style>
