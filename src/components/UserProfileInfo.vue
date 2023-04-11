<template>
    <div class="card" style="margin-top: 30px;">
        <div class="card-body">
            <div class="row">
                <div class="col-3">
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
        const follow = () => (
            context.emit("follow")
        );
        const unfollow = () => (
            context.emit("unfollow")
        );

        return { follow, unfollow };
    }
}
</script>

<style scoped>
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
