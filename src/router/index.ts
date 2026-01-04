import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/category/:slug',
    name: 'Category',
    component: () => import('@/views/Category.vue')
  },
  {
    path: '/site/:id',
    name: 'SiteDetail',
    component: () => import('@/views/SiteDetail.vue')
  },
  {
    path: '/search',
    name: 'Search',
    component: () => import('@/views/Search.vue')
  },
  // User routes
  {
    path: '/user/login',
    name: 'Login',
    component: () => import('@/views/user/Login.vue')
  },
  {
    path: '/user/register',
    name: 'Register',
    component: () => import('@/views/user/Register.vue')
  },
  {
    path: '/user/dashboard',
    name: 'Dashboard',
    component: () => import('@/views/user/Dashboard.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
