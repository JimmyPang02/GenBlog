<template>
    <a-card :bordered="true" style="width: 100%; margin: 30px auto;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
        <div class="user-info">
            <a-avatar :src="user.photo" :size="{ xs: 70, sm: 80, md: 100, lg: 130, xl: 150, xxl: 170 }" />
            <div class="user-details">
                <h2 class="username">{{ user.username }}</h2>
                <h5 class="userintro">
                    {{ user.description ? user.description : '这个人很懒,没有留下简介' }}
                </h5>
            </div>
        </div>
        <a-divider style="margin: 16px 0;" />
        <div class="user-stats">
            <a-row :gutter="8">
                <a-col :span="8">
                    <TeamOutlined />
                    <a-statistic title="关注" :value="user.followerCount">
                    </a-statistic>
                </a-col>
                <a-col :span="8">
                    <TeamOutlined />
                    <a-statistic title="粉丝" :value="user.fanCount">
                    </a-statistic>
                </a-col>
                <a-col :span="8">
                    <FormOutlined />
                    <a-statistic title="文章" :value="user.postCount ? user.postCount : 105">
                    </a-statistic>
                </a-col>
            </a-row>
        </div>
        <div class="user-actions">
            <a-button class="action-button" size="middle" type="primary" @click="follow" v-if="!user.is_followed">
                <UserAddOutlined />
                关注
            </a-button>
            <a-button class="action-button" size="middle" @click="unfollow" v-if="user.is_followed">
                <UserDeleteOutlined />
                取消关注
            </a-button>
            <a-icon type="plus"></a-icon>
        </div>
    </a-card>
</template>

<script>
import $ from 'jquery';
import { useStore } from 'vuex';
import { UserAddOutlined, TeamOutlined, FormOutlined, UserDeleteOutlined } from '@ant-design/icons-vue';
import API_ROUTES from "@/api/api";
import { backendIP } from "@/api/backend";
import { computed } from 'vue';

export default {
    name: 'UserProfileInfo',
    components: { UserAddOutlined, TeamOutlined, FormOutlined, UserDeleteOutlined },
    props: {
        user: {
            type: Object,
            required: true
        }
    },
    setup(props, context) {
        const store = useStore();
        //判断当前的用户界面是不是自己的userID
        const is_me = computed(() => { return props.user.id == store.state.user.id })
        const follow = () => {
            // 判断是否是自己的界面,弹出提示
            if (is_me.value) {
                alert("不能关注自己哦~");
                return;
            }
            // 后端关注
            $.ajax({
                url: backendIP + API_ROUTES.follow,
                type: "POST",
                data: {
                    access_token: store.state.user.access,
                    follow_user_id: props.user.id
                },
                success(resp) {
                    if (resp.result == '关注用户成功') {
                        //后端成功则进行前端修改，保持数据一致性
                        context.emit("follow")
                        console.log("关注成功");
                    }
                    else {
                        console.log("关注失败");
                    }
                }
            })
        };
        const unfollow = () => (

            // 后端保证取消关注
            $.ajax({
                url: backendIP + API_ROUTES.unfollow,
                type: "POST",
                data: {
                    access_token: store.state.user.access,
                    unfollow_user_id: props.user.id
                },
                //后端成功则进行前端修改，保持数据一致性
                success(resp) {
                    if (resp.result == '取消关注用户成功') {
                        context.emit("unfollow")
                        console.log("取消关注成功");
                    }
                    else {
                        console.log("取消关注失败");
                    }
                }
            })
        );
        return { follow, unfollow, is_me };
    }
}
</script>

<style scoped>
.image-field {
    display: flex;
    flex-direction: column;
    justify-content: center;
}


/* 指定圆形图片 */
img {
    border-radius: 50%;
}

.fans {
    font-size: 14px;
    color: #999;
}

button {
    margin-top: 10px;
}
</style>
