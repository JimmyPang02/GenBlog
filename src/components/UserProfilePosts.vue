<template>
    <div class="card" style="margin-top: 30px;">
        <div class="card-body">
            文章总数：{{ posts.count }}
            <div v-for="post in posts.posts" :key="post.id">
                <div class="card" style="margin-top: 30px;">
                    <div class="card-body">
                        <div>{{ post.content }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'UserProfilePosts',
    props: {
        posts: {
            type: Object,
            required: true
        }
    },
}
</script>

<style scoped></style>
