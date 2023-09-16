import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router/router.js";
import store from "./store/store.js";
<<<<<<< HEAD
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from "axios";


axios.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Token ${token}`;
        } else {
            // 如果没有令牌，您可以选择在此处执行适当的处理，例如重定向到登录页面或抛出错误
            // 这里是一个示例，您可以根据您的需求进行更改
            throw new Error('No token found. Please log in.');
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
=======


const app = createApp(App)
app.use(store)
app.use(router)

>>>>>>> 326b59aa53e211a6e29b8a033e45707b234981e4

app.mount('#app')
