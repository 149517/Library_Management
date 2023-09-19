<script>
import axios from "axios";
import {mapState} from "vuex";

export default {
  data() {
    return {
      borrow: true,
      buy: false,
      fix: false,
      borrowData: [{
        time:'',
        book: {
          title: '',
          author: '',
          price: '',
          publisher: '',
          isbn: ''
        }
      }],
    }
  },
  computed: {
    ...mapState(['baseUrl'])
  },
  methods: {
    toggle(type) {
      if (type === 'borrow') {
        this.borrow = true;
        this.buy = false
        this.getRecord('borrow')
      } else if (type === 'buy') {
        this.borrow = false;
        this.buy = true
        this.getRecord('buy')
      } else {
        this.borrow = false;
        this.buy = false

      }
    },
    getRecord(type) {
      const url = this.baseUrl + '/record/getRecord/';
      let formData = new FormData();
      formData.append('type', type)
      axios
          .post(url, formData)
          .then((res) => {
            this.borrowData = res.data.records
          })
          .catch((err) => {
            console.log(err)
          })
    }
  },
  mounted() {
    this.getRecord('borrow')
  }
}
</script>

<template>
  <div class="main">
    <div class="category">
      <div class="block bg">
        <h2 :class="{'active':borrow}" @click="toggle('borrow')">我的借阅</h2>
        <h2 :class="{'active':buy}" @click="toggle('buy')">购书记录</h2>
        <h2 :class="{'active':fix}" @click="toggle('fix')">错误修订</h2>
      </div>

    </div>
    <div class="content">
      <div class="view" v-if="borrow">
        <table>
          <thead>
          <tr>
            <th>借阅时间</th>
            <th>书籍</th>
            <th>作者</th>
            <th>ISBN</th>
            <th>价格</th>
            <th>出版社</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="item in borrowData">
            <td>{{item.time.split('T')[0]}}</td>
            <td>{{ item.book.title }}</td>
            <td>{{ item.book.author }}</td>
            <td>{{ item.book.isbn }}</td>
            <td>{{ item.book.price }}</td>
            <td>{{ item.book.publisher }}</td>
          </tr>
          </tbody>
        </table>
      </div>

      <div class="view" v-if="buy">
        <table>
          <thead>
          <tr>
            <th>购买日期</th>
            <th>书籍</th>
            <th>作者</th>
            <th>ISBN</th>
            <th>价格</th>
            <th>出版社</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="item in borrowData">
            <td>{{item.time.split('T')[0]}}</td>
            <td>{{ item.book.title }}</td>
            <td>{{ item.book.author }}</td>
            <td>{{ item.book.isbn }}</td>
            <td>{{ item.book.price }}</td>
            <td>{{ item.book.publisher }}</td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>


</template>

<style scoped lang="scss">
// 颜色变量
$aColor: #1A535E;
$btnColor: #38B081;
$bgColor: #ECFBFB;
.main {
  padding: 30px 80px;
  display: flex;
}

// 公共背景样式
.bg {
  background: $bgColor;
  border-radius: 20px;
}

.category {
  width: 200px;

  .block {
    text-align: center;
  }

  h2 {
    padding: 20px 0;
    color: $btnColor;
    transition: all .5s linear;
  }

  .active {
    color: $aColor;
  }
}

.content {
  margin-left: 30px;
  width: calc(100% - 80px * 2 - 30px);
  height: 500px;
  .view{
    opacity: 0;
    transition: all .5s linear;
    animation: downIn .3s ease-in forwards;
    //animation: upMove .3s ease-in forwards;
  }
  table{
    border-spacing: 3px;
    thead{
      background: #9bdec9;
      th{
        border-radius: 10px;
        width: 200px;
        height: 40px;
      }
    }
    tbody{
      text-align: center;
      td{
        height: 30px;
        background: #b4e7f5;
        border-radius: 5px;
      }
    }
  }
}
</style>