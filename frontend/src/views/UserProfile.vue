<template>
    <Navigation></Navigation>

    <ContentBaseNcard>
        <a-row :gutter="16">
            <a-col :span="6">
                <UserProfileInfo @follow="follow" @unfollow="unfollow" @save="save" :user="user" />
            </a-col>
            <a-col :span="18">
                <a-card :bordered="true" style="width: 100%; margin: 30px auto;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); ">
                    <div>
                        <a-menu mode="horizontal">
                            <a-menu-item key="followlist" @click="selectMenu('followlist')">
                                <template #icon>
                                    <AppstoreOutlined />
                                </template>
                                <TeamOutlined></TeamOutlined>
                                关注列表
                            </a-menu-item>
                            <a-menu-item key="myposts" @click="selectMenu('myposts')">
                                <FormOutlined></FormOutlined>
                                我的文章
                            </a-menu-item>
                        </a-menu>
                    </div>
                    <div v-if="Current === 'followlist'">
                        <FollowList :userID="userID" />
                    </div>
                    <div v-if="Current === 'myposts'">
                        <MyArticlePage :authorID="userID" />
                    </div>
                </a-card>
            </a-col>
        </a-row>
    </ContentBaseNcard>
</template> 
  
<script>
import { reactive } from 'vue';
import { ref } from 'vue'

import ContentBaseNcard from '../components/ContentBaseNcard.vue';
import UserProfileInfo from '../components/UserProfileInfo.vue';
import MyArticlePage from './MyArticlePage.vue';
import FollowList from './FollowList.vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import $ from 'jquery';
import { computed } from 'vue';
import { TeamOutlined, FormOutlined } from '@ant-design/icons-vue';
import Navigation from '../components/navigationView.vue';
import API_ROUTES from "@/api/api";
import { backendIP } from "@/api/backend";

export default {
    name: 'UserProfile',
    components: {
        ContentBaseNcard, UserProfileInfo, FollowList, MyArticlePage,
        TeamOutlined, FormOutlined, Navigation,
    },

    setup() {
        // 内嵌菜单栏
        let Current = ref('followlist');
        const selectMenu = (key) => {
            Current.value = key;
        };
        // 获取用户信息
        const store = useStore();
        const route = useRoute();
        const userID = parseInt(route.params.userID);//不解析返回的是字符串，会影响后续is_me的判断
        const user = reactive({
        });

        //判断当前的用户界面是不是自己的userID
        const is_me = computed(() => { return userID == store.state.user.id })

        //(1)获取所查看的用户信息
        $.ajax({
            url: backendIP + API_ROUTES.UserInfoByID,
            type: "POST",
            data: {
                user_id: userID
            },
            success(resp) {
                user.id = resp["当前用户id"];
                user.username = resp["当前用户名"];
                user.description = resp["自我介绍"];
                user.photo = resp["头像链接"];
                user.followerCount = resp["关注数"];
                user.fanCount = resp["粉丝数"];
                user.postCount = resp["文章数"];
            }
        })
        //(2)获取所查看的用户的关注信息
        $.ajax({
            url: backendIP + API_ROUTES.isFollowed,
            type: "POST",
            data: {
                access_token: store.state.user.access,
                user_id: userID
            },
            success(resp) {
                user.is_followed = resp.isfollowed;
            }
        })
        // (3)关注和取消关注
        const follow = () => {
            user.is_followed = true;
            user.followerCount = user.followerCount + 1;
        };
        const unfollow = () => {
            user.is_followed = false;
            user.followerCount = user.followerCount - 1;
        };
        // (4)保存个人资料
        const save = (editedUser) => {
            user.description = editedUser.description;
            user.photo = editedUser.photo;
        };
        return {
            selectMenu, Current, userID,
            user, follow, unfollow, is_me, save
        };

    }
}
</script >
  
<style scoped></style>