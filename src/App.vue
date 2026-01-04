<script setup lang="ts">
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
</script>

<template>
  <div class="min-h-screen flex flex-col bg-gray-50 text-gray-900 font-sans">
    <Navbar />
    <main class="flex-grow container mx-auto px-4 py-8">
      <router-view />
    </main>
    <Footer />
  </div>
</template>

<style>
body {
  @apply antialiased;
}
</style>
