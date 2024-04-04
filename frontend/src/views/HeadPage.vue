<script setup>
import pageHeader from '../components/pageHeader.vue';
import recentPostItem from '@/components/recentPostItem.vue';
import {ref} from 'vue';

let array=ref();
let num=ref();

let myUrl = 'http://111.230.109.227:8000/api/get_random_ten_articles/';
fetch(myUrl, {
  method: 'get'
  })
  .then(response => response.json())
  .then(data => {
    console.log(data['文章列表']);
    num.value=data['文章数目'];
    array.value=data['文章列表'];
    console.log(array.value)
});

console.log("文章数："+num.value);
console.log("文章列表"+array.value);



</script>

<template>
  <header class="full-page" id="page-header">
    <pageHeader></pageHeader>
  </header>

  <main class="layout">
    <div class="first-page-article">
      <recentPostItem v-for="article in array" :title="article['文章标题']" :pageImg="article['图片url']"
      :publishTime="article['更新时间']" :briefInfo="article['文章内容']" :author="article['文章作者']" :key="article['文章id']" :id="article['文章id']"></recentPostItem>
    </div>

  </main>
</template>

<script>

</script>


<style scoped>
header.full-page {
  height: 100vh;
  background-attachment: fixed;
  background-image: url('../assets/index.png');
  color: white;
}

#page-header {
  position: relative;
  width: 100%;
  background-position: center center;
  background-size: cover;
  background-repeat: no-repeat;

}

.layout {
  flex: 1 auto;
  margin: 0 auto;
  padding: 40px 15px;
  max-width: 1200px;
  width: 100%;
}

#menus-items a {
  color: white !important;
}
</style>
