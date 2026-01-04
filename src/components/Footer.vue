<script setup lang="ts">
const currentYear = new Date().getFullYear()
</script>

<template>
  <footer class="bg-white border-t border-gray-100 py-8 mt-auto">
    <div class="container mx-auto px-4 text-center text-gray-500 text-sm">
      <p>&copy; {{ currentYear }} AI Nav. All rights reserved.</p>
      <div class="mt-4 space-x-4">
        <a href="#" class="hover:text-primary">关于我们</a>
        <a href="#" class="hover:text-primary">免责声明</a>
        <a href="#" class="hover:text-primary">联系方式</a>
      </div>
    </div>
  </footer>
</template>
