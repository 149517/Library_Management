<script>
import {mapState} from "vuex";

export default {
  data() {
    return {
      // 判断是否登录，如果localStore中含有token和pic则认为是登录状态
      login: false,
      link: [
        {
          id: 1,
          name: "数字图书",
          href: "#"
        },
        {
          id: 2,
          name: "热门必读",
          href: "/bookList"
        },
        {
          id: 3,
          name: "借阅",
          href: "/borrowing"
        },
        {
          id: 4,
          name: "查询和申报",

          href: "/table"
        },
      ]
    }
  },
  computed: {
    ...mapState(['name', 'picUrl'])
  },
  methods: {
    getPic() {
      let pic = localStorage.getItem('pic')
      if (pic !== "") {
        this.$store.commit('setPicUrl', pic)
        this.login = true
      }
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
        <div class="person" v-else>
          <img :src="picUrl" alt="">
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
  //box-shadow: 1px 0 5px #38b0815c;
  //margin: 0;
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
    img {
      width: 40px;
      height: 40px;
      border-radius: 20px;
      vertical-align: middle;
    }
  }

  .link {
    display: flex;

    div {
      line-height: 50px;
      overflow: hidden;
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