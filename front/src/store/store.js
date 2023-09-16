import {createStore} from 'vuex'

// 创建一个新的 store 实例
const store = createStore({
    state() {
        return {
            // baseUrl: "http://127.0.0.1:8000"
            baseUrl: "http://localhost:8000",
            name:"",
<<<<<<< HEAD
            picUrl:"",
            borrowStatus:true,
            buyStatus:true,
=======
            picUrl:""
>>>>>>> 326b59aa53e211a6e29b8a033e45707b234981e4
        }
    },
    mutations: {
        setName(state,value){
            state.name = value
        },
        setPicUrl(state,value){
            state.picUrl = value
<<<<<<< HEAD
        },
        setBorrStatus(state,value){
            state.borrowStatus = value
        },
        setBuyStatus(state,value){
            state.buyStatus = value
=======
>>>>>>> 326b59aa53e211a6e29b8a033e45707b234981e4
        }
    }
})

export default store;