import $ from "jquery";
import jwt_decode from "jwt-decode";

const ModuleUser = {
    state: {
        username: "",
        id: 1,//这里要给个初值
        firstName: "",
        lastName: "",
        photo:"",
        followerCount: 0,
        access: "",
        refresh: "",
        is_login:false,
    },
    getters: {
    },
    mutations: {
        //(3)根据获取的用户信息，存到全局变量state中
        updateUser(state, data) {
            state.id = data.id;
            state.username = data.username;
            state.photo = data.photo;
            state.followerCount = data.followerCount;
            state.access = data.access;
            state.refresh = data.refresh;
            state.is_login = data.is_login;            
        },
        updateAccess(state, data) {
            state.access=data.access
        },
        logout(state) {
            state.id = "";
            state.username = "";
            state.photo = "";
            state.followerCount = "";
            state.access = "";
            state.refresh = "";
            state.is_login = false;
        }
    },
    actions: {
        //data是我们传递的值，如username和password
        login(context, data) {
            //(1)根据账号密码，获取JWT token，保存access和refresh值
            $.ajax({
                url: "https://app165.acapp.acwing.com.cn/api/token/",
                type: "POST",
                data: {
                    username: data.username,
                    password: data.password
                },
                success(resp) {
                    const { access, refresh } = resp;

                    const access_obj = jwt_decode(access);
                    //(2)根据token中的userid，获取用户信息
                    $.ajax({
                        url: "https://app165.acapp.acwing.com.cn/myspace/getinfo/",
                        type: "GET",
                        data: {
                            user_id: access_obj.user_id
                        },
                        //jwt验证
                        headers: {
                            'Authorization': "Bearer " + access
                        },
                        success(resp) {
                            //(3)根据获取的用户信息，存到全局变量state中
                            //but修改state的函数得在mutation里面写，具体函数见：mutation

                            //（4）调用mutation的updateUser函数
                            context.commit("updateUser", {
                                ...resp, //将resp解构(一些用户信息)
                                access: access,//再补充一些用户信息
                                refresh: refresh,
                                is_login: true,
                            })
                            console.log(resp)
                            // （5）调用组件传过来的回调函数，表示登录成功
                            data.success()
                        }
                    });

                    //每5分钟根据refresh值去获取最新的access值
                    //【疑问】：可是我觉得不应该写着这里啊，
                    //这里是输入了账号密码才会激活的函数，
                    //最终还是得输入账号密码，才会用到这个代码）
                    //【回答】：写了setInterval以后,
                    //只会定期执行包裹住的代码,
                    //并不依赖于代码所在的位置
                    setInterval(()=>{
                        $.ajax({
                            url: "https://app165.acapp.acwing.com.cn/api/token/refresh/",
                            type: "POST",
                            data: {
                                refresh: refresh
                            },
                            success(resp) {
                                //调用mutation的更新access的函数
                                context.commit("updateAccess", resp)
                                console.log(resp)
                            }
                        })
                    }, 1000 * 60 * 4.5);
                    //这里的1000是1000毫秒，即1秒
                    //这里设置4分半就刷新一次access
                },
                //（5）如果登录失败，同样调用组件传来的回调函数
                error() {
                    data.error()
                }
            });
        },
        register(context,data) {
            //后端实现：
            //先查询数据库，用户名是否存在，然后判断两次输入的密码是否一致，如果通过，则写入数据库
            $.ajax({
                url: "https://app165.acapp.acwing.com.cn/myspace/user/",
                type: "POST",
                data: {
                    username: data.username,
                    password: data.password,
                    password_confirm:data.password2
                },
                success(resp) {
                    if (resp.result == 'success') {
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