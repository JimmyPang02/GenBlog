<script setup>
import Navigation from '../components/navigationView.vue';
import AiReadCard from '@/components/AiReadCard.vue';
import router from '@/router'
//import richTextEditor from '../components/richTextEditor.vue';
import { ref } from 'vue';
//富文本部分
import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';

// highlightjs
import hljs from 'highlight.js';

VMdEditor.use(githubTheme, {
    Hljs: hljs,
});

const loading = ref(false);
const visible = ref(false);
//点击上传文章响应函数
const showModal = () => {
    console.log('show modal')
    visible.value = true;
};
//点击确定响应函数
const handleOk = () => {
    loading.value = true;
    console.log('text' + text.value);
    console.log('title' + articleTitle.value);
    setTimeout(() => {
        loading.value = false;
        visible.value = false;
        publishArticle()
    }, 2000);
};
const handleCancel = () => {
    visible.value = false;
};

//文章信息
let text = ref('');
let articleTitle = ref('');
//点击富文本编辑器里的save
function saveFile(text, html) {
    console.log('successfully saved')
    console.log(text)
    console.log(html)
}



function publishArticle() {
    var myHeaders = new Headers();
    myHeaders.append("User-Agent", "Apifox/1.0.0 (https://www.apifox.cn)");

    var formdata = new FormData();
    formdata.append("article_title", articleTitle.value);
    formdata.append("article_content", text.value);
    formdata.append("access_token", "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoiYWNjZXNzIiwidXNlcm5hbWUiOiJsenQiLCJleHAiOjE2ODU0ODQ2Nzh9.RSWqPkgoX3V2JLavPgTzSe1h8Lz2KzDez0NDbxCmAtA");
    formdata.append("image_url", "https://s3.bmp.ovh/imgs/2023/05/30/0187ff90a351d527.webp");

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: formdata,
        redirect: 'follow'
    };
    
    var idA=0;
    
    fetch("http://111.230.109.227:8000/api/create_article/", requestOptions)
        .then(response => response.json())
        .then(result => {
            console.log(result);
            console.log("successfully published")
            idA=result['文章编号:']
            console.log('文章id:'+result['文章编号:']);
            router.push({ name: 'article', params: { articleID: idA}})
        })
        .catch(error => console.log('error', error));
}
</script>

<template>
    <header class="navigation">
        <navigation></navigation>
    </header>

    <main class="layout">
        <div id="recent-post">
            <div id="post">
                <div id="article-container">
                    <v-md-editor v-model="text" height="600px" @save="saveFile"></v-md-editor>
                </div>
            </div>
        </div>

        <div id="aside-content">
            <div class="sticky">
                <AiReadCard></AiReadCard>

                <div id="aside-button">
                    <a-button type="primary" class="button">一键润色</a-button>
                    <a-button type="primary" class="submit-button" @click="showModal">上传文章</a-button>
                </div>
            </div>

        </div>

        <div class="submit-modal">
            <a-modal v-model:visible="visible" title="输入要保存的文章标题" @ok="handleOk">
                <template #footer>
                    <a-button key="back" @click="handleCancel">取消</a-button>
                    <a-button key="submit" type="primary" :loading="loading" @click="handleOk">确定</a-button>
                </template>
                <a-input-group compact>
                    <a-input v-model:value="articleTitle" style="width: calc(100% - 200px)" />
                </a-input-group>
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
    max-width: 1300px;
    width: 100%;
}

.layout #recent-post {
    width: 80%;
}

#aside-content {
    padding-left: 15px;
    width: 20%;

}

span a {
    color: black;
}

#aside-button {
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    align-content: center;
    justify-content: center;

}

#aside-button .button {
    width: 100%;
}

.sticky {
    position: sticky;
    top: 20px;
}

.submit-button {
    margin-top: 10px;
}

.submit-modal {
    margin-top: 100px;
}

/* 富文本 */
#post {
    align-self: flex-start;
    -ms-flex-item-align: start;
    padding: 50px 40px;

    border-radius: 8px;
    background-color: white;
    box-shadow: 0 3px 8px 6px rgba(7, 17, 27, 0.09);

}

#article-container {
    overflow-wrap: break-word;
}

.v-md-editor {
    height: 100% !important;
}
</style>