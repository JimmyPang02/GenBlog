<script setup>
import Navigation from '../components/navigationView.vue';
import AiReadCard from '@/components/AiReadCard.vue';
import router from '@/router'
import { message } from 'ant-design-vue';
import { useStore } from 'vuex';
//import richTextEditor from '../components/richTextEditor.vue';
import { ref } from 'vue';
//富文本部分
import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import VMdPreview from '@kangc/v-md-editor/lib/preview';
import '@kangc/v-md-editor/lib/style/preview.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';

// highlightjs
import hljs from 'highlight.js';

VMdEditor.use(githubTheme, {
    Hljs: hljs,
});

VMdPreview.use(githubTheme, {
    Hljs: hljs,
});

const store = useStore();
const loading = ref(false);
const visible = ref(false);//上传文章
const dvisible = ref(false);//文章润色
const dvisible2 = ref(false);//文章续写
const wvisible = ref(true);//加载图标
//点击上传文章响应函数
const showModal = () => {
    if (!text.value) {
        message.info('文章内容为空');
    }
    else {
        console.log('show modal')
        visible.value = true;
    }

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
let polishedText = ref('');
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
    formdata.append("access_token", store.state.user.access);
    formdata.append("image_url", "https://s3.bmp.ovh/imgs/2023/05/30/0187ff90a351d527.webp");

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: formdata,
        redirect: 'follow'
    };

    var idA = 0;

    fetch("http://111.230.109.227:8000/api/create_article/", requestOptions)
        .then(response => response.json())
        .then(result => {
            console.log(result);
            console.log("successfully published")
            idA = result['文章编号:']
            console.log('文章id:' + result['文章编号:']);
            router.push({ name: 'article', params: { articleID: idA } })
        })
        .catch(error => console.log('error', error));
}
//文章润色
function articlePolishing() {
    if (!text.value) {
        message.info('文章内容为空');
    }
    else {
        wvisible.value=true;
        dvisible.value = true;
        var myHeaders = new Headers();
        myHeaders.append("User-Agent", "Apifox/1.0.0 (https://www.apifox.cn)");

        var formdata = new FormData();
        formdata.append("access_token", store.state.user.access);
        formdata.append("gpt_message", "润色一下给定文章，使文章表述更清晰，内容更规整有序。注意文章采用markdown格式书写, 返回的文章要分点，排版要美观，文章内容如下：" + text.value);

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
                wvisible.value=false;
                polishedText.value = result["gpt_response"];
            })
            .catch(error => console.log('error', error));
    }
}
//续写
function articleCompletion(){
    if (!text.value) {
        message.info('文章内容为空');
    }
    else {
        wvisible.value=true;
        dvisible2.value = true;
        var myHeaders = new Headers();
        myHeaders.append("User-Agent", "Apifox/1.0.0 (https://www.apifox.cn)");

        var formdata = new FormData();
        formdata.append("access_token", store.state.user.access);
        formdata.append("gpt_message", "补充续写一下给定文章，内容更完整。注意文章采用markdown格式书写, 返回的文章要分点，排版要美观，文章内容如下：" + text.value);

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
                wvisible.value=false;
                polishedText.value = text.value+'\n'+ result["gpt_response"];
            })
            .catch(error => console.log('error', error));
    }
}
const onClose = () => {
    dvisible.value = false;
    dvisible2.value = false;
}

function adopt(){
    text.value=polishedText.value;
    onClose();
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
                <AiReadCard :text="text"></AiReadCard>

                <div id="aside-button">
                    <a-button type="primary" class="button" @click="articlePolishing">AI润色</a-button>
                    <a-button type="primary" class="submit-button" @click="articleCompletion">AI续写</a-button>
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
                    <a-input v-model:value="articleTitle" />
                </a-input-group>
            </a-modal>
        </div>
        <a-drawer title="文章润色结果" size='large' placement="left" :visible="dvisible" @close="onClose">
            <template #extra>
                <a-button style="margin-right: 8px" @click="onClose">取消</a-button>
                <a-button type="primary" @click="adopt">采纳</a-button>
            </template>
            <a-spin v-if="wvisible" />
            <div class="text-contain">
                <v-md-preview v-if="!wvisible" :text="text" style="overflow: hidden"></v-md-preview>
                <v-md-preview v-if="!wvisible" :text="polishedText" style="overflow: hidden"></v-md-preview>
            </div>
            
        </a-drawer>
        <a-drawer title="文章续写结果" size='large' placement="left" :visible="dvisible2" @close="onClose">
            <template #extra>
                <a-button style="margin-right: 8px" @click="onClose">取消</a-button>
                <a-button type="primary" @click="adopt">采纳</a-button>
            </template>
            <a-spin v-if="wvisible" />
            <div class="text-contain">
                <v-md-preview v-if="!wvisible" :text="text" style="overflow: hidden"></v-md-preview>
                <v-md-preview v-if="!wvisible" :text="polishedText" style="overflow: hidden"></v-md-preview>
            </div>
            
        </a-drawer>
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
.text-contain{
    display:flex;
}
</style>