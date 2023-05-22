<template>
    <ContentBase>

        <div class="welcom">
            <div>
                <a-icon #="loginicon">
                    <LoginOutlined />
                </a-icon>
            </div>
            <div>
                欢迎登陆
            </div>

        </div>
        <a-row type="flex" justify="center" style="margin-top: 20px;">
            <a-col :span="8">
                <a-form name="basic" :label-col="{ span: 4 }" :wrapper-col="{ span: 16 }" @submit.prevent="login">
                    <a-form-item label="用户名" name="username" :rules="[{ required: true, message: '请输入用户名！' }]">
                        <a-input v-model:value="username" />
                    </a-form-item>
                    <a-form-item label="密码" name="password" :rules="[{ required: true, message: '请输入密码！' }]">
                        <a-input-password v-model:value="password" />
                    </a-form-item>
                    <a-form-item name="remember" :wrapper-col="{ offset: 4, span: 16 }">
                        <a-checkbox v-model:checked="remember">Remember me</a-checkbox>
                    </a-form-item>
                    <div style="color: red;">{{ error_message }}</div>
                    <a-form-item :wrapper-col="{ offset: 4, span: 16 }">
                        <a-button type="primary" html-type="submit">
                            <div>
                                登录
                            </div>
                        </a-button>
                    </a-form-item>
                </a-form>
            </a-col>
        </a-row>
    </ContentBase>
    <ContentBaseNcard v-if="0"></ContentBaseNcard>
    <!-- <ContentBase>
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
    </ContentBase> -->
</template> 
  
<script>
import ContentBase from '../components/ContentBase.vue';
import ContentBaseNcard from '@/components/ContentBaseNcard.vue';
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router/index';
import { LoginOutlined } from '@ant-design/icons-vue';


export default {
    name: 'LoginView',
    components: { ContentBase, ContentBaseNcard, LoginOutlined },
    setup() {

        const onFinish = values => {
            console.log('Success:', values);
        };
        const onFinishFailed = errorInfo => {
            console.log('Failed:', errorInfo);
        };
        const store = useStore();
        let username = ref('');
        let password = ref('');
        let remember = ref(true);
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
                    router.push({ name: "home" });
                },
                error() {
                    //（2）错误的话，显示错误信息
                    // html里面直接放这个响应式变量即可，为空的时候反正也不会显示
                    console.log("failed");
                    error_message.value = "用户名或密码错误";
                }
            });
        }

        return {
            onFinish,
            onFinishFailed,
            username, password, remember, login, error_message
        };
    }
}
</script >

<style scoped>
button {
    margin-top: 5px;
    width: 100%;
}

.welcom {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-size: 24px;
    margin-top: 50px;
}
#loginicon{
    display: flex !important;;
}
</style>