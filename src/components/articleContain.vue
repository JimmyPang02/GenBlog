<script setup>
import VMdPreview from '@kangc/v-md-editor/lib/preview';
import '@kangc/v-md-editor/lib/style/preview.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';

// highlightjs
import hljs from 'highlight.js';

VMdPreview.use(githubTheme, {
  Hljs: hljs,
});

</script>

<template>
    <div id="post">
        <div id="article-container">
            <v-md-preview :text="text"></v-md-preview>
        </div>
    </div>
</template>

<script>
import mdfile from '../assets/Git.md?raw'
export default {
  data() {
    return {
      text: mdfile,
    };
  },
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
}
</style>