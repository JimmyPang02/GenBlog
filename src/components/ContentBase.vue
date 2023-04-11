<template>
    <div class="home">
        <div class="container">
            <!--这里是一个container，
            感觉就是一个固定样式的div罢了
            用于把东西放在中间
      -->
            <div class="card">
                <!--这里是card，card就是一个框，里面可以放内容-->
                <div class="card-body">
                    <slot></slot>
                    <!--这里是slot，slot就是一个占位符，相当于函数参数一样的东西，
                        可以允许使用这个组件的时候往这个地方加入内容-->
                </div>
            </div>
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
}
</style>