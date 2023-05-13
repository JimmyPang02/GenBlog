<script setup>
import {ArrowRightOutlined} from "@ant-design/icons-vue"
</script>

<template>
    <div id="airead">
        <div class="ai-img is-center">
                <img src="../assets/aichat.png" alt="图像">
            </div>
        <h2 class="is-center">AI交互</h2>
        <div class="ai-content"></div>
        <div class="input">
            <a-textarea placeholder="有问题尽管问我" :auto-size="{ minRows: 1, maxRows: 5 }"
    />
            <a-button type="primary" ><arrow-right-outlined /></a-button>
        </div>
    </div>
</template>

<style scoped>
#airead{
    background-color: white;
    position: sticky;
    top: 20px;
    overflow: hidden;
    margin-top:20px;
    padding: 20px 24px;
    border-radius: 8px;
    box-shadow: 0 3px 8px 6px rgba(7,17,27,0.09);
}
.ai-img{
    overflow: hidden;
    margin: 0 auto;
    width: 60px;
    height: 60px;
    border-radius: 70px;
}

.ai-img img{
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.is-center {
    text-align: center;
}

.ai-content{
    padding: 20px 24px;
    width:100%;
    min-height:60px;
    background-color:rgb(231, 227, 227);
    border-radius: 10px;
}

.input{
    padding: 20px 0px;
    display: flex;
}
</style>