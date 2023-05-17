<script setup>
import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';

// highlightjs
import hljs from 'highlight.js';

VMdEditor.use(githubTheme, {
  Hljs: hljs,
});
</script>

<template>
    <div id="post">
        <div id="article-container">
            <v-md-editor v-model="text" height="600px" @save="saveFile"></v-md-editor>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      text:`# 欢迎使用Gen-Blog
## 这是一个markdown格式的富文本编辑器
可以提供实时书写效果展示，可插入图片连接![Description](https://file.crazywong.com/gh/jerryc127/CDN@latest/Photo/categories.jpg)`,
    };
  },
  methods:{
    saveFile(text,html){
      console.log('successfully saved')
      console.log(text)
      console.log(html)
      
    }
  },
  mounted() {
    console.log(this.text)
  }
};
</script>

<style scoped>
#post{
    align-self: flex-start;
    -ms-flex-item-align: start;
    padding: 50px 40px;

    border-radius: 8px;
    background-color: white;
    box-shadow: 0 3px 8px 6px rgba(7,17,27,0.09);
    
}
#article-container{
    overflow-wrap: break-word;
    height: 100%;
}
.v-md-editor{
  height:100% !important;
}
</style>