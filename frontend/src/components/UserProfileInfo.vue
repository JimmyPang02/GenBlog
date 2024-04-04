<template>
    <a-card :bordered="true" style="width: 100%; margin: 30px auto;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); text-align: center;">
        <div class="user-info">
            <a-avatar :src="user.photo" :size="{ xs: 70, sm: 80, md: 100, lg: 130, xl: 150, xxl: 170 }" />
            <div class="user-details">
                <h2 class="username">{{ user.username }}</h2>
                <h5 class="userintro">
                    {{ user.description ? user.description : '这个人很懒,没有留下简介' }}
                </h5>
            </div>
        </div>
        <a-divider style="margin: 16px 0;" />
        <div class="user-stats">
            <a-row :gutter="8">
                <a-col :span="8">
                    <TeamOutlined />
                    <a-statistic title="关注" :value="user.followerCount">
                    </a-statistic>
                </a-col>
                <a-col :span="8">
                    <TeamOutlined />
                    <a-statistic title="粉丝" :value="user.fanCount">
                    </a-statistic>
                </a-col>
                <a-col :span="8">
                    <FormOutlined />
                    <a-statistic title="文章" :value="user.postCount">
                    </a-statistic>
                </a-col>
            </a-row>
        </div>
        <div class="user-actions">
            <div v-if="is_me">
                <a-button class="action-button" size="middle" type="primary" @click="showEditbox">
                    <FormOutlined />
                    编辑个人资料
                </a-button>
                <a-modal v-model:visible="visible" title="编辑个人资料" :ok-text="isEditing ? '保存' : '确定'"
                    :cancel-text="isEditing ? '取消' : '关闭'" @ok="handleSave" @cancel="handleCancel">
                    <div class="user-info" style="text-align: center;">
                        <a-avatar :src="editedUser.photo" :size="{ xs: 70, sm: 80, md: 100, lg: 130, xl: 150, xxl: 170 }" />
                        <div class="user-details">
                            <h5 class="userintro">
                                <a-input v-model:value="editedUser.photo" :rows="4" :placeholder="'图片URL'" />
                            </h5>
                            <h5 class="userintro">
                                <a-input v-model:value="editedUser.description" :rows="4" :placeholder="'这个人很懒，没有留下简介'" />
                            </h5>
                        </div>
                    </div>
                </a-modal>
            </div>
            <div v-else>
                <a-button class="action-button" size="middle" type="primary" @click="follow" v-if="!user.is_followed">
                    <UserAddOutlined />
                    关注
                </a-button>
                <a-button class="action-button" size="middle" @click="unfollow" v-if="user.is_followed">
                    <UserDeleteOutlined />
                    取消关注
                </a-button>
            </div>
            <a-icon type="plus"></a-icon>
        </div>
    </a-card>
</template>

<script>
import $ from 'jquery';
import { useStore } from 'vuex';
import { UserAddOutlined, TeamOutlined, FormOutlined, UserDeleteOutlined } from '@ant-design/icons-vue';
import API_ROUTES from "@/api/api";
import { backendIP } from "@/api/backend";
import { computed, reactive } from 'vue';
import { ref } from 'vue';

export default {
    name: 'UserProfileInfo',
    components: { UserAddOutlined, TeamOutlined, FormOutlined, UserDeleteOutlined },
    props: {
        user: {
            type: Object,
            required: true
        }
    },
    setup(props, context) {
        const store = useStore();
        const is_me = computed(() => { return props.user.id == store.state.user.id })//判断当前的用户界面是不是自己的userID

        let visible = ref(false); // 控制编辑个人资料的弹窗显示
        let isEditing = ref(false); // 判断是否正在编辑
        let editedUser = reactive({}); // 编辑个人资料的临时变量

        // 编辑个人资料窗口的显示
        const showEditbox = () => {
            visible.value = true;
            isEditing.value = false; // false: 显示确定按钮; true: 显示保存按钮
            editedUser.description = props.user.description;
            editedUser.photo = props.user.photo;
        };

        // 编辑个人资料窗口的保存和取消
        const handleSave = () => {
            if (isEditing.value) {
                console.log(editedUser);
                // 后端保存
                $.ajax({
                    url: backendIP + API_ROUTES.editProfile,
                    type: "POST",
                    data: {
                        access_token: store.state.user.access,
                        self_introduction: editedUser.description,
                        avatar_url: editedUser.photo
                    },
                    success(resp) {
                        if (resp.result == '修改用户信息成功') {
                            context.emit("save", editedUser)
                            console.log("修改用户信息成功");
                        }
                        else {
                            console.log("修改用户信息失败");
                        }
                    }
                })
                isEditing.value = false;
                visible.value = false;
            } else {
                isEditing.value = true;
            }
        };
        const handleCancel = () => {
            if (isEditing.value) {
                isEditing.value = false;
                editedUser.description = props.user.description;
                editedUser.photo = props.user.photo;
            } else {
                visible.value = false;
            }
        };

        const follow = () => {
            // 后端关注
            $.ajax({
                url: backendIP + API_ROUTES.follow,
                type: "POST",
                data: {
                    access_token: store.state.user.access,
                    follow_user_id: props.user.id
                },
                success(resp) {
                    if (resp.result == '关注用户成功') {
                        //后端成功则进行前端修改，保持数据一致性
                        context.emit("follow")
                        console.log("关注成功");
                    }
                    else {
                        console.log("关注失败");
                    }
                }
            })
        };
        const unfollow = () => (

            // 后端保证取消关注
            $.ajax({
                url: backendIP + API_ROUTES.unfollow,
                type: "POST",
                data: {
                    access_token: store.state.user.access,
                    unfollow_user_id: props.user.id
                },
                //后端成功则进行前端修改，保持数据一致性
                success(resp) {
                    if (resp.result == '取消关注用户成功') {
                        context.emit("unfollow")
                        console.log("取消关注成功");
                    }
                    else {
                        console.log("取消关注失败");
                    }
                }
            })
        );
        return { follow, unfollow, is_me, showEditbox, handleSave, handleCancel, visible, isEditing, editedUser };//, editedUserRefs };
    }
}
</script>

<style scoped>
.image-field {
    display: flex;
    flex-direction: column;
    justify-content: center;
}


/* 指定圆形图片 */
img {
    border-radius: 50%;
}

.fans {
    font-size: 14px;
    color: #999;
}

button {
    margin-top: 10px;
}
</style>
