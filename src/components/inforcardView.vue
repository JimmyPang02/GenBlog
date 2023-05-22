

<template>
    <div class="card-widget card-info">
        <div class="is-center">
            <div class="avatar-img">
                <img src="../assets/avatar.png" alt="头像">
            </div>
            <div class="author-info__name">Jerry</div>
            <div class="author-info__description">A Simple and Card UI Design theme for Hexo</div>
        </div>
        <div class="card-info-data site-data is-center">
            <a href="/archives/" data-pjax-state="">
                <div class="headline">文章</div>
                <div class="length-num">17</div>
            </a>
        </div>

        <div class="card-info-social-icons is-center">
            <a-button type="primary">关注</a-button>
            
        </div>
    </div>
</template>

<style scoped>
.card-widget {
    background-color: white;
    
    top: 20px;
    overflow: hidden;
    padding: 20px 24px;
    border-radius: 8px;
    box-shadow: 0 3px 8px 6px rgba(7,17,27,0.09);
}
.is-center {
    text-align: center;
}
.avatar-img {
    overflow: hidden;
    margin: 0 auto;
    width: 110px;
    height: 110px;
    border-radius: 70px;
}
.avatar-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.card-info .author-info__name {
    font-weight: 500;
    font-size: 1.57em;
}
#aside-content .card-info .author-info__description {
    margin-top: -.42em;
}
#aside-content .card-info .card-info-data {
    margin: 14px 0 4px;
}
.site-data {
    display: flex;
    width: 100%;
    justify-content: space-evenly;
}
.card-info-social-icons .social-icon{
    color: black;
    font-weight: 900;
    color: var(--font-color);
    font-size: 1.4em;
}
#follow{
    background-color: rgb(187, 187, 233);
    border: none;
    color: white;
}
</style>