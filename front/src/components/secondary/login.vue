<script>
// import Vue from 'vue'

import {mapState} from "vuex";

import axios from "axios";



export default {
  computed: {
    ...mapState(['baseUrl'])
  },
  data() {
    return {
      // 是否是登录页面
      login: true,
      uname: '',
      password: "",
      password2: "",
      // 输入提示
      unameTip: "",
      passwordTip: "",
      password2Tip: "",
      // 控制密码可见
      psV: true,
      ps2V: true,
    }
  },
  methods: {
    clear() {
      this.uname = '';
      this.password = '';
      this.password2 = ''
    },
    Jump() {
      this.login = !this.login;
      let mid = document.querySelector('.mid');
      let btn = document.querySelectorAll('label')[2];

      if (!this.login) {
        mid.classList.add('res_mid')
      } else {
        mid.classList.remove('res_mid')
      }
    },
    check(type) {
      console.log(type)
      if (type === 'login') {
        if (this.login === '' || this.password === "") {
          alert("账号或密码不能为空")
        } else {
          this.submitForm('login')
        }
      }
      if (type === 'register') {
        if (this.login === '' || this.password === "" || this.password2 === "") {
          alert("账号或密码不能为空")
        } else {
          this.submitForm('register');
        }
      }
      return false

    },
    submitForm(type) {
      let url = this.baseUrl + '/user/'
      let formData = new FormData();
      formData.append('uname', this.uname);
      formData.append('password', this.password);

      if (type === 'login') {
        url = url + 'login/';
        this.axiosLogin(url, formData)
      }
      if (type === 'register') {
        url = url + 'register/';
        formData.append('password2', this.password2);
        this.axiosRegister(url, formData)
      }
    },
    axiosLogin(url, formData) {
      axios
          // .post(url, formData, {withCredentials: true})
          .post(url, formData)
          .then(res => {

            // console.log(res.data)

            console.log(res.data)

            if (res.data.code === 200) {
              localStorage.setItem('token', res.data.token);
              localStorage.setItem('pic', res.data.pic)
              this.$store.commit('setName', this.uname)
              this.$store.commit('setPicUrl', res.data.pic)
              this.$router.push('/')
            } else {
              alert(res.data.msg)
            }
          })
          .catch(err => {
            console.log("数据提交失败" + err)
          })
    },
    axiosRegister(url, formData) {

      // console.log(url,formData)
      axios
          .post(url, formData)
          .then((res) => {
            // console.log(res)
            if (res.data.code === 201) {
              axios
                  .post(url, formData)
                  .then(res => {
                    if (res.data.code === 201) {

                      if (confirm(res.data.msg + "，是否直接登录")) {
                        this.submitForm('login')
                      } else {
                        this.clear();
                        this.login = false;
                      }
                    } else {
                      alert(res.data.msg)
                    }
                  })
                  .catch(err => {
                    console.log("数据提交失败" + err)
                  })
            }
          })
    }
  },
  watch: {
    uname(newValue) {
      if (newValue.length < 4) {
        this.unameTip = '用户名过短'
      } else if (newValue.length > 30) {
        this.unameTip = '用户名过长'
      } else {
        this.unameTip = ""
      }
    },
    password(newValue) {
      if (newValue.length < 6) {
        this.passwordTip = '密码安全度低'
      } else if (newValue.length > 30) {
        this.passwordTip = '超出限定长度'
      } else {
        this.passwordTip = ""
      }
    },
    password2(newValue) {
      if (newValue.length < 6) {
        this.password2Tip = '密码安全度低'
      } else if (newValue.length > 30) {
        this.password2Tip = '超出限定长度'
      } else {
        this.password2Tip = ""
      }
    },
  }
}

</script>

