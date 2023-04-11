<template>
    <ContentBase>
        <div>用户列表</div>
        <div v-for="user in users" :key="user.id">
            <div class="card" @click="open_user_profile(user.id)">
                <div class="card-body">
                    <div class="row">
                        <div class="col-1">
                            <img :src="user.photo" class=".img-fluid" style="width: 50px; height: 50px;">
                        </div>
                        <div class="col-11">
                            <div class="username">{{ user.username }}</div>
                            <div class="followerCount">粉丝数：{{ user.followerCount }}</div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </ContentBase>
</template> 
  
<script>
import ContentBase from '../components/ContentBase.vue';
import $ from 'jquery';
import { ref } from 'vue';
import router from '@/router/index';
import { useStore } from 'vuex';

export default {
    name: 'UserList',
    components: { ContentBase },
    setup() {

        //请求用户列表信息
        let users = ref([]);
        $.ajax({
            url: 'https://app165.acapp.acwing.com.cn/myspace/userlist/',
            type: 'GET',
            success(data) {
                users.value = data;
            }
        });

        //定义点击用户卡片时的触发函数
        const store = useStore();
        const open_user_profile = (userID) => {
            //如果未登陆，先登陆
            if (!store.state.user.is_login) {
                router.push({
                    name: 'login'
                })
            }
            //如果已登录，才可以点击卡片，跳转指定用户界面
            else {
                router.push({
                    name: 'userprofile',
                    params: { userID: userID }
                })
            }
        }

        return { users, open_user_profile }
    }
}
</script >

<style scoped>
img {
    border-radius: 50%;
}

.username {
    font-size: 20px;
    font-weight: bold;
}

.followerCount {
    font-size: 15px;
    color: #999;
}

.card {
    cursor: pointer;
    margin-top: 30px;
}

.card:hover {
    background-color: #f5f5f5;
}
</style>