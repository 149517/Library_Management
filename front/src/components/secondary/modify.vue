<script>
import fixBook from "./fixBook.vue";
import {mapState} from "vuex";

export default {
  components:{
    fixBook
  },
  computed: {
    ...mapState(['baseUrl'])
  },
}
</script>

<template>
<div class="container">
  <fix-book></fix-book>
</div>
</template>

<style scoped lang="scss">

</style>