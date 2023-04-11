<template>
    <ContentBase>
        <div class="row justify-content-md-center">
            <div class="col-3">
                <form @submit.prevent="login">
                    <div class="mb-3">
                        <label for="username" class="form-label">用户名</label>
                        <input v-model="username" type="text" class="form-control" id="username">
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">密码</label>
                        <input v-model="password" type="password" class="form-control" id="password">
                    </div>
                    <div style="color: red;">{{ error_message }}</div>
                    <button type="submit" class="btn btn-primary">登录</button>
                </form>
            </div>
        </div>
    </ContentBase>
</template> 
  
<script>
import ContentBase from '../components/ContentBase.vue';
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router/index';

export default {
    name: 'LoginView',
    components: { ContentBase },
    setup() {
        const store = useStore();
        let username = ref('');
        let password = ref('');
        let error_message = ref('');

        const login = () => {
            //登录前把error message清空
            error_message.value = '';
            store.dispatch('login', {
                username: username.value,
                password: password.value,
                success() {
                    console.log("success")
                    //（1）实现登录成功后跳转
                    router.push({ name: "userlist" });
                },
                error() {
                    //（2）错误的话，显示错误信息
                    // html里面直接放这个响应式变量即可，为空的时候反正也不会显示
                    console.log("failed");
                    error_message.value = "用户名或密码错误";
                }
            });
        }

        return { username, password, login, error_message };
    }
}
</script >

<style scoped>
button {
    margin-top: 5px;
    width: 100%;
}
</style>