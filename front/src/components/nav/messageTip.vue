<template>
  <el-button :plain="true" @click="open2(buttonText,borrowStatus,buyStatus)" id="btn">{{ buttonText }}</el-button>
</template>

<script lang="ts" setup>
import {ElMessage} from 'element-plus'

import {mapState} from 'vuex';

const { borrowStatus, buyStatus } = mapState(['borrowStatus', 'buyStatus']);

const props = defineProps({
  buttonText: String, // 定义一个props属性来接收按钮文字
})

const open2 = (buttonText, borrowStatus,buyStatus) => {
  if (buttonText === '借阅' && borrowStatus) {
    ElMessage({
      message: '借阅成功',
      type: 'success',
    })
  } else if (buttonText === '借阅' && !borrowStatus) {
    ElMessage({
      message: '借阅失败',
      type: 'warning',
    })
  } else if (buttonText === '购买' && buyStatus) {
    ElMessage({
      message: '购买成功',
      type: 'success',
    })
  } else {
    ElMessage({
      message: '购买失败',
      type: 'warning',
    })
  }
}
</script>
<style>
#btn {
  border: 0;
  background: none;
  font-size: 42px;
  color: white;
}
</style>