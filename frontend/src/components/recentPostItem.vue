<script setup>
import {FieldTimeOutlined} from '@ant-design/icons-vue';
</script>

<template>
    <div class="recent-post-item" v-if="id%2===1">
        <div class="post-cover-left">
            <router-link :to="{ name: 'article', params: { articleID: id} }" >
                <img :src="pageImg" alt="" class="post-img">
            </router-link>
        </div>
        <div class="recent-post-info">
            <router-link :to="{ name: 'article', params: { articleID: id} }" class="article-title">{{ title }}</router-link>
            <div class="artical-meta-wrap">
                <span class="post-meta-date">
                    {{ author }}|<field-time-outlined />发表于 {{ publishTime }}
                </span>
                
            </div>
            <div class="content">
                {{briefInfo.slice(0,20)+'...'}}
            </div>
        </div>
    </div>
    <div class="recent-post-item" v-else>
        <div class="recent-post-info">
            <router-link :to="{ name: 'article', params: { articleID: id} }" class="article-title">{{ title }}</router-link>
            <div class="artical-meta-wrap">
                <span class="post-meta-date">
                    {{ author }}|<field-time-outlined />发表于 {{ publishTime }}
                </span>
                
            </div>
            <div class="content">
                {{briefInfo.slice(0,10)+'...'}}
            </div>
        </div>
        <div class="post-cover-left">
            <router-link :to="{ name: 'article', params: { articleID: id} }" >
                <img :src="pageImg" alt="" class="post-img">
            </router-link>
        </div>
    </div>
</template>

<script>
export default {
  props: {
    title: String,
    publishTime: String,
    briefInfo: String,
    author: String,
    pageImg: String,
    id: Number
  }
}
</script>

<!-- Gen-Blog使用文檔(一) 快速開始 -->

<style scoped>
.recent-post-item{
    display: flex;
    flex-direction: row;
    max-height: 250px;
}
.post-cover-left {
    overflow: hidden;
    width: 44%;
    height: 100%;
    box-sizing: border-box;
}

.recent-post-info {
    padding: 0 40px;
    width: 57%;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: white;
    text-align: center;
}

.post-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.article-title{
    font-size: 2em;
}

.recent-post-item{
    box-sizing: border-box;
    
    background: var(--card-bg);
    margin-top: 20px;
    box-shadow: 0 3px 8px 6px rgba(7,17,27,0.09);
    border-radius: 20px 20px;
    overflow: hidden;
}

.artical-meta-wrap{
    color:#858585
}
</style>