<script setup>
import articleContain from '../components/articleContain.vue'
import Navigation from '../components/navigationView.vue';
import Inforcard from '../components/inforcardView.vue';
import AiReadCard from '@/components/AiReadCard.vue';
</script>

<template>
    <header class="article_page_head">
        <div class="navigate">
            <Navigation></Navigation>
            <div class="mypage">
                <h1 class="site-title" style="color:white">javascript教程</h1>
            </div>
        </div>
    </header>

    <main class="layout">
        <div id="recent-post">
            <articleContain></articleContain>

        </div>
        <div id="aside-content">
            <Inforcard></Inforcard>
            <div class="sticky">
                <AiReadCard></AiReadCard>
                <div id="aside-button">
                    <a-button type="primary" class="button">提炼文章内容</a-button>
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
    max-width: 1200px;
    width: 100%;
}

.layout #recent-post {
    width: 74%;
    -webkit-transition: all .3s;
    -moz-transition: all .3s;
    -o-transition: all .3s;
    -ms-transition: all .3s;
    transition: all .3s;
}

#aside-content {
    padding-left: 15px;
    width: 26%;

}

.mypage {
    color: white;
    position: absolute;
    text-align: center;
    top: 45%;
    padding: 0 10px;
    width: 100%;


}

.article_page_head {
    height: 50vh;
    background-attachment: fixed;
    background-image: url('../assets/10001.jpg');
    color: white;
    position: relative;
    width: 100%;
    background-color: #49b1f5;
    background-position: center center;
    background-size: auto;
    background-repeat: no-repeat;
}

h1 {
    color: white;
    font-size: 3em
}

a {
    color: black !
}

#recent-post {
    display: flex;
}

#aside-button {
    margin-top: 10px;
    display: flex;
    align-content: center;
    justify-content: center;
    
}
.sticky{
    margin-top:20px;
    position: sticky;
    top: 20px;
}

#aside-button .button {
    width: 100%;
}
</style>