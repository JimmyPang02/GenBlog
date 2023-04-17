<template>
    <ContentBase>
        <div class="row">
            <div class="col-3">
                <UserProfileInfo @follow="follow" @unfollow="unfollow" :user="user"></UserProfileInfo>
                <!--是自己才显示编辑区-->
                <UserProfileWrite v-if="is_me" @post_a_post="post_a_post">
                </UserProfileWrite>
            </div>
            <div class="col-9">
                <UserProfilePosts :user="user" :posts="posts" @delete_a_post="delete_a_post"></UserProfilePosts>
            </div>
        </div>
    </ContentBase>
</template> 
  
<script>
import { reactive } from 'vue';
import ContentBase from '../components/ContentBase.vue';
import UserProfileInfo from '../components/UserProfileInfo.vue';
import UserProfilePosts from '../components/UserProfilePosts.vue';
import UserProfileWrite from '@/components/UserProfileWrite.vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import $ from 'jquery';
import { computed } from 'vue';

export default {
    name: 'UserProfile',
    components: { ContentBase, UserProfileInfo, UserProfilePosts, UserProfileWrite },
    setup() {

        //用路由获取userID，为什么不用store，两者有本质区别
        //因为路由获取的是打开页面的userID，而store的userID是用户的userID
        const store = useStore();
        const route = useRoute();
        const userID = parseInt(route.params.userID);//不解析返回的是字符串，会影响后续is_me的判断

        const user = reactive({
            //这里不需要定义属性，在ajax的success里面赋值属性时自动定义
        });
        const posts = reactive({
            //这里不需要定义属性，在ajax的success里面赋值属性时自动定义
        });

        //判断当前的用户界面是不是自己的userID
        const is_me = computed(() => { return userID == store.state.user.id })

        //(1)获取所查看的用户信息
        $.ajax({
            url: "https://app165.acapp.acwing.com.cn/myspace/getinfo/",
            type: "GET",
            data: {
                user_id: userID
            },
            //这里的认证，代表的是登陆用户的信息
            //这里的传参data，代表的是想要查看的用户页面的userID
            //分别代表两个不同的人，才能构成：“一人是否关注另一人”的情景
            headers: {
                "Authorization": "Bearer " + store.state.user.access,
            },
            success(resp) {
                user.id = resp.id;
                user.username = resp.username;
                user.photo = resp.photo;
                user.followerCount = resp.followerCount;
                user.is_followed = resp.is_followed;
            }
        })
        //(2)获取所查看的用户的帖子信息
        $.ajax({
            url: "https://app165.acapp.acwing.com.cn/myspace/post/",
            type: "GET",
            data: {
                user_id: userID
            },
            headers: {
                "Authorization": "Bearer " + store.state.user.access,
            },
            success(resp) {
                posts.posts = resp;
                posts.count = resp.length;
            }
        })

        // 下面是视频1版本的时候，写死的帖子
        // const user = reactive({
        //     id: 1,
        //     username: '彭山羊',
        //     lastname: '彭',
        //     firstname: '山羊',
        //     followerCount: 10000,
        //     avatar: 'https://cdnv2.ruguoapp.com/FsHDe1QJ2oB7iedLDJfuw4rY1SU-v3.jpg?imageMogr2/auto-orient/heic-exif/1/format/jpeg/thumbnail/!120x120r/gravity/Center/crop/!120x120a0a0',
        //     isfollowed: false,
        // });
        // const posts = reactive(
        //     {
        //         count: 2,
        //         posts: [
        //             {
        //                 id: 1,
        //                 content: '今天上了web课，学了vue，感觉很有意思',
        //             },
        //             {
        //                 id: 2,
        //                 content: '今天好好学习，明天好好写代码',
        //             }
        //         ]
        //     }
        // )
        const follow = () => {
            user.is_followed = true;
            user.followerCount = user.followerCount + 1;
        };
        const unfollow = () => {
            user.is_followed = false;
            user.followerCount = user.followerCount - 1;
        };
        /**/


        const post_a_post = (content) => {
            posts.count = posts.count + 1;
            posts.posts.unshift({
                id: posts.count,
                content: content
            });
        }

        const delete_a_post = (post_id) => {
            //前端删除
            posts.posts = posts.posts.filter(
                //这里面是遍历posts数组里的每个元素post
                //只要不是删除帖子ID的帖子都保留
                post => post.id !== post_id
            );
        }
        return { user, follow, unfollow, posts, post_a_post, is_me, delete_a_post };
    }
}
</script >
  
<style scoped></style>