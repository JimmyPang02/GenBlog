<template>
    <div class="home">
        <!--这里是一个container，
            感觉就是一个固定样式的div罢了
            用于把东西放在中间
      -->
        <div class="container">
            <a-card bordered="false">
                <slot></slot>
            </a-card>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ContentBaseNcard',
}
</script>

<style scoped>
.container {
    margin-top: 30px;
    margin-bottom: 30px;
    padding: 0px 40px;

}
</style>