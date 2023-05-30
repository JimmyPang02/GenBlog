<script setup>
import recentPostItem from './recentPostItem.vue';
</script>

<template>
    <div class="recent-posts" id="recent-posts">
        <div class="item" v-for="article in array" :key="article['文章id']">
            <recentPostItem :title="article['文章标题']" :pageImg="article['图片url']" :publishTime="article['更新时间']" :briefInfo="article['文章内容']" 
            :author="article['文章作者']" :id="article['文章id']"></recentPostItem>
            <div v-if="authorID==userID" class="buttons">
                <a-button type="primary" id="edit">编辑</a-button>
                <a-button danger id="delete">删除</a-button>
            </div>
        </div>
        
    </div>
</template>

<script>
import { useStore } from 'vuex';
export default {
    props: {
        authorID: Number,
    },
    data(){
        return {
            array: Array,
            userID: Number
        }
    },
    created() {
        const store = useStore();
        this.userID == store.state.user.id//存储用户ID
        var myHeaders = new Headers();
        myHeaders.append("User-Agent", "Apifox/1.0.0 (https://www.apifox.cn)");

        var formdata = new FormData();
        //由于代码还没整合，传入的authorID还无法使用，暂用2替代
        formdata.append("user_id", '2');

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
                this.array=result['文章列表'];
                console.log(this.array);
            })
            .catch(error => console.log('error', error));
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