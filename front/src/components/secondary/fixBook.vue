<script>
import {mapState} from "vuex";
import axios from "axios";
import Autocomplete from "../nav/autocomplete.vue";

export default {
  components: {
    Autocomplete,
  },
  data() {
    return {
      msg: '000',
      play: false,
      add: true,
      active: '',
      isbn: '',
      // 空书籍对象，用于清空数据
      emptyBook: {},
      book: {
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
        Listing_time: '',
      },
    }
  },
  methods: {
    getAuthority() {
      axios.post(this.baseUrl + '/user/manage/')
          .then((res) => {
            console.log(res.data.msg)
            this.msg = res.data.msg
            if (res.data.code === 200) {
              this.play = true
            } else {
              this.play = false
            }
          })
          .catch((err) => {
            console.log(err)
          })
    },
    getBook(link) {
      // console.log(link)
      let formData = new FormData()
      formData.append('way', 'isbn')
      formData.append('name', link)
      axios.post(this.baseUrl + '/books/query/', formData)
          .then((res) => {
            if (res.data.books.length === 0) {
              alert("未检索到数据")
            }
            // console.log(res.data.books[0].fields)
            this.book = res.data.books[0].fields

          })
          .catch((err) => {
            console.log("数据提交失败" + err)
          })
    },
    handleLinkSelected(linkItem) {
      // 在这里处理从子组件传递过来的数据，即选中的 Link 对象
      console.log('选中的 Link 对象:', linkItem)
      // this.link = linkItem
      this.isbn = linkItem.link
      this.getBook(linkItem.link)
    },
    toggle(type) {
      if (type === 'false') {
        this.add = false
        this.book = this.emptyBook
      } else {
        this.add = true
      }
    },
    submit() {
      if (this.add) {
        console.log("修改")
        const url = this.baseUrl + '/books/fix/'
        this.fixBook(url)
      }
      if (!this.add) {
        console.log("添加")
        const url = this.baseUrl + '/books/add/'
        this.addBook(url)
      }
    },
    fixBook(url) {
      axios.post(url, {'isbn': this.link, 'book': this.book})
          .then((res) => {
            console.log(res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
    addBook(url) {
      axios.post(url, {'book': this.book})
          .then((res) => {
            console.log(res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    }
  },
  computed: {
    ...mapState(['baseUrl'])
  },
  mounted() {
    this.getAuthority()
    this.emptyBook = this.book;
    console.log(this.emptyBook)
  }
}
</script>

<template>
  <h1 v-if="!this.play">{{ this.msg }}</h1>

  <div class="box" v-if="this.play">
    <div class="row">
      <div :class="{'active':add}" @click="toggle('true')"><p>书籍纠错</p></div>
      <div :class="{'active':!add}" @click="toggle('false')"><p>增加新书</p></div>
    </div>

    <div class="block">

      <div class="fix" v-if="add">
        书籍检索
        <Autocomplete @link-selected="handleLinkSelected"></Autocomplete>
      </div>
      <div class="add" v-else>
        <h3>添加图书</h3>
      </div>

    </div>

    <div class="form">
      <el-form :model="book" label-width="120px">
        <el-form-item label="书名：">
          <el-input v-model="book.bookname"/>
        </el-form-item>
        <el-form-item label="作者：">
          <el-input v-model="book.author"/>
        </el-form-item>
        <el-form-item label="出版社：">
          <el-input v-model="book.publisher"/>
        </el-form-item>
        <el-form-item label="语言：">
          <el-input v-model="book.lang"/>
        </el-form-item>
        <el-form-item label="ISBN：">
          <el-input v-model="book.isbn"/>
        </el-form-item>
        <el-form-item label="类型：">
          <el-input v-model="book.type"/>
        </el-form-item>
        <el-form-item label="定价：">
          <el-input v-model.number="book.price"/>
        </el-form-item>
        <el-form-item label="封面链接：">
          <el-input v-model="book.pic"/>
        </el-form-item>
        <el-form-item label="出版日期：">
          <el-input v-model="book.Listing_time" placeholder="YYYY-MM-DD"/>
        </el-form-item>


        <el-form-item label="介绍：">
          <el-input
              v-model="book.intro"
              :rows="5"
              type="textarea"
              placeholder="Please input"
          />
          <el-button type="primary" class="btn" @click.prevent="submit()">提交</el-button>
        </el-form-item>
      </el-form>
    </div>

  </div>

</template>

<style scoped lang="scss">
$aColor: #1A535E;
$btnColor: #38B081;
$bgColor: #ECFBFB;
.box {
  background: $bgColor;
  padding: 30px;
  border-radius: 10px;
}

.block {
  .fix {
    font-weight: bold;
  }
}

.row {
  display: flex;
  width: 300px;
  height: 60px;
  line-height: 60px;
  color: #919191;
  cursor: pointer;
  margin-bottom: 30px;

  div {
    text-align: center;
    padding: 5px 10px;
    margin-right: 20px;
    transition: all .5s ease;
  }
}

.active {
  border-bottom: 3px solid $aColor;
  color: $btnColor;
  font-weight: bold;
}

.form {
  margin-top: 30px;
  width: 600px;

  el-form-item {
    font-weight: bold;
  }

  .btn {
    padding: 20px 30px;
    font-size: 20px;
    margin-top: 30px;
  }
}
</style>