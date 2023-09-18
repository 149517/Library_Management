import {createRouter, createWebHashHistory} from 'vue-router'
import Home from "../components/Home.vue";
import Login from "../components/secondary/login.vue";
import BookList from "../components/secondary/bookList.vue";
import Borrowing from "../components/secondary/borrowing.vue";
import Table from "../components/secondary/table.vue"
import Details from "../components/secondary/details.vue";
import FixBook from "../components/secondary/fixBook.vue";


const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {path: '/', component: Home},
        {path: '/login', component: Login},
        {path: '/bookList', component: BookList},
        {path: '/borrowing', component: Borrowing,meta: {requiresAuth: true}},
        {path: '/table', component: Table,
            meta: {requiresAuth: true},
            children:[
                {path:'fixBook',component:FixBook}
            ]
        },
        // meta: {requiresAuth: true} 需要身份认证的路由
        {path:'/details',component:Details,meta:{requiresAuth: true}}
    ],
})

// 创建导航守卫
router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('token');

    // 如果路由需要身份验证，但没有令牌，则重定向到登录页面
    if (to.meta.requiresAuth && !token) {
        alert("请先进行登录...")
        next('/login'); // 这里的'/login'应该是您的登录页面路由
    } else {
        next(); // 继续导航
    }
});

export default router;