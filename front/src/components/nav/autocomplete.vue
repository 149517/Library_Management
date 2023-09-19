<template>
  <el-autocomplete
      v-model="state"
      :fetch-suggestions="querySearch"
      popper-class="my-autocomplete"
      placeholder="Please input"
      @select="handleSelect"
      @link-selected="handleLinkSelected"
  ><!-- 添加监听事件 -->
    <template #suffix>
      <el-icon class="el-input__icon" @click="handleIconClick">
        <edit/>
      </el-icon>
    </template>
    <template #default="{ item }">
      <div class="value">{{ item.value }}</div>
      <span class="link">{{ item.link }}</span>
    </template>
  </el-autocomplete>
</template>

<script lang="ts" setup>
import {computed, onMounted, ref} from 'vue'
import {Edit} from '@element-plus/icons-vue'
import {mapState} from "vuex";
import axios from "axios";


interface LinkItem {
  value: string
  link: string
}

const state = ref('')
const links = ref<LinkItem[]>([])

const querySearch = (queryString: string, cb) => {
  const results = queryString
      ? links.value.filter(createFilter(queryString))
      : links.value
  // call callback function to return suggestion objects
  cb(results)
}
const createFilter = (queryString) => {
  return (restaurant) => {
    return (
        restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
    )
  }
}

const getList = () => {

}
const loadAll = () => {
  return axios.get('http://localhost:8000/books/getList/')
      .then((res) => {
        console.log(res);
        console.log(typeof res.data);
        if (Array.isArray(res.data)) {
          // 响应数据是数组
          console.log('Response data is an array');
          return res.data; // 返回数据数组
        } else {
          // 尝试将响应数据转换为数组
          const dataArray = Array.from(res.data);
          console.log('Response data is not an array, but converted to an array:', dataArray);
          return dataArray; // 返回转换后的数组
        }
      })
      .catch((err) => {
        console.log(err);
        return null;
      });
}

// const loadAll = () => {
  // return [
  //   {value: '红与黑', link: 9787544629362},
  //   {value: '长安的荔枝', link: 9787572608582},
  //   {value: '三体', link: 9787229166922},
  //   {value: '明朝那些事（全集）', link: 9787801656179},
  //   {value: '活着', link: 9787530221532},
  //   {value: '平凡的世界（全三部）', link: 9787530221396},
  //   {value: '追风筝的人', link: 9787208061644},
  //   {value: '杀死一只知更鸟', link: 9787544766500},
  //   {value: '南京大屠杀', link: 9787508653389},
  //   {value: '白夜行', link: 9787544258609},
  //   {value: '白鹿原', link: 9787020090297},
  //   {value: '我们仨', link: 9787108018809},
  //   {value: '小王子', link: 9787020042494},
  //   {value: '一个叫欧维的男人决定去死', link: 9787541142185},
  //   {value: '置身事内：中国政府与经济发展', link: 9787208171336},
  //   {value: '围城', link: 9787020127894},
  //   {value: '东汉至魏晋时期的瘟疫、战争与社会', link: 9787553818016},
  //   {value: '冰路狂花', link: 9787559861030},
  //   {value: '写作是一把刀', link: 9787208182721},
  //   {value: '重读鲁迅', link: 9787308235372},
  //   {value: '思想之诗', link: 9787559858184},
  //   {value: '明清白莲教社会历史调查', link: 9787100184168},
  //   {value: '为书籍的一生', link: 9787108064370},
  //   {value: '消费图像', link: 9787568938945},
  //   {value: '杂文的自觉', link: 9787108059345},
  //   {value: '风痕', link: 9787108075864},
  // ]
// }
const emit = defineEmits() // 引入 emit 函数
const handleSelect = (item: LinkItem) => {
  // console.log(item)
  // 触发自定义事件 'link-selected'，并传递选中的 Link 对象
  // this.$emit('自定义事件名称', 传递的数据)
  emit('link-selected', item)
}
const handleLinkSelected = (linkItem) => {
  // 处理选中的 Link 对象
  console.log('选中的 Link 对象:', linkItem)
}
const handleIconClick = (ev: Event) => {
  console.log(ev)
}
// 在获取数据后手动分配给 links
loadAll().then((data) => {
  links.value = data;
});


// onMounted(() => {
//   links.value = loadAll();
//   // links.value = getList()
// })
</script>

<style scoped>
input {
  width: 500px !important;
}

.my-autocomplete li {
  line-height: normal;
  padding: 7px;
}

.my-autocomplete li .name {
  text-overflow: ellipsis;
  overflow: hidden;
}

.my-autocomplete li .addr {
  font-size: 12px;
  color: #b4b4b4;
}

.my-autocomplete li .highlighted .addr {
  color: #ddd;
}
</style>
