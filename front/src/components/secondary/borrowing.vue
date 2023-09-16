<<<<<<< HEAD
<script>
import {mapState} from "vuex";
import axios from "axios";
import MessageTip from "../nav/messageTip.vue";

export default {
  components: {MessageTip},
  data() {
    return {
      // 按钮是否可用
      disabled: true,
      // line显示
      play: false,
      // 控制right的值
      isRight: false,
      bookname: '',
      buttonText1: '借阅', // 第一个子组件的按钮文字
      buttonText2: '购买', // 第二个子组件的按钮文字
      books: [
        {
          fields: {
            bookname: "",
            pic: "",
            author: "",
            isbn: '',
            lang: '',
            publisher: '',
            type: '',
            price: '',
            intro: '',
            updated_time: '',
            Listing_time: ''
          }
        }
      ],
      query: [{
        name: "书名",
        value: "bookname"
      }, {
        name: "ISBN",
        value: "isbn"
      }, {
        name: "作者",
        value: "author"
      }, {
        name: "出版社",
        value: "publisher"
      }]
    }
  },
  watch: {
    bookname(newValue) {
      if (newValue !== '') {
        this.disabled = false
      }
    },
  },
  computed: {
    ...mapState(['baseUrl'])
  }
  ,
  methods: {
    check() {
      const url = this.baseUrl + '/books/query/';
      let data = new FormData();
      let index = this.$refs.sel.selectedIndex
      let value = this.$refs.sel.options[index].value;
      data.append('name', this.bookname)
      data.append('way', value)
      axios.post(url, data)
          .then((res) => {
            // console.log(res.data.books)
            if (res.data.books.length === 0) {
              alert("未检索到数据")
            }
            this.books = res.data.books
            this.play = true

          })
          .catch((err) => {
            console.log("数据提交失败" + err)
          })
    },
    borr(index) {
      let op = this.$refs.line[index].children[0];
      if (this.isRight) {
        op.style.right = "0px"
      } else {
        op.style.right = "-600px"
      }
      this.isRight = !this.isRight;

    },
    add(book, type) {
      console.log(book)
      const url = this.baseUrl + '/record/borrow/'
      let formData = new FormData()
      formData.append('isbn', book);
      formData.append('type', type)

      axios.post(url, formData)
          .then((res) => {
            console.log(res.data)
            if (type === 'borrow') {
              this.$store.commit('setBorrStatus', true)
            } else {
              this.$store.commit('setBuyStatus', true)
            }
          })
          .catch((err) => {
            if (type === 'borrow') {
              this.$store.commit('setBorrStatus', false)
            } else {
              this.$store.commit('setBuyStatus', false)
            }
            console.log(err)
          })
    }
  }
}
=======
<script setup>

>>>>>>> 326b59aa53e211a6e29b8a033e45707b234981e4
</script>

<template>
  <div class="container">
    <div class="bg">
<<<<<<< HEAD
      <div class="box">
        <form :action="this.baseUrl+'books/query/'" method="post" @submit.prevent="check">
          <p>
            书籍搜索：<input type="text" v-model="bookname">
          </p>
          <p>
            检索类别：
            <select ref="sel">
              <option v-for="item in query" :value="item.value">{{ item.name }}</option>
            </select>
          </p>
          <p>
            <button type="submit" :disabled="disabled">检索</button>
          </p>
        </form>
      </div>
      <div class="content">
        <div class="line" v-for="(item,index) in books" key="item.fields.isbn" v-if="play" ref="line"
             @click="borr(index)">
          <div class="right">
            <div class="bor" @click.stop="add(item.fields.isbn,'borrow')">
              <message-tip :buttonText="buttonText1"></message-tip>
            </div>
            <div class="buy" @click.stop="add(item.fields.isbn,'buy')">
              <message-tip :buttonText="buttonText2"></message-tip>
            </div>

          </div>
          <img :src="item.fields.pic" :alt="item.fields.bookname" v-if="item.fields.pic">
          <div class="block">
            <div class="name">{{ item.fields.bookname }}</div>
            <div class="in">
              <div class="text" v-if="item.fields.bookname !== ''">

                <p>作者: <span>{{ item.fields.author }}</span></p>
                <p>出版社：<span>{{ item.fields.publisher }}</span></p>
                <p>分类: <span>{{ item.fields.type }}</span></p>
                <p>定价:<span>{{ item.fields.price }}</span></p>
                <p>出版时间：<span>{{ item.fields.Listing_time }}</span></p>
              </div>
              <div class="intro" v-if="item.fields.intro">
                <p>介绍：<span>{{ item.fields.intro }}</span></p>
              </div>
            </div>

          </div>


        </div>

      </div>
=======
      <h2>图书借阅</h2>
>>>>>>> 326b59aa53e211a6e29b8a033e45707b234981e4
    </div>
  </div>
</template>

<style scoped lang="scss">
<<<<<<< HEAD
// 颜色变量
=======
>>>>>>> 326b59aa53e211a6e29b8a033e45707b234981e4
$aColor: #1A535E;
$btnColor: #38B081;
$bgColor: #ECFBFB;

<<<<<<< HEAD
// 公共背景样式
=======
>>>>>>> 326b59aa53e211a6e29b8a033e45707b234981e4
.bg {
  background: $bgColor;
  border-radius: 20px;
  padding: 60px 100px;
}

<<<<<<< HEAD
// 标题样式
h2 {
  margin-bottom: 30px;
}

// 表单样式
.box {
  font-size: 20px;
  font-weight: bold;

  p {
    margin: 30px 0;
  }

  input, select {
    width: 300px;
    background: white;
    padding: 10px;
    border: 2px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
  }

  button {
    width: 200px;
    padding: 10px;
    background-color: $aColor;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;

    &[disabled] {
      background: #eeaaaa;
    }
  }
}

// 内容部分样式
.content {
  // 单个内容块样式
  .line {
    display: flex;
    box-shadow: 1px 1px 8px #919191;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 30px;

    .in {
      display: flex;

      .intro {
        margin-left: 50px;
        width: 420px;
        height: 124px;
        line-height: 24px;
        word-break: break-all;
        overflow: hidden;
        display: -webkit-box;
        -webkit-line-clamp: 5;
        -webkit-box-orient: vertical;
      }
    }

    img {
      width: 120px;
      height: 180px;
      margin-right: 50px;
    }

    .name {
      font: {
        weight: bold;
        size: 20px;
      }
      color: $btnColor;
    }

    .text p,
    .intro p {
      margin: 8px 0;
      font-weight: bold;
      color: $aColor;

      span {
        font-weight: 400;
      }
    }

  }

}

.line {
  position: relative;
  top: 0;
  left: 0;
  overflow: hidden;

  .right {
    display: flex;
    width: 400px;
    height: 100%;
    font: {
      size: 42px;
      weight: bold;
    }
    color: white;
    position: absolute;
    top: 0;
    //right: 0;
    right: -600px;
    transition: all .4s ease;

    .buy,
    .bor {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 300px;
      height: 100%;
      background-color: rgba(255, 165, 0, 0.71);
    }

    .buy {
      background-color: rgba(124, 42, 136, 0.71);
    }

  }
}
=======
>>>>>>> 326b59aa53e211a6e29b8a033e45707b234981e4
</style>