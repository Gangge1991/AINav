<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { Search, Menu, X, User } from 'lucide-vue-next'

const router = useRouter()
const isMenuOpen = ref(false)
const searchQuery = ref('')

const handleSearch = () => {
  if (searchQuery.value.trim()) {
    router.push({ name: 'Search', query: { q: searchQuery.value } })
    isMenuOpen.value = false
  }
}
</script>

<template>
  <header class="bg-white shadow-sm sticky top-0 z-50">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between h-16">
        <!-- Logo -->
        <RouterLink to="/" class="flex items-center gap-2 font-bold text-xl text-primary">
          <span class="bg-primary text-white p-1 rounded-lg">AI</span>
          <span>Nav</span>
        </RouterLink>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center space-x-8">
          <div class="relative w-64">
            <input
              v-model="searchQuery"
              @keyup.enter="handleSearch"
              type="text"
              placeholder="搜索网站..."
              class="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-200 focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary transition-colors"
            />
            <Search class="w-4 h-4 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" />
          </div>
          
          <nav class="flex items-center gap-6 text-sm font-medium text-gray-600">
            <RouterLink to="/" class="hover:text-primary transition-colors">首页</RouterLink>
            <RouterLink to="/category/tech-tools" class="hover:text-primary transition-colors">分类</RouterLink>
            <RouterLink to="/user/dashboard" class="flex items-center gap-2 hover:text-primary transition-colors">
              <User class="w-4 h-4" />
              <span>用户中心</span>
            </RouterLink>
          </nav>
        </div>

        <!-- Mobile Menu Button -->
        <button @click="isMenuOpen = !isMenuOpen" class="md:hidden p-2 text-gray-600">
          <Menu v-if="!isMenuOpen" class="w-6 h-6" />
          <X v-else class="w-6 h-6" />
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    <div v-if="isMenuOpen" class="md:hidden border-t border-gray-100 bg-white">
      <div class="p-4 space-y-4">
        <div class="relative">
          <input
            v-model="searchQuery"
            @keyup.enter="handleSearch"
            type="text"
            placeholder="搜索网站..."
            class="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-200 focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary"
          />
          <Search class="w-4 h-4 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" />
        </div>
        <nav class="flex flex-col space-y-3 text-sm font-medium text-gray-600">
          <RouterLink to="/" class="hover:text-primary" @click="isMenuOpen = false">首页</RouterLink>
          <RouterLink to="/category/tech-tools" class="hover:text-primary" @click="isMenuOpen = false">分类</RouterLink>
          <RouterLink to="/user/dashboard" class="hover:text-primary" @click="isMenuOpen = false">用户中心</RouterLink>
        </nav>
      </div>
    </div>
  </header>
</template>
