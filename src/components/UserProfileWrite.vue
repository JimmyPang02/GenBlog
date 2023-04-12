<template>
    <div class="card" style="margin-top: 30px;">
        <div class="card-body">
            <div class="mb-3">
                <label for="edit-post" class="form-label">编辑帖子</label>
                <textarea v-model="content" class="form-control" id="edit-post" rows="3"></textarea>
            </div>
            <button @click="post_a_post" type="button" class="btn btn-primary">发帖</button>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';
import $ from "jquery"
import { useStore } from 'vuex';

export default {
    name: 'UserProfileWrite',
    setup(props, context) {

        const store = useStore();

        let content = ref('');
        const post_a_post = () => {

            //发帖（让数据库存储）
            $.ajax({
                url: "https://app165.acapp.acwing.com.cn/myspace/post/",
                type: "POST",
                data: {
                    content: content.value
                },
                headers: {
                    "Authorization": "Bearer " + store.state.user.access,
                },
                success(resp) {
                    //这里应该是属于【前端修改】，根据前端的content.value直接更新
                    //（1）前端修改用户会更流畅，但如果后端有bug的话，可能会出现前端实现更新，
                    //但后端出bug没保存，一刷新你前端的东西就没有了
                    //（2）后端更新就是修改数据库，等数据库更新完再请求获取最新数据
                    if (resp.result === 'success') {
                        context.emit("post_a_post", content.value);
                        content.value = "";
                    }
                }
            })


        };
        return { content, post_a_post };
    },
}

</script>

<style scoped></style>
