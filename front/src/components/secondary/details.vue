<script>
import axios from "axios";
import {mapState} from "vuex";
import MessageTip from "../nav/messageTip.vue";

export default {
  components: {MessageTip},
  data() {
    return {
      isbn: '',
      buttonText1: '借阅', // 第一个子组件的按钮文字
      buttonText2: '购买', // 第二个子组件的按钮文字
      book: {
        Listing_time: '',
        author: "",
        bookname: '',
        intro: '',
        isbn: "",
        lang: "",
        pic: "",
        price: "",
        publisher: "",
        type: "",
        updated_time: "",
      }
    }
  },
  computed: {
    ...mapState(['baseUrl'])
  },
  methods: {
    getData() {
      /**
       * 获取指定的ISBN的书籍信息
       * way,指定搜索的方式为ISBN
       *
       * */
      const url = this.baseUrl + '/books/query/'
      let formData = new FormData();
      formData.append('name', this.isbn)
      formData.append('way', 'isbn')
      axios.post(url, formData)
          .then((res) => {
            console.log(res.data)
            this.book = res.data.books[0].fields;
          })
          .catch((err) => {
            console.log(err)
          })
    },
    add(book, type) {
      /**
       * 通过用户操作添加到书籍为当前用户的记录（借入或者购买）
       *
       * 参数：
       * book 书籍的ISBN
       * type 借书或者是购买
       * */
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

  },

  mounted() {
    this.isbn = this.$route.query.isbn
    // console.log(this.isbn)
    this.getData()
  }
}
</script>

<template>
  <div class="container">
    <div class="bg">
      <div class="box">
        <div class="op">
          <div class="bor" @click.stop="add(this.isbn,'borrow')">
            <message-tip :buttonText="buttonText1"></message-tip>
          </div>
          <div class="buy" @click.stop="add(this.isbn,'buy')">
            <message-tip :buttonText="buttonText2"></message-tip>
          </div>
        </div>
        <div class="block">
          <img :src="book.pic" alt="">
          <div class="text">
            <p>书名：<span>{{ book.bookname }}</span></p>
            <p>作者：<span>{{ book.author }}</span></p>
            <p>语言：<span>{{ book.lang }}</span></p>
            <p>定价：<span>{{ book.price }}</span></p>
            <p>类型：<span>{{ book.type }}</span></p>
            <p>出版社：<span>{{ book.publisher }}</span></p>
            <p>ISBN：<span>{{ book.isbn }}</span></p>
            <p>出版日期：<span>{{ book.Listing_time }}</span></p>
          </div>
        </div>
        <p class="intro">介绍：<span>{{ book.intro }}</span></p>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
$aColor: #1A535E;
$btnColor: #38B081;
$bgColor: #ECFBFB;

.bg {
  background: $bgColor;
  border-radius: 20px;
  padding: 50px 80px;
}

.box {
  position: relative;
  top: 0;
  left: 0;
  .block {
    display: flex;

    img {
      border-radius: 5px;
      margin-right: 30px;
    }

    .text {
      margin-top: 20px;
      font-size: 22px;

      p {
        margin: 8px 0;
        font-weight: bold;
        color: $aColor;

        span {
          font-weight: 400;
        }
      }
    }
  }

  .intro {
    margin-top: 30px;
    font-size: 24px;
    font-weight: bold;
    color: $aColor;
    span {
      font-weight: 400;
    }
  }
  .op{
    width: 200px;
    height: 200px;
    border-radius: 10px;
    display:flex;
    flex-direction: column;
    position: absolute;
    top: 20px;
    right: 80px;
    .bor{
      text-align: center;
      line-height: 100px;
      flex: 1;
      background: #9bdec9;
      border-radius: 8px;
    }
    .buy{
      text-align: center;
      line-height: 100px;
      flex: 1;
      background: #79dbea;
      border-radius: 8px;
    }
  }

}
</style>