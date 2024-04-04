<template>
    <div class="container">
        <!--这里是一个container,
        用于把东西放在中间，还可以调整大小
      -->
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
                <router-link class="navbar-brand" :to="{ name: 'home' }">GOAT空间</router-link>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
                    aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <!--（1）登录前的导航栏-->
                <div class="collapse navbar-collapse" id="navbarText" v-if="!$store.state.user.is_login">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <router-link class="nav-link active" aria-current="page" :to="{ name: 'home' }">首页</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" :to="{ name: 'FollowList' }">好友列表</router-link>
                        </li>
                        <li class="nav-item">
                            <!--这个用户动态地方不能轻易改成$store.state.user.id，因为一开始还没有登录，就没有user.id
                            如果没有userID，这里就会出错，所以先暂时注释掉-->
                            <!--
                            <router-link class="nav-link"
                                :to="{ name: 'userprofile', params: { userID: 1 } }">用户动态</router-link>
                            -->
                        </li>
                    </ul>
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <router-link class="nav-link" :to="{ name: 'login' }">登陆</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" :to="{ name: 'register' }">注册</router-link>
                        </li>
                    </ul>
                </div>
                <!--（2）登录后的导航栏-->
                <div class="collapse navbar-collapse" id="navbarText" v-else>
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <router-link class="nav-link active" aria-current="page" :to="{ name: 'home' }">首页</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" :to="{ name: 'FollowList' }">好友列表</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link"
                                :to="{ name: 'userprofile', params: { userID: $store.state.user.id } }">用户动态</router-link>
                        </li>
                    </ul>
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <router-link class="nav-link" :to="{
                                    name: 'userprofile',
                                    params: { userID: $store.state.user.id }
                                }">
                                {{ $store.state.user.username }}
                            </router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" :to="{ name: 'home' }" @click="logout">退出</router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
</template>
<script>
import { useStore } from 'vuex';
export default {
    name: 'NavBar',
    components: {
    },
    setup() {
        const store = useStore();
        const logout = () => {
            //action里面的成员才是用dispatch
            //store.dispatch("logout");

            //mutation里面的成员用commit！！！！
            store.commit("logout");
        };
        return { logout };
    }
}
</script>

<style scoped>

</style>
