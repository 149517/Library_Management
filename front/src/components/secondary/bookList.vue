<script>
import axios from "axios";
import {mapState} from "vuex";

export default {
  data() {
    return {
      books: [
        {
          fields: {
            bookname: "",
            id: 0,
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
      pagination_info: {
        total_pages: 0,
        current_page: 0,
        has_next: true,
        has_previous: false
      },
      page: 1,
    }
  },
  methods: {
    getBooks() {
      let url = this.baseUrl + `/books/all/?page=${this.page}`
      axios.get(url)
          .then((res) => {
            // console.log(res.data)
            this.books = res.data.data
            this.pagination_info = res.data.pagination_info
          })
          .catch((err) => {
            console.log("数据请求失败" + err)
          })
    },
    fixPage(type) {
      console.log(type)
      console.log(this.page)
      if (type === 'up') {
        if (this.page === 1) {
          return false
        } else {
          this.page = this.page - 1
        }
      } else if (type === 'down') {

        if (this.page === this.pagination_info.total_pages) {

          if (this.page === 3) {
            return false
          } else {
            this.page = this.page + 1
          }
        }
      } else {
        this.page = type
      }

    },
    open(item){
      // console.log(item)
      let isbn = item.fields.isbn
      this.$router.push(`/details/?isbn=${isbn}`)
    }
  },
  watch: {
    page(newValue) {
      this.getBooks()
    }
  },
  computed: {
    ...mapState(['baseUrl'])
  },
  mounted() {
    this.getBooks()
  }

}
</script>

<template>
  <div class="container">
    <div class="bg">
      <div class="box">
        <div class="line" v-for="item in books" key="item.id" @click="open(item)">
          <img :src="item.fields.pic" :alt="item.fields.bookname">
          <div class="text">
            <div class="name">{{ item.fields.bookname }}</div>
            <p>作者: <span>{{ item.fields.author }}</span></p>
            <p>出版社：<span>{{ item.fields.publisher }}</span></p>
            <p>分类: <span>{{ item.fields.type }}</span></p>
            <p>定价:<span>{{ item.fields.price }}</span></p>
          </div>

        </div>
      </div>
      <div class="paging">
        <button :disabled="!pagination_info.has_previous" @click="fixPage('up')">上一页</button>
        <button class="li" :class="{'li_active': pagination_info.current_page === (index+1)}"
                v-for="(item,index) in pagination_info.total_pages"
                @click="fixPage(index+1)">{{ index + 1 }}
        </button>
        <button @click="fixPage('down')" :disabled="!pagination_info.has_next">下一页</button>
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
}

.box {
  padding: 60px 100px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-column-gap: 10px;

  .line {
    display: flex;
    margin-bottom: 40px;
    animation: leftIn .5s linear forwards;
    //overflow: hidden;
    //box-sizing: border-box;
    box-shadow: 1px 1px 12px transparent;

    overflow: hidden;
    box-sizing: border-box;

    transition: all .3s ease;

    img {
      width: 120px;
    }

    .text {
      margin-left: 30px;
      margin-top: 20px;

      .name {
        padding: 5px;
        font: {
          weight: bold;
          size: 20px;
        }
      }

      p {
        padding: 5px 0;
      }

      span {
        padding-left: 10px;
        font-weight: bold;
      }
    }
  }

  .line:hover {
    box-shadow: 1px 1px 12px $aColor;

    transform: scale(1.1);


    border-radius: 10px;
    padding: 5px;
  }
}

.paging {
  width: 400px;
  margin: auto;

  button {
    width: 60px;
    height: 40px;
    outline: none;
    margin: 10px;
    border: 1px solid black;
    background: white;
    border-radius: 8px;
  }

  .li {
    width: 40px;
  }

  .li_active {
    font-weight: bold;
    //background: gainsboro;
    border: 3px solid #9bdec9;
  }
}
</style>