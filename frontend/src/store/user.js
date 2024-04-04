import $ from "jquery";
import API_ROUTES from "@/api/api";
import { backendIP } from "@/api/backend"; 
    
const ModuleUser = {
    state: {
        username: "",
        id: 1,//这里要给个初值
        description: "",
        photo:"",
        followerCount: 0,
        fanCount: 0,
        postCount: 0,
        access: "",
        is_login:false,
    },
    getters: {
    },
    mutations: {
        //(3)根据获取的用户信息，存到全局变量state中
        updateUser(state, data) {
            state.id = data["当前用户id"];
            state.username = data["当前用户名"];
            state.photo = data["头像链接"];
            state.description = data["自我介绍"];
            state.followerCount = data["关注数"];
            state.fanCount = data["粉丝数"];
            state.postCount = data["文章数"];
            state.access = data.access;
            state.is_login = data.is_login;
            // 存储到本地, 用于页面刷新时的登录状态保持
            localStorage.setItem("access", data.access);
        },
        updateAccess(state, data) {
            state.access=data.access
        },
        logout(state) {
            state.id = "";
            state.username = "";
            state.photo = "";
            state.description = "";
            state.followerCount = "";
            state.fanCount = "";
            state.postCount = "";
            state.access = "";
            state.is_login = false;
            // 清除本地存储
            localStorage.removeItem("access");
        }
    },
    actions: {
        //调用后端接口，获取用户信息
        getUserInfo(context,access) {
             $.ajax({
                url:  backendIP+API_ROUTES.UserInfo,
                type: "POST",
                data: {
                    access_token: access,
                },
                 success(resp) {
                    if (resp.result == '获取用户信息成功'){
                        //调用mutation的updateUser函数，把获取的用户信息，存到全局变量state中
                        context.commit("updateUser", {
                            ...resp, //将resp解构(一些用户信息)
                            access: access,//再补充一些用户信息
                            is_login: true,
                        })
                     }
                    else {
                        console.log(resp)
                    }
                }
            });
        }, 
        login(context, data) {
            //data是我们传递的值，如username和password
            //根据账号密码，获取JWT token，保存access值
            $.ajax({
                url: backendIP+API_ROUTES.login,
                type: "POST",
                data: {
                    username: data.username,
                    password: data.password
                },
                success(resp) {
                    if (resp.result == '登录成功，生成jwt令牌') {
                        const access = resp.access_token;
                        context.dispatch('getUserInfo', access); // 登陆成功后，调用getUserInfo函数，获取用户信息
                        data.success() // 如果登录成功调用组件传来的回调函数（跳转首页等）
                    }
                    //如果登录失败调用组件传来的回调函数
                    else {
                        data.error(resp.result)
                    }
                },
  
            });
        },
        register(context,data) {
            $.ajax({
                url: backendIP+API_ROUTES.register,
                type: "POST",
                data: {
                    username: data.username,
                    password: data.password,
                    password_confirm:data.password2
                },
                success(resp) {
                    if (resp.result == '注册成功') {
                        data.success()
                    }
                    else {
                        data.error(resp.result)
                    }
                }
            })
        }
    },
    modules: {
    }
};

export default ModuleUser;