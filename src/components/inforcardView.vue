
<template>
    <div class="card-widget card-info">
        <div class="is-center">
            <div class="avatar-img">
                <img :src="imgUrl" alt="头像">
            </div>
            <div class="author-info__name">{{ authorName }}</div>
            <div class="author-info__description">{{ authorIntroduce }}</div>
        </div>
        <div class="card-info-data site-data is-center">
            <div style="color:rgb(44, 116, 209)">
                <div class="headline">文章</div>
                <div class="length-num">{{ articleNum }}</div>
            </div>
        </div>

        <div class="card-info-social-icons is-center">
            <a-button type="primary">关注</a-button>

        </div>
    </div>
</template>

<script>
//import {ref} from 'vue';

export default {
    props: {
        authorId: Number
    },
    data() {
        return {
      articleNum: 0,
      authorName: '',
      authorIntroduce: '',
      imgUrl: ''
    }
  },
    mounted() {
        console.log(this.authorId)
        console.log('aaaaaa')
        var myHeaders = new Headers();
        myHeaders.append("User-Agent", "Apifox/1.0.0 (https://www.apifox.cn)");

        var formdata = new FormData();
        formdata.append("user_id", this.authorId);

        var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: formdata,
            redirect: 'follow'
        };

        fetch("http://111.230.109.227:8000/api/get_user_info_by_id/", requestOptions)
            .then(response => response.json())
            .then(result => {
                console.log(result);
                this.articleNum=result['文章数'];
                this.authorName=result['当前用户名'];
                this.authorIntroduce=result['自我介绍'];
                this.imgUrl=result['头像链接']
                console.log(this.articleNum)
            })
            .catch(error => console.log('error', error));
    }
}



</script>

<style scoped>
.card-widget {
    background-color: white;

    top: 20px;
    overflow: hidden;
    padding: 20px 24px;
    border-radius: 8px;
    box-shadow: 0 3px 8px 6px rgba(7, 17, 27, 0.09);
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

.card-info-social-icons .social-icon {
    color: black;
    font-weight: 900;
    color: var(--font-color);
    font-size: 1.4em;
}

#follow {
    background-color: rgb(187, 187, 233);
    border: none;
    color: white;
}
</style>