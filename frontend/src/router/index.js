import { createRouter, createWebHistory } from 'vue-router'
//import { createRouter, createWebHashHistory } from 'vue-router'

/* import HomeView from '../views/HomeView.vue' */
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import FollowList from '../views/FollowList.vue'
import UserProfile from '../views/UserProfile.vue'
import HomePage from "../views/HeadPage.vue"
import MyArticlePage from "../views/MyArticlePage.vue"
import WriteCenter from "../views/WriteCenter.vue"
import ArticlePage from "../views/ArticlePage.vue"
import articleModify from '@/views/articleModify.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/myarticle/',
    name: 'myarticle',
    component: MyArticlePage
  },
  {
    path: '/writecenter/',
    name: 'writecenter',
    component: WriteCenter
  },
  {
    path: '/article/:articleID/',
    name: 'article',
    component: ArticlePage
  },
  {
    path: '/articleModify/:articleID',
    name: 'articleModify',
    component: articleModify
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
