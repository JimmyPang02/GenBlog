<template>
  <router-view :key="$route.fullPath" />
</template>


<script>
import store from './store';

/* import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap'; */

export default {
  name: 'App',
  created() {
    // 钩子函数，会在页面刷新时自动调用，用于刷新页面时的登录状态保持
    console.log("created");
    const access = localStorage.getItem("access");
    if (access) {
      store.commit("updateAccess", { access: access }) // 调用mutation的updateAccess函数，把获取的access存到全局变量state中
      store.dispatch('getUserInfo', access); // 调用getUserInfo函数，获取用户信息
    }

  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;

  /* 灰色背景 */
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
