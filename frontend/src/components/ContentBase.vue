<template>
    <div class="home">
        <div class="container">
            <a-card>
                <slot></slot>
            </a-card>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ContentBase',
}
</script>

<style scoped>
.container {
    margin-top: 30px;
    margin-bottom: 30px;
    width: 100%;
    align-items: center;
}

.home {

    height: 100%;
    display: flex;
    align-items: center;
    justify-items: center;
}
</style>