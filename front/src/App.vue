<script>
import Nav from "./components/nav/nav.vue";

export default {
  components: {
    Nav,
  }
}
</script>

<template>
  <Nav></Nav>
  <router-view></router-view>

</template>

<style lang="scss">
.container {
  padding: 0 80px;
  //margin-top: 30px;
}


</style>
