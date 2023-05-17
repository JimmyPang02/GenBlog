<script setup>
import Navigation from '../components/navigationView.vue';
import AiReadCard from '@/components/AiReadCard.vue';
import richTextEditor from '../components/richTextEditor.vue';
import { ref } from 'vue';

const loading = ref(false);
const visible = ref(false);
const showModal = () => {
    console.log('show modal')
    visible.value = true;
};
const handleOk = () => {
    loading.value = true;
    setTimeout(() => {
        loading.value = false;
        visible.value = false;
    }, 2000);
};
const handleCancel = () => {
    visible.value = false;
};
</script>

<template>
    <header class="navigation">
        <navigation></navigation>
    </header>

    <main class="layout">
        <div id="recent-post">
            <richTextEditor></richTextEditor>
        </div>

        <div id="aside-content">
            <div class="sticky">
                <AiReadCard></AiReadCard>

                <div id="aside-button">
                    <a-button type="primary" class="button">一键润色</a-button>
                    <a-button type="primary" class="submit-button" @click="showModal">上传文章</a-button>
                </div>
            </div>

        </div>

        <div class="submit-modal">
            <a-modal v-model:visible="visible" title="输入要保存的文章标题" @ok="handleOk">
                <template #footer>
                    <a-button key="back" @click="handleCancel">取消</a-button>
                    <a-button key="submit" type="primary" :loading="loading" @click="handleOk">确定</a-button>
                </template>
                <a-input-group compact>
                    <a-input v-model:value="value19" style="width: calc(100% - 200px)" />
                </a-input-group>
            </a-modal>
        </div>
    </main>
</template>



<style scoped>
.layout {

    display: flex;
    flex: 1 auto;
    margin: 0 auto;
    padding: 40px 15px;
    max-width: 1300px;
    width: 100%;
}

.layout #recent-post {
    background-color: white;
    width: 80%;
}

#aside-content {
    padding-left: 15px;
    width: 20%;

}

span a {
    color: black;
}

#aside-button {
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    align-content: center;
    justify-content: center;

}

#aside-button .button {
    width: 100%;
}

.sticky {
    position: sticky;
    top: 20px;
}

.submit-button {
    margin-top: 10px;
}

.submit-modal {
    margin-top: 100px;
}
</style>