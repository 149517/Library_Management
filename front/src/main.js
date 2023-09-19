import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router/router.js";
import store from "./store/store.js";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from "axios";


// axios.interceptors.request.use(
//     (config) => {
//         const token = localStorage.getItem('token');
//         if (token) {
//             config.headers.Authorization = `Token ${token}`;
//         } else {
//             // 如果没有令牌，您可以选择在此处执行适当的处理，例如重定向到登录页面或抛出错误
//             // 这里是一个示例，您可以根据您的需求进行更改
//             throw new Error('No token found. Please log in.');
//         }
//         return config;
//     },
//     (error) => {
//         return Promise.reject(error);
//     }
// );

// 在请求中包含 token ，如果没有token 同样也会正常发送，
// 需要登录的页面将会在当前页面进行拦截
axios.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        // console.log(token)
        if (token) {
            config.headers.Authorization = `Token ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

const app = createApp(App)
app.use(store)
app.use(router)
app.use(ElementPlus)


app.mount('#app')
