<template>
    <ContentBase>
        404
    </ContentBase>
</template> 
  
<script>
// @ is an alias to /src
import ContentBase from '../components/ContentBase.vue';
// 这里是导出一个对象的语法，
//这个对象有一个name属性，
//还有一个components属性，填入想要引入的组件名
export default {
    name: 'NotFoundView',
    components: { ContentBase }
}
</script >
  
<style scoped></style>