<script setup>
import recentPostItem from './recentPostItem.vue';
</script>

<template>
    <div class="recent-posts" id="recent-posts">
        <div class="item">
            <recentPostItem></recentPostItem>
            <div class="buttons">
                <a-button type="primary" id="edit">编辑</a-button>
                <a-button  danger id="delete">删除</a-button>
            </div>
        </div>
        <div class="item">
            <recentPostItem></recentPostItem>
            <div class="buttons">
                <a-button type="primary" id="edit">编辑</a-button>
                <a-button  danger id="delete">删除</a-button>
            </div>
        </div>
        <div class="item">
            <recentPostItem></recentPostItem>
            <div class="buttons">
                <a-button type="primary" id="edit">编辑</a-button>
                <a-button  danger id="delete">删除</a-button>
            </div>
        </div>
        <div class="item">
            <recentPostItem></recentPostItem>
            <div class="buttons">
                <a-button type="primary" id="edit">编辑</a-button>
                <a-button  danger id="delete">删除</a-button>
            </div>
        </div>
        <div class="item">
            <recentPostItem></recentPostItem>
            <div class="buttons">
                <a-button type="primary" id="edit">编辑</a-button>
                <a-button  danger id="delete">删除</a-button>
            </div>
        </div>
        <div class="item">
            <recentPostItem></recentPostItem>
            <div class="buttons">
                <a-button type="primary" id="edit">编辑</a-button>
                <a-button danger id="delete">删除</a-button>
            </div>
        </div>
        <div class="item">
            <recentPostItem></recentPostItem>
            <div class="buttons">
                <a-button type="primary" id="edit">编辑</a-button>
                <a-button  danger id="delete">删除</a-button>
            </div>
        </div>
    </div>
    
</template>

<style scoped>
.recent-post{
    width:100%
}

.buttons{
    display:flex;
    justify-content: flex-end;
}
.buttons button{
    width:100px;
    margin:10px;
}
</style>