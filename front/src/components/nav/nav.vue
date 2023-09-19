<script>
import {mapState} from "vuex";
import axios from "axios";

export default {
  data() {
    return {
      // 判断是否登录，如果localStore中含有token和pic则认为是登录状态
      login: false,
      out:false,
      link: [
        {
          id: 1,
          name: "热门必读",
          href: "/bookList"
        },
        {
          id: 2,
          name: "借阅",
          href: "/borrowing"
        },
        {
          id: 3,
          name: "用户记录",
          href: "/table"
        },
        {
          id: 4,
          name: "数据申报",
          href: "/modify"
        },
      ]
    }
  },
  computed: {
    ...mapState(['name', 'picUrl','baseUrl'])
  },
  methods: {
    getPic() {
      let pic = localStorage.getItem('pic')
      if (pic !== "") {
        this.$store.commit('setPicUrl', pic)
        this.login = true
      }
    },
    logout(){
        let ele = this.$refs.logout;
        if(this.out){
          ele.classList.remove('enter')
          this.out = false
        }else{
          ele.classList.add('enter')
          this.out = true
        }
    },
    exit(){
      if(confirm("是否确定退出？")){
        let url = this.baseUrl + '/user/logout/'
        axios.get(url)
            .then((res)=>{
              localStorage.removeItem('pic');
              localStorage.removeItem('token');
              // alert(res.data.msg)
              location.reload()
            })
            .catch((err)=>{
              console.log(err)
            })
      }
    },
    fix(){

    }
  },
  watch:{
    picUrl(newValue){
      if(this.picUrl === null){
        this.login = false
      }else{
        this.login = true
      }
    }
  },
  mounted() {
    this.getPic()
    if(this.picUrl === null){
      this.login = false
    }
  }

}
</script>

<template>

  <div class="container">
    <div class="top">
      <div class="logo">
        <!--        曦林图书-->
        <img @click="this.$router.push('/')" src="../../assets/images/logo2.png" alt="">
      </div>
      <div class="link">
        <div v-for="item in link" key="item.id">
          <router-link :to="item.href">{{ item.name }}</router-link>
          <span ref="op"></span>
        </div>
        <div class="login" v-if="!login">
          <router-link to="/login">Sign in</router-link>
          <div></div>
        </div>
        <div class="person" v-else @click="logout()">
          <img :src="picUrl" alt="">
          <div class="logout" ref="logout">
            <div class="out" @click.stop="exit()">
              退出登录
            </div>
            <div class="fix" @click.stop="fix()">
              账户修改
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
$aColor: #1A535E;
$btnColor: #38B081;
$bgColor: #ECFBFB;

.container{
}
.top {
  height: 80px;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;

  .logo {
    height: 60px;
    font: {
      weight: bold;
      size: 40px;
    }
    letter-spacing: 5px;

    img {
      height: 60px;
    }
  }

  .person {
    position: relative;
    top: 0;
    left: 0;
    img {
      width: 40px;
      height: 40px;
      border-radius: 20px;
      vertical-align: middle;
    }
    .logout{
      position: absolute;
      top: 54px;
      right: -60px;
      z-index: 9;
      opacity: 0;
      width: 100px;
      height: 80px;
      transition: all .5s ease;
      div{
        cursor: pointer;
        height: 40px;
        line-height: 40px;
        text-align: center;
        margin-top: 5px;
        color: white;
        border-radius: 10px;
        background: $btnColor;
      }
    }
    .enter{
      right: -10px;
      opacity: 1;
    }
  }

  .link {
    display: flex;

    div {
      line-height: 50px;
      transition: all .3s linear;

      span {
        display: block;
        width: 0;
        height: 3px;
        background: green;
        transition: all .3s linear;
      }

      a {
        display: block;
        padding-right: 40px;
        color: $aColor;
        font: {
          weight: bold;
          size: 18px;
        }
      }
    }

    div:hover span {
      width: calc(100% - 40px);
    }
  }

  .login {
    position: relative;
    top: 0;
    left: 0;
    transition: all .3s linear;
    border-radius: 4px;

    a {
      color: $btnColor;
      //padding-right: 20px;
      padding-left: 40px;
      border: 2px solid $btnColor;
    }

    div {
      position: absolute;
      top: 0;
      left: 0;
      z-index: -1;
      height: 100%;
      width: 0;
      background: $btnColor;
    }
  }

  .login:hover div {
    width: 100%;
  }

  .login:hover a {
    color: white;
  }
}


</style>