import {createRouter, createWebHashHistory} from 'vue-router'
import Home from "../components/Home.vue";
import Login from "../components/secondary/login.vue";
import BookList from "../components/secondary/bookList.vue";
import Borrowing from "../components/secondary/borrowing.vue";
<<<<<<< HEAD
import Table from "../components/secondary/table.vue"

=======
>>>>>>> 326b59aa53e211a6e29b8a033e45707b234981e4


const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {path: '/', component: Home},
        {path: '/login', component: Login},
        {path: '/bookList', component: BookList},
        {path: '/borrowing', component: Borrowing},
<<<<<<< HEAD
        {path: '/table', component: Table},

=======
>>>>>>> 326b59aa53e211a6e29b8a033e45707b234981e4
    ],
})

export default router;