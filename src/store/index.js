import { createStore } from 'vuex'
import ModuleUser from './user.js'

export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
        // 钩子函数，会在页面刷新时自动调用，用于刷新页面时的登录状态保持
        // 这个过程是异步的，在刷新后获取用户信息的请求还未返回之前
        // 用户信息相关页面已经渲染,
        // state中的用户信息为空, 导致显示未登录。
        created(context) {
          console.log("created");
          const access = localStorage.getItem("access");
          if (access) {
              context.commit("updateAccess", { access: access }) // 调用mutation的updateAccess函数，把获取的access存到全局变量state中
              context.dispatch('getUserInfo', access); // 调用getUserInfo函数，获取用户信息
          }
      },
  },
  modules: {
    user: ModuleUser
  }
})
