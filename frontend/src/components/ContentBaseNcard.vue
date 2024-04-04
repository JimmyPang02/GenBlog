<template>
    <div class="home">
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