<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Category {
  id: number
  name: string
  slug: string
  icon: string
  children: Category[]
}

const categories = ref<Category[]>([])
const loading = ref(true)

const fetchCategories = async () => {
  try {
    const response = await axios.get('/api/categories')
    if (response.data.status === 'success') {
      categories.value = response.data.data
    }
  } catch (error) {
    console.error('Failed to fetch categories:', error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchCategories()
})
</script>

<template>
  <div class="space-y-8">
    <!-- Hero Section -->
    <section class="text-center py-12 bg-gradient-to-br from-primary/5 to-transparent rounded-2xl">
      <h1 class="text-4xl font-bold text-gray-900 mb-4">发现优质 AI 工具与资源</h1>
      <p class="text-xl text-gray-600 mb-8">收录全球最热门的 AI 网站，助你提升工作效率</p>
    </section>

    <!-- Categories -->
    <section>
      <h2 class="text-2xl font-bold text-gray-900 mb-6">热门分类</h2>
      <div v-if="loading" class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
        <div v-for="i in 6" :key="i" class="h-24 bg-gray-100 rounded-xl animate-pulse"></div>
      </div>
      <div v-else class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
        <RouterLink
          v-for="category in categories"
          :key="category.id"
          :to="{ name: 'Category', params: { slug: category.slug } }"
          class="flex flex-col items-center justify-center p-6 bg-white border border-gray-100 rounded-xl hover:shadow-md hover:border-primary/20 transition-all group"
        >
          <span class="text-3xl mb-3">{{ category.icon }}</span>
          <span class="font-medium text-gray-900 group-hover:text-primary">{{ category.name }}</span>
        </RouterLink>
      </div>
    </section>
  </div>
</template>
