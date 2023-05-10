<template>
    <a-card :bordered="true" style="width: 100%; margin: 30px auto;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
        <div class="user-info">
            <a-avatar :src="user.photo" :size="{ xs: 70, sm: 80, md: 100, lg: 130, xl: 150, xxl: 170 }" />
            <div class="user-details">
                <h2 class="username">{{ user.username }}</h2>
                <h5 class="userintro">
                    {{ user.intro ? user.intro : '这个人很懒,没有留下简介' }}
                </h5>
            </div>
        </div>
        <a-divider style="margin: 16px 0;" />
        <div class="user-stats">
            <a-row :gutter="8">
                <a-col :span="12">
                    <TeamOutlined />
                    <a-statistic title="粉丝" :value="user.followerCount">
                    </a-statistic>
                </a-col>
                <a-col :span="12">
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
        // let fullname = computed(() => {
        //     return props.user.lastname + props.user.firstname;
        // });
        const store = useStore();
        const follow = () => (
            //后端实现关注
            $.ajax({
                url: "https://app165.acapp.acwing.com.cn/myspace/follow/",
                type: "POST",
                //data传的是所查看的用户
                data: {
                    target_id: props.user.id
                },
                //jwt认证的是自身用户
                headers: {
                    'Authorization': 'Bearer ' + store.state.user.access
                },
                //后端成功则进行前端修改，保持数据一致性
                success(resp) {
                    if (resp.result == 'success') {
                        context.emit("follow")
                    }
                }
            })

        );
        const unfollow = () => (
            //后端实现取消关注
            $.ajax({
                url: "https://app165.acapp.acwing.com.cn/myspace/follow/",
                type: "POST",
                //data传的是所查看的用户
                data: {
                    target_id: props.user.id
                },
                //jwt认证的是自身用户
                headers: {
                    'Authorization': 'Bearer ' + store.state.user.access
                },
                //后端成功则进行前端修改，保持数据一致性
                success(resp) {
                    if (resp.result == 'success') {
                        context.emit("unfollow")
                    }
                }
            })
        );

        return { follow, unfollow };
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
