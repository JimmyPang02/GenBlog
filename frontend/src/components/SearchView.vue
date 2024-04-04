<script setup>
import { ref } from 'vue';
import recentPostItem from './recentPostItem.vue';
import { message } from 'ant-design-vue';
const value = ref('');
const onSearch = searchValue => {
  console.log('use value', searchValue);
  console.log('or use this.value', value.value);
  if (!searchValue) {
    message.info('搜索内容为空')
  }
  else {
    search(searchValue)
    showModal();
  }

};

const visible = ref(false);
const showModal = () => {
  visible.value = true;
};
const handleOk = e => {
  console.log(e);
  visible.value = false;
};

//文章列表
let array = ref()
function search(searchValue) {
  var myHeaders = new Headers();
  myHeaders.append("User-Agent", "Apifox/1.0.0 (https://www.apifox.cn)");

  var formdata = new FormData();
  formdata.append("keyword", searchValue);

  var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: formdata,
    redirect: 'follow'
  };

  fetch("http://111.230.109.227:8000/api/search_article_by_keyword/", requestOptions)
    .then(response => response.json())
    .then(result => {

      array.value = result["文章列表"]
      console.log(array.value);
    })
    .catch(error => console.log('error', error));
}
</script>
<template>
  <a-space direction="vertical">
    <a-input-search v-model="value" placeholder="input search text" style="width: 200px" @search="onSearch">
    </a-input-search>
  </a-space>
  <div>
    <a-modal v-model:visible="visible" width="1000px" title="搜索结果" @ok="handleOk" class="layout">
      <div class="item" v-for="article in array" :key="article['文章id']">
            <recentPostItem :title="article['文章标题']" :pageImg="article['图片url']" :publishTime="article['更新时间']"
                :briefInfo="article['文章内容']" :author="article['文章作者']" :id="article['文章id']"></recentPostItem>
        </div>
    </a-modal>
  </div>
</template>
  
<style scoped>
.layout{
  max-height: 80vh;
  overflow-block: scroll;
}
</style>