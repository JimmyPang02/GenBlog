<template>
    <ContentBase>
        <div class="row justify-content-md-center">
            <div class="col-3">
                <form @submit.prevent="register">
                    <div class="mb-3">
                        <label for="username" class="form-label">用户名</label>
                        <input v-model="username" type="text" class="form-control" id="username">
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">密码</label>
                        <input v-model="password" type="password" class="form-control" id="password">
                    </div>
                    <div class="mb-3">
                        <label for="password2" class="form-label">确认密码</label>
                        <input v-model="password2" type="password2" class="form-control" id="password2">
                    </div>
                    <div style="color: red;">{{ error_message }}</div>
                    <button type="submit" class="btn btn-primary">注册</button>
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
    name: 'RegisterView',
    components: { ContentBase },
    setup() {
        const store = useStore();
        let username = ref('');
        let password = ref('');
        let password2 = ref('');//确认密码
        let error_message = ref('');

        const register = () => {
            //登录前把error message清空
            error_message.value = '';
            //调用store里面的注册函数
            store.dispatch('register', {
                username: username.value,
                password: password.value,
                password2: password2.value,
                success() {
                    console.log("success")
                    //（1）注册成功后跳转登录界面
                    router.push({ name: "login" });
                },
                //（2）错误的话，显示错误信息
                error(mesg) {
                    error_message.value = mesg;
                },
            });
        }

        return { username, password, password2, register, error_message };
    }
}
</script >

<style scoped>
button {
    margin-top: 5px;
    width: 100%;
}
</style>