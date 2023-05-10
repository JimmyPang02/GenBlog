<script setup>
import searchView from './SearchView.vue';
import { useStore } from 'vuex';
import { HomeOutlined, SolutionOutlined, LoginOutlined, LogoutOutlined, EditOutlined } from '@ant-design/icons-vue';
const store = useStore();
const logout = () => {
    //action里面的成员才是用dispatch
    //store.dispatch("logout");

    //mutation里面的成员用commit！！！！
    store.commit("logout");
    console.log("test")
};
</script>


<template>
    <nav class="container">
        <div id="blog-info">
            <router-link to="/"><span class="site name">Gen-Blog</span></router-link>


        </div>

        <div id="menus">
            <span id="search-button">
                <searchView></searchView>
            </span>
            <span id="menus-items">
                <span>
                    <home-outlined /><router-link to="/">首页</router-link>
                </span>
                <span v-if="!$store.state.user.is_login">
                    <span><solution-outlined /><router-link to="/login">个人主页</router-link></span>
                    <span><edit-outlined /> <router-link to="/login">创作中心</router-link></span>
                    <span><login-outlined /> <router-link to="/login">登录</router-link></span>
                    <span><logout-outlined /><router-link to="/register">注册</router-link></span>
                </span>

                <span v-else>
                    <span>
                        <solution-outlined />
                        <router-link :to="{ name: 'userprofile', params: { userID: $store.state.user.id } }">个人主页
                        </router-link>
                    </span>
                    <span><edit-outlined /> <router-link to="/writecenter">创作中心</router-link></span>
                    <span><login-outlined /> <router-link
                            :to="{ name: 'userprofile', params: { userID: $store.state.user.id } }">{{
                                $store.state.user.username }}</router-link></span>
                    <span><logout-outlined /><router-link class="nav-link" :to="{ name: 'home' }"
                            @click="logout">退出</router-link></span>
                </span>


            </span>

        </div>

    </nav>
</template>


<style scoped>
.container {
    display: flex;
    height: 60px;
    margin: 0;
    padding: 0;
    align-items: center
}

#blog-info {
    font-size: 1.5em;
    font-weight: bold;
    width: 25%;
    margin: 0 .5em;
}

#menus {
    display: flex;
    justify-content: flex-end;
    width: 70%;
    align-items: center;
    font-size: 1.1em
}

span {
    margin: 0 .5em;
}

#menus-items a {
    color: #fff;
    mix-blend-mode: difference;

}
</style>