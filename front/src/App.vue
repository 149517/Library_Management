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
}
@keyframes upMove {
  0% {
    opacity: 0;
    transform: translateY(50px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
@keyframes leftIn {
  0% {
    transform: translateX(-30px);
    opacity: 0;
  }
  100% {
    transform: translateX(0);
    opacity: 1;
  }
}
@keyframes downIn {
  0% {
    transform: translateY(-30px);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}



</style>
