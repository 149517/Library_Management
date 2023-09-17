import {createStore} from 'vuex'

// 创建一个新的 store 实例
const store = createStore({
    state() {
        return {
            baseUrl: "http://127.0.0.1:8000",
            // baseUrl: "http://localhost:8000",
            name:"",
            picUrl:"",
            borrowStatus:true,
            buyStatus:true,
        }
    },
    mutations: {
        setName(state,value){
            state.name = value
        },
        setPicUrl(state,value){
            state.picUrl = value
        },
        setBorrStatus(state,value){
            state.borrowStatus = value
        },
        setBuyStatus(state,value){
            state.buyStatus = value
        }
    }
})

export default store;