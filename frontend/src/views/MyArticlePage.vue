<script setup>
import innerpage from '../components/innerpageView.vue'
</script>

<template>

    <main class="layout">
        <div id="recent-post">
            <innerpage v-if="authorID" :authorID="authorID"></innerpage>

        </div>
    </main>
</template>


<script>
export default {
    props:{
        authorID: Number
    },
    mounted(){
        console.log('authorID:'+this.authorID)
    }
    
}
</script>


<style scoped>
.layout {
    display: flex;
    flex: 1 auto;
    margin: 0 auto;
    padding: 10px 15px;
    max-width: 1200px;
    width: 100%;
}

.layout #recent-post {
    width: 100%;
    -webkit-transition: all .3s;
    -moz-transition: all .3s;
    -o-transition: all .3s;
    -ms-transition: all .3s;
    transition: all .3s;
}

.mypage {
    color: white;
    position: absolute;
    text-align: center;
    top: 200px;
    padding: 0 10px;
    width: 100%;

    
}

.article_page_head{
    height: 50vh;
    background-attachment: fixed;
    background-image: url('../assets/10001.jpg');
    color: white;
    position: relative;
    width: 100%;
    background-color: #49b1f5;
    background-position: center center;
    background-size:auto;
    background-repeat: no-repeat;
}

h1 {
    color: white;
    font-size: 3em
}
</style>