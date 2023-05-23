<template>

  <li class="d-flex justify-content-between">
    <div class="fw-bold">{{index + 2}} 등</div>
    <div class="text-start">
      <img v-if="user?.image_base64" :src="getImageSrc(user?.image_base64)" alt="user" class="profile-photo">
      <img v-else src="../../assets/baseProfile.png" alt="user" class="profile-photo">
      {{quiztype == 'cho' ? user?.cho_points : user?.overview_points}} 점 | {{user?.username}}
    </div>
  </li>

</template>

<script>
export default {
  name: "RankUserListView",
  props: {
    user: Object,
    index: Number,
    quiztype: String,
  },
  methods: {
    getImageSrc(base64String) {
      return `data:image/png;base64, ${base64String}`; // Base64 데이터를 이미지 src 형식으로 변환
    },
  }
}
</script>

<style>
.profile-photo{
  height: 30px;
  width: 30px;
  border-radius: 50%;
}

ul.nav-news-feed{
  padding-left: 20px;
  padding-right: 20px;
  margin: 0 0 40px 0;
  background:#fff;
}

ul.nav-news-feed li{
  list-style: none;
  display: block;
  padding: 15px 0;
}

ul.nav-news-feed li div{
  position: relative;
  margin-left: 10px;
  }

ul.nav-news-feed li div::after{
  content: "";
  width: 100%;
  height: 1px;
  border-top: 1px solid #f1f2f2;
  position: absolute;
  bottom: -15px;
  left: 0;
}

ul.nav-news-feed li a{color: #6d6e71;}

ul.nav-news-feed li i{
  font-size: 18px;
  margin-right: 15px;
  float: left;
}

ul.nav-news-feed i.icon1{color: #8dc63f;}

ul.nav-news-feed i.icon2{color: #662d91;}

ul.nav-news-feed i.icon3{color: #ee2a7b;}

ul.nav-news-fee i.icon4{color: #f7941e;}

ul.nav-news-fee i.con5{color: #1c75bc;}

ul.nav-news-feed i.icon6{color: #9e1f63;}
</style>