<template>
  <div class="container">
    <div class="mid">
      <div class="left">
        <img class="img" src="../../assets/images/login/02.jpg" alt="">
      </div>
      <div class="right">
        <div class="login_bg">
          <div class="top">
            <div class="head">
              <router-link to="/">返回首页</router-link>
              <a href="javascript:void(0)" @click="Jump()" v-if="login">注册</a>
              <a href="javascript:void(0)" @click="Jump()" v-else>登录</a>

            </div>
            <h2 v-if="login">用户登录</h2>
            <h2 v-else>注册新用户</h2>
          </div>

          <form :action="this.baseUrl+'/user/login/'" ref="login" method="post" v-if="login"

                @submit.prevent="check('login')">
            <div class="box">
              <label>
                账号：<input type="text" v-model="uname" name="uname" id="uname">
              </label>
              <div>{{ unameTip }}</div>
            </div>
            <div class="box">
              <label class="pass">
                密码：<input :type="psV ? 'password' : 'text' " v-model="password" name="password" id="password">
                <div @click="psV = !psV">
                  <img v-if="!psV" src="../../assets/icon/visible.png" alt="">
                  <img v-else src="../../assets/icon/invisible.png" alt="">
                </div>
              </label>
              <div>{{ passwordTip }}</div>
            </div>

            <label>
              <button id="submit" type="submit">登录</button>
            </label>
          </form>

          <form :action="this.baseUrl+'/user/register/'" ref="register" method="post" v-else

                @submit.prevent="check('register')">
            <div class="box">
              <label>
                账号：<input type="text" v-model="uname" name="uname" id="uname">
              </label>
              <div>{{ unameTip }}</div>
            </div>
            <div class="box">
              <label class="pass">
                密码：<input :type="psV ? 'password' : 'text' " v-model="password" name="password" id="password">
                <div @click="psV = !psV">
                  <img v-if="!psV" src="../../assets/icon/visible.png" alt="">
                  <img v-else src="../../assets/icon/invisible.png" alt="">
                </div>
              </label>
              <div>{{ passwordTip }}</div>
            </div>
            <div class="box">
              <label class="pass">
                密码：<input :type="ps2V ? 'password' : 'text' " v-model="password2" name="password2" id="password2">
                <div @click="ps2V = !ps2V">
                  <img v-if="!ps2V" src="../../assets/icon/visible.png" alt="">
                  <img v-else src="../../assets/icon/invisible.png" alt="">
                </div>
              </label>
              <div>{{ password2Tip }}</div>
            </div>
            <label>
              <button id="submit" type="submit">注册</button>
            </label>
          </form>
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
$aColor: #1A535E;
$btnColor: #38B081;
$bgColor: #ECFBFB;

.container {
  //width: 100%;
  //height: calc(100vh - 80px);
  ////background: #9bdec9;
  //position: relative;
  //top: 0;
  //left: 0;
}

.mid {
  position: absolute;
  top: 50%;
  left: 50%;
  margin-top: 30px;
  display: flex;
  width: 1200px;
  height: 520px;
  background: $bgColor;
  //box-shadow: 1px 1px 10px rgb(128, 128, 128);
  border-radius: 20px;
  transform: translate(-50%, -50%);
  overflow: hidden;
  transition: all .5s linear;
}

.res_mid {
  height: 620px;
  transition: all .5s linear;
  .right{
    .login_bg{
      height: 480px;
    }
  }

}

.left {
  width: 600px;
  height: 100%;

  .img {
    margin-top: 120px;
    width: 100%;
    transition: all .3s ease;

    &:hover {
      transform: scale(1.1);
    }

  }
}

.right {
  margin: auto;

  .login_bg {
    width: 400px;
    height: 420px;
    padding: 30px 30px 0;
    background: rgb(248, 248, 248, 0.6);
    box-shadow: -6px 6px 20px 1px #d2eff1;
    border-radius: 20px;
    transition: all .5s linear;

    .top {
      .head {
        display: flex;
        justify-content: space-between;
        margin-bottom: 50px;

        a {
          color: $btnColor;
          font: {
            size: 20px;
            weight: bold;
          }
        }
      }

      h2 {
        text-align: center;
        color: $aColor;
        margin-bottom: 50px;
      }
    }

  }

  form {
    text-align: center;

    .box {
      margin-bottom: 20px;

      div {
        text-align: left;
        margin-left: 100px;
        color: red;
        font-size: 12px;
      }
    }

    label {
      display: inline-block;
      width: 300px;
      height: 50px;
      transform: translateY(50px);
      opacity: 0;
      animation: upMove .5s linear forwards;
      transition: all .5s linear;
    }

    .pass {
      position: relative;
      top: 0;
      left: 0;

      div {
        position: absolute;
        right: 15px;
        top: 10px;

        img {
          width: 24px;
          height: 24px;
        }
      }
    }

    #uname,
    #password,
    #password2 {
      height: 40px;
      width: 240px;
      padding-left: 10px;
      border: 0;
      outline: none;
      box-shadow: inset 5px 0 20px 20px white;
      border-radius: 8px;
      margin-bottom: 20px;
      background: none;
    }

    #submit {
      display: inline-block;
      width: 100px;
      height: 40px;
      border: 0;
      border-radius: 8px;
      background: $btnColor;
      font-size: 16px;
      color: white;
    }
  }
}


</style>