<script setup>
import { ArrowRightOutlined } from "@ant-design/icons-vue"
import { defineProps, ref } from 'vue';
import { message } from 'ant-design-vue';
import { useStore } from 'vuex';
const store=useStore();
const props = defineProps({// eslint-disable-line
    text: String
})

let question = ref();
let gpt_response = ref();
let visible=ref(false);

const info = () => {
    message.info('使用该功能请先登录');
};

function startGpt() {
    if (!store.state.user.is_login) {
        //未登录
        info();
    } else if (!props.text){
        message.info('文本内容为空');
    } else if (!question.value){
        message.info('输入的问题为空');
    } else {
        visible.value=true;
        console.log('text:' + props.text)
        console.log('gpt hat start');
        var myHeaders = new Headers();
        myHeaders.append("User-Agent", "Apifox/1.0.0 (https://www.apifox.cn)");

        var formdata = new FormData();
        formdata.append("access_token", store.state.user.access);
        if (!question.value) {
            gpt_response.value = '输入的问题为空';
        }
        else {
            console.log('问题：' + question.value)
            formdata.append("gpt_message", "回答有关给定文章的问题，问题如下:" + question.value + "。文章内容如下（注意文章是用markdown格式书写的）：" + props.text);

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
                    visible.value=false;
                    gpt_response.value = result["gpt_response"];
                })
                .catch(error => console.log('error', error));
        }
    }

}

</script>

<template>
    <div id="airead">
        <div class="ai-img is-center">
            <img src="../assets/aichat.png" alt="图像">
        </div>
        <h2 class="is-center">AI交互</h2>
        <div class="ai-content"><a-spin v-if="visible"/>{{ gpt_response }}</div>
        <div class="input">
            <a-textarea v-model:value="question" placeholder="有问题尽管问我" :auto-size="{ minRows: 1, maxRows: 5 }" />
            <a-button type="primary" @click="startGpt"><arrow-right-outlined /></a-button>
        </div>
    </div>
</template>


<style scoped>
#airead {
    background-color: white;

    overflow: hidden;
    padding: 20px 24px;
    border-radius: 8px;
    box-shadow: 0 3px 8px 6px rgba(7, 17, 27, 0.09);
}

.ai-img {
    overflow: hidden;
    margin: 0 auto;
    width: 60px;
    height: 60px;
    border-radius: 70px;
}

.ai-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.is-center {
    text-align: center;
}

.ai-content {
    padding: 20px 24px;
    width: 100%;
    min-height: 60px;
    background-color: rgb(231, 227, 227);
    border-radius: 10px;
    max-height: 50%;
}

.input {
    padding: 20px 0px;
    display: flex;
}
</style>