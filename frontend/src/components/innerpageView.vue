
<template>
    <div class="recent-posts" id="recent-posts">
        <div class="item" v-for="article in array" :key="article['文章id']">
            <recentPostItem :title="article['文章标题']" :pageImg="article['图片url']" :publishTime="article['更新时间']"
                :briefInfo="article['文章内容']" :author="article['文章作者']" :id="article['文章id']"></recentPostItem>
            <div v-if="authorID === $store.state.user.id" class="buttons">
                <a-button type="primary" id="edit" @click="editArticle(article['文章id'])">编辑</a-button>
                <a-button danger id="delete" @click="deleteArticle(article['文章id'])">删除</a-button>
            </div>
        </div>

    </div>
</template>

<script>
import { useStore } from 'vuex';
import { message } from 'ant-design-vue';
import router from '@/router'
import recentPostItem from './recentPostItem.vue';
export default {
    components: {
        recentPostItem
    },
    setup() {
        let store = useStore();
        const token=store.state.user.access;
        const userID=store.state.user.id;
        return {
            token,userID
        }
    },
    props: {
        authorID: Number,
    },
    data() {
        return {
            array: []
        }
    },
    methods: {
        deleteArticle(articleId) {
            console.log('userID:'+this.userID)
            console.log('token: '+this.token)

            debugger//eslint-disable-line
            var myHeaders = new Headers();
            myHeaders.append("User-Agent", "Apifox/1.0.0 (https://www.apifox.cn)");

            var formdata = new FormData();
            debugger//eslint-disable-line
            formdata.append("access_token", this.token);
            formdata.append("article_id", articleId);

            var requestOptions = {
                method: 'POST',
                headers: myHeaders,
                body: formdata,
                redirect: 'follow'
            };

            fetch("http://111.230.109.227:8000/api/delete_article_by_id/", requestOptions)
                .then(response => response.json())
                .then(result => {
                    message.info(result["result"]);
                    console.log('')
                })
                .catch(error => console.log('error', error));

            this.initArticle();
        },
        initArticle() {
            //作者所有文章
            var myHeaders = new Headers();
            myHeaders.append("User-Agent", "Apifox/1.0.0 (https://www.apifox.cn)");

            var formdata = new FormData();
            formdata.append("user_id", this.authorID);

            var requestOptions = {
                method: 'POST',
                headers: myHeaders,
                body: formdata,
                redirect: 'follow'
            };

            fetch("http://111.230.109.227:8000/api/show_articles/", requestOptions)
                .then(response => response.json())
                .then(result => {
                    console.log(result);
                    this.array = result['文章列表'];
                    console.log(this.array);
                })
                .catch(error => console.log('error', error));

            console.log('authorId:' + this.authorID);

        },
        editArticle(ID){
            router.push({ name: 'articleModify', params: { articleID: ID } })
        }
    },
    mounted() {
        this.initArticle();
    }
}
</script>
<style scoped>
.recent-post {
    width: 100%
}

.buttons {
    display: flex;
    justify-content: flex-end;
}

.buttons button {
    width: 100px;
    margin: 10px;
}
</style>