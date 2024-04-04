<script setup>
import articleContain from '../components/articleContain.vue'
import Navigation from '../components/navigationView.vue';
import Inforcard from '../components/inforcardView.vue';
import AiReadCard from '@/components/AiReadCard.vue';
import { useRoute } from 'vue-router';
import { ref } from 'vue';
import { message } from 'ant-design-vue';
import { useStore } from 'vuex';
import VMdPreview from '@kangc/v-md-editor/lib/preview';
import '@kangc/v-md-editor/lib/style/preview.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';

// highlightjs
import hljs from 'highlight.js';

VMdPreview.use(githubTheme, {
    Hljs: hljs,
});
const store = useStore();
//存储文章内容
//let articleInfo=''
let articleTitle = ref();
let articleText = ref();
let publishTime = ref();
let imgUrl = ref();
let authorId = ref();
let aiInput = ref();
let gpt_response = ref();
//文章id


const route = useRoute();
const articleID = parseInt(route.params.articleID);
console.log('article id:' + articleID)

//根据文章ID请求文章数据
var myHeaders = new Headers();
myHeaders.append("User-Agent", "Apifox/1.0.0 (https://www.apifox.cn)");

var formdata = new FormData();
formdata.append("article_id", articleID);

var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: formdata,
    redirect: 'follow'
};

fetch("http://111.230.109.227:8000/api/show_article_by_id/", requestOptions)
    .then(response => response.json())
    .then(result => {
        
        articleTitle.value = result['文章信息']['文章标题'];
        articleText.value = result['文章信息']['文章内容'];
        publishTime.value = result['文章信息']['更新时间'].slice(0, 10);
        imgUrl.value = " background-image: url(" + result['文章信息']['图片url'] + ")"
        authorId.value = result['文章信息']['作者id']
        //console.log('作者id:'+authorId.value);
        aiInput.value = articleText.value;
        /* 
        var reg1 = new RegExp("#","g"); // 加'g'，删除字符串里所有的"a"
        aiInput.value=articleText.value.replace(reg1,",");
         */
        
    })
    .catch(error => console.log('error', error));


//点击提炼文章内容
const visible = ref(false);
const showModal = () => {
    if (!store.state.user.is_login) {
        //未登录
        info();
    }
    else {
        summarizeArticle();
        visible.value = true;
    }

};
const handleOk = e => {
    console.log(e);
    visible.value = false;
};

const info = () => {
    message.info('使用该功能请先登录');
};

function summarizeArticle() {
    var myHeaders = new Headers();
    myHeaders.append("User-Agent", "Apifox/1.0.0 (https://www.apifox.cn)");

    var formdata = new FormData();
    formdata.append("access_token", store.state.user.access);
    formdata.append("gpt_message", "总结提炼一下给定文章，注意文章采用markdown格式书写,返回的文章概要分点，排版要美观些，文章内容如下：" + aiInput.value);

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: formdata,
        redirect: 'follow'
    };

    fetch("http://111.230.109.227:8000/api/gpt_for_chat/", requestOptions)
        .then(response => response.json())
        .then(result => {
            console.log(result);
            gpt_response.value = result["gpt_response"];
        })
        .catch(error => console.log('error', error));
}

</script>

<template>
    <header class="article_page_head" :style="imgUrl">
        <div class="navigate">
            <Navigation></Navigation>
        </div>
        <div class="mypage">
                <h1 class="site-title" style="color:white">{{ articleTitle }}</h1>
                <p>更新时间:{{ publishTime }}</p>
        </div>
    </header>

    <main class="layout">
        <div id="recent-post">
            <articleContain :text="articleText"></articleContain>

        </div>
        <div id="aside-content">
            <Inforcard v-if="authorId" :authorId="authorId"></Inforcard>
            <div class="sticky">
                <AiReadCard v-if="articleText" :text="articleText"></AiReadCard>
                <div id="aside-button">
                    <a-button type="primary" class="button" @click="showModal">提炼文章内容</a-button>
                </div>
            </div>

        </div>
        <div>
            <a-modal v-model:visible="visible" width="1000px" title="文章内容概要" @ok="handleOk">
                <a-spin v-if="!gpt_response" />
                <div id="article-container">
                    <v-md-preview :text="gpt_response" style="overflow: hidden"></v-md-preview>
                </div>
            </a-modal>
        </div>
    </main>
</template>


<style scoped>
.layout {
    display: flex;
    flex: 1 auto;
    margin: 0 auto;
    padding: 40px 15px;
    max-width: 1200px;
    width: 100%;
}

.layout #recent-post {
    width: 74%;
    -webkit-transition: all .3s;
    -moz-transition: all .3s;
    -o-transition: all .3s;
    -ms-transition: all .3s;
    transition: all .3s;
}

#aside-content {
    padding-left: 15px;
    width: 26%;

}

.mypage {
    color: white;
    position: absolute;
    text-align: center;
    top: 45%;
    padding: 0 10px;
    width: 100%;
    mix-blend-mode: difference;

}

.article_page_head {
    height: 50vh;
    background-attachment: fixed;
    background-size:cover;
    color: white;
    position: relative;
    width: 100%;
    background-color: #49b1f5;
    background-position: center center;
    background-repeat: no-repeat;
    
}

h1 {
    color: white;
    font-size: 3em
}

a {
    color: black !
}

#recent-post {
    display: flex;
}

#aside-button {
    margin-top: 10px;
    display: flex;
    align-content: center;
    justify-content: center;

}

.sticky {
    margin-top: 20px;
    position: sticky;
    top: 20px;
}

#aside-button .button {
    width: 100%;
}
</style>