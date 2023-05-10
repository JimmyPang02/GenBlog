import { createRouter, createWebHistory } from 'vue-router'
//import { createRouter, createWebHashHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import FollowList from '../views/FollowList.vue'
import UserProfile from '../views/UserProfile.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/register/',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/FollowList/',
    name: 'FollowList',
    component: FollowList
  },
  {
    path: '/userprofile/:userID/',
    name: 'userprofile',
    component: UserProfile
  },
  {
    path: '/404/',
    name: '404',
    component: NotFoundView
  },
  {
    path: '/:pathMatch(.*)*/',
    redirect: { name: '404' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
