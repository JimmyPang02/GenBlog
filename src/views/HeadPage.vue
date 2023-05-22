<script setup>
import pageHeader from '../components/pageHeader.vue'
import recentPostItem from '@/components/recentPostItem.vue';
</script>

<template>
  <header class="full-page" id="page-header">
    <pageHeader></pageHeader>
  </header>

  <main class="layout">
    <div class="first-page-article">
      <recentPostItem></recentPostItem>
      <recentPostItem></recentPostItem>
      <recentPostItem></recentPostItem>
      <recentPostItem></recentPostItem>
      <recentPostItem></recentPostItem>
      <recentPostItem></recentPostItem>
    </div>
    
  </main>

  
  
</template>

<style scoped>
header.full-page {
  height: 100vh;
  background-attachment: fixed;
  background-image: url('../assets/index.png');
  color:white;
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

#menus-items a{
  color: white !important;
}
</style>
