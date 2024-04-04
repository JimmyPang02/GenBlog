<script setup>
import navigation from './navigationView.vue'
import { DownOutlined } from '@ant-design/icons-vue';

</script>

<template>
    <navigation></navigation>

    <div id="site-info">
        <h1 id="site-title" style="color:white">Gen-Blog</h1>
        <div id="site-subtitle">
            一款AI生成式轻博客网站
            
        </div>
    </div>

    <div id="scroll-down">
        <down-outlined />
    </div>
</template>

<style scoped>
#site-info {
    color: white;
    position: absolute;
    text-align: center;
    top: 43%;
    padding: 0 10px;
    width: 100%;
    background: var(--global-bg);
}

.title {

    text-shadow: 2px 2px 4px rgba(0, 0, 0, .15);
    line-height: 1.5;
}

#scroll-down {
    bottom: 0;
    text-align: center;
    position: absolute;
    width: 100%;
    color: var(--light-grey);
    font-size: 30px;
}

h1 {
    color: white;
    font-size: 3em
}
</style>