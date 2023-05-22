<template>
    <div class="home">
        <!--这里是一个container，
            感觉就是一个固定样式的div罢了
            用于把东西放在中间
      -->
        <div class="container">
            <!--这里是card，card就是一个框，里面可以放内容-->
            <a-card>
                <!--这里是slot，slot就是一个占位符，相当于函数参数一样的东西，
                        可以允许使用这个组件的时候往这个地方加入内容-->
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
    width:100%;
}
.home{
    
    height: 100%;
    display: flex;
    align-items: center;
    justify-items: center;
}
</style>