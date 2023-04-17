<template>
    <div class="card" style="margin-top: 30px;">
        <div class="card-body">
            <!--文章总数：{{ posts.count }}-->
            <div v-for="post in posts.posts" :key="post.id">
                <div class="card" style="margin-top: 30px;">
                    <div class="card-body">
                        <div>
                            {{ post.content }}
                            <!--增加删除帖子按钮-->
                            <button @click="delete_a_post(post.id)" v-if="is_me" type="button"
                                class="btn btn-danger btn-sm">删除</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';
import $ from "jquery";

export default {
    name: 'UserProfilePosts',
    props: {
        posts: {
            type: Object,
            required: true
        },
        user: {
            type: Object,
            required: true
        }
    },
    setup(props, context) {
        const store = useStore();
        const is_me = computed(() => {
            return store.state.user.id === props.user.id;
        });
        const delete_a_post = (post_id) => {
            //后端删除
            $.ajax({
                url: "https://app165.acapp.acwing.com.cn/myspace/post/",
                type: "DELETE",
                headers: {
                    "Authorization": "Bearer " + store.state.user.access,
                },
                data: {
                    post_id: post_id
                },
                success(resp) {
                    if (resp.result === 'success') {
                        //前端删除
                        context.emit("delete_a_post", post_id)
                    }
                }
            })
        }
        return { is_me, delete_a_post }
    }
}
</script>

<style scoped>
button {
    float: right;
}
</style>
