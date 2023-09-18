<script>
import {mapState} from "vuex";
import axios from "axios";

export default {
  data() {
    return {
      msg: ''
    }
  },
  methods: {
    getAuthority() {
      axios.post(this.baseUrl + '/user/manage/')
          .then((res) => {
            console.log(res.data)
            this.msg = res.data.msg
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
  }
}
</script>

<template>
  <h1>{{ msg }}</h1>
</template>

<style scoped lang="scss">

</style>