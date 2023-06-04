<template>
    <!-- <div style="text-align: center; font-size: 24px; margin-top: 50px;">关注列表</div> -->
    <ContentBase>
        <div v-for="user in users" :key="user.id" style="margin-top: 20px;">
            <a-card @click="open_user_profile(user['当前用户id'])">
                <a-row>
                    <a-col :span="4">
                        <a-avatar :src="user['头像链接']" :size="50" />
                    </a-col>
                    <a-col :span="20">
                        <div class="username">{{ user['当前用户名'] }}</div>
                        <div class="description">{{ user['自我介绍'] }}</div>
                        <div class="followerCount">文章数：{{ user['文章数'] }}</div>
                        <div class="followerCount">关注数：{{ user['关注数'] }}</div>
                        <div class="followerCount">粉丝数：{{ user['粉丝数'] }}</div>
                    </a-col>
                </a-row>
            </a-card>
        </div>
    </ContentBase>
</template> 
  
<script>
import ContentBase from '../components/ContentBase.vue';
import $ from 'jquery';
import { ref } from 'vue';
import router from '@/router/index';
import { useStore } from 'vuex';
import API_ROUTES from "@/api/api";
import { backendIP } from "@/api/backend";

export default {
    name: 'FollowList',
    components: { ContentBase },
    props: {
        userID: {
            type: Number,
            required: true
        }
    },
    setup(props) {
        const store = useStore();
        console.log("进入关注列表界面");
        console.log("当前用户为：" + props.userID);
        //请求用户列表信息
        let users = ref([]);
        $.ajax({
            url: backendIP + API_ROUTES.followList,
            type: 'POST',
            data: {
                user_id: props.userID
            },
            success(data) {
                if (data.result == "获取关注用户列表成功") {
                    users.value = data.followed_user_info_list;
                    console.log("获取关注用户列表成功");
                }
                else {
                    console.log("获取关注用户列表失败");
                }
            }
        });

        //定义点击用户卡片时的触发函数
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

.description {
    font-size: 15px;
    color: #999;
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