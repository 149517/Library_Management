<script>
export default {

  data() {
    return {

    }
  },
  methods: {

  },


}
</script>

<template>
  <div class="container">
    <div class="banner">
      <div class="tit">
        Reading makes us meet in our souls
      </div>
      <div class="des">
        这里是曦林图书，在这里你可以通过数字图书在线阅读书籍，也可以查询和自主借阅，也能在线上购买书籍。
      </div>
      <div class="image">
        <img class='left' src="../assets/images/banner-left.png" alt="">
        <img class='middle' src="../assets/images/banner3.png" alt="">
        <img class='right' src="../assets/images/banner-right.png" alt="">
      </div>
    </div>

    <div class="content">

    </div>
  </div>
</template>

<style scoped lang="scss">
$aColor: #1A535E;
$btnColor: #38B081;
$bgColor: #ECFBFB;

.banner {
  width: 100%;
  //height: calc(100vh - 80px * 2);
  overflow: hidden;
  padding: 20px 0;
  border-radius: 20px;
  background: $bgColor;
  text-align: center;

  .tit {
    padding-top: 50px;
    color: $aColor;
    animation: leftIn .5s ease-in forwards;
    font: {
      size: 50px;
      weight: bold;
    }
  }

  .des{
    opacity: 0;
    animation: downIn .5s ease-in forwards;
    animation-delay: .6s;
  }

  div {
    padding-top: 30px;
  }

  .image {
    width: 100%;
    margin-bottom: 30px;
    display: flex;
    justify-content: space-between;

    .right,
    .left{
      transition: all .4s ease;
      transform: scale(1);
    }

    .middle {
      transition: all .4s ease;
      animation: upMove .5s linear forwards;
      &:hover{
        transform: scale(1.1);
      }
    }
  }


}

</style>