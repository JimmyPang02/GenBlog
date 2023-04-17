<template>
    <div class="card" style="margin-top: 30px;">
        <div class="card-body">
            <div class="row">
                <!-- grid system的可以直接后缀一个名，这个名可用于CSS-->
                <div class="col-3 image-field">
                    <!--
                        img class=".img-fluid"是bootstrap的响应式图片，
                        可以自适应大小，很重要,加个samll可以指定图片大小
                    -->
                    <img class=".img-fluid" :src="user.photo" alt="">
                </div>
                <div class="col-9">
                    <div class="username">{{ user.username }}</div>
                    <div class="fans">粉丝数：{{ user.followerCount }}</div>
                    <button @click="unfollow" v-if="user.is_followed" type="button" class="btn btn-secondary">取消关注</button>
                    <button @click="follow" v-if="!user.is_followed" type="button" class="btn btn-secondary">关注</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import $ from 'jquery';
import { useStore } from 'vuex';

export default {
    name: 'UserProfileInfo',
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

.username {
    font-size: 20px;
    font-weight: bold;
}

.fans {
    font-size: 14px;
    color: #999;
}

button {
    margin-top: 10px;
}
</style>
