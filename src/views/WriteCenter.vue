<script setup>
import Navigation from '../components/navigationView.vue';
import AiReadCard from '@/components/AiReadCard.vue';
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
            <div class="sticky">
                <AiReadCard></AiReadCard>

                <div id="aside-button">
                    <a-button type="primary" class="button">一键润色</a-button>
                </div>
            </div>

        </div>


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
    background-color: white;
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
    align-content: center;
    justify-content: center;
    
}

#aside-button .button {
    width: 100%;
}

.sticky{
    position: sticky;
    top: 20px;
}
</style>