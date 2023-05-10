<script setup>
import Navigation from '../components/navigationView.vue';
import Inforcard from '../components/inforcardView.vue';
import richTextEditor from '../components/richTextEditor.vue';
</script>

<template>
    <header class="navigation">
        <navigation></navigation>
    </header>

    <main class="layout">
        <div id="recent-post">
            <richTextEditor></richTextEditor>
        </div>

        <div id="aside-content">
            <Inforcard></Inforcard>
        </div>
    </main>
</template>



<style scoped>
.layout {
    
    display: flex;
    flex: 1 auto;
    margin: 0 auto;
    padding: 40px 15px;
    max-width: 1200px;
    width: 100%;
}
.layout #recent-post {
    background-color: white;
    width: 74%;
}

#aside-content {
    padding-left: 15px;
    width: 26%;
    
}

span a{
    color:black;
}
</style>