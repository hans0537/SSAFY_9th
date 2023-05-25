<template>
  <div class="container">
    <section class="h-100 gradient-custom-2">
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col col-lg-9 col-xl-7">
            <div class="card">
              <div class="rounded-top text-white d-flex flex-row" style="background-color: #000; height:200px;">
                <div class="ms-4 d-flex flex-column" style="width: 150px;">

                  <div class="image-container d-flex align-items-center" style="width: 150px; height: 180px;">
                    
                    <img v-if="thisUser?.image_base64" :src="getImageSrc(thisUser?.image_base64)"
                      alt="프로필 이미지" class="img-fluid img-thumbnail mt-4 mb-2 py-3"
                      style="max-width: 100%; max-height: 100%;">
                  
                    <img v-else src="../assets/baseProfile.png"
                      alt="프로필 이미지" class="img-fluid img-thumbnail mt-4 mb-2 py-3"
                      style="max-width: 100%; max-height: 100%;">
                  </div>
                  
                </div>
                <div class="ms-3" style="margin-top: 130px;">
                  <h4 class="text-start">{{thisUser?.username}}</h4>
                  <p>{{thisUser?.email}}</p>
                </div>
              </div>

              <div class="p-4 text-black d-flex justify-content-between" style="background-color: #f8f9fa;">
                <div class="d-flex justify-content-start text-center py-1">
                  <div>
                    <p class="mb-1 h5">{{thisUser?.like_movies?.length + thisUser?.worldcup_movies?.length}}</p>
                    <p class="small text-muted mb-0">My Movies</p>
                  </div>
                  <div class="px-3" @click="goToFriendList" style="cursor: pointer;">
                    <p class="mb-1 h5">{{thisUser?.followers_cnt}}</p>
                    <p class="small text-muted mb-0">Followers</p>
                  </div>
                  <div @click="goToFriendList" style="cursor: pointer;">
                    <p class="mb-1 h5">{{thisUser?.followings_cnt}}</p>
                    <p class="small text-muted mb-0">Following</p>
                  </div>
                </div>
                <div>
                  <button v-if="!followCheck" type="button" class="btn btn-success" @click="follow">팔로우</button>
                  <button v-else type="button" class="btn btn-danger" @click="follow">언팔로우</button>
                </div>
              </div>
              <div class="card-body p-4 text-black">
                <div class="mb-5">
                  <p class="lead fw-normal mb-1">About</p>
                  <div class="p-4 text-start" style="background-color: #f8f9fa;">
                    <p class="font-italic mb-1"> - 등록한 게시글: {{thisUser?.articles?.length }}개</p>
                    <p class="font-italic mb-1"> - 나의 영화: {{thisUser?.like_movies.length + thisUser?.worldcup_movies?.length}} 개</p>
                    <p class="font-italic mb-0"> - 초성 게임 등수: {{cho_rank}} 등</p>
                    <p class="font-italic mb-0"> - 줄거리 게임 등수: {{overview_rank}} 등</p>
                  </div>
                </div>
                

                <div class="d-flex justify-content-between align-items-center my-4 border-top pt-4">
                  <p class="lead fw-bold mb-0">월드컵 1위 영화들</p>
                  <div class="text-muted" @click="showAll('world')" style="cursor: pointer;"><p class="mb-0 text-decoration-underline">Show all</p></div> 
                </div>

                <div v-if="displayWorld?.length === 0">
                  <h3>활동 내용이 없네여잉~</h3> 
                </div>  
                <div v-else>
                  <div class="row g-2">
                    <div class="col mb-2" v-for="(movie, index) in displayWorld" :key="index">
                      <img :src="getImgSrc(movie.poster_path)" alt="image 1" class="w-100 rounded-3" @click="openDetail(movie)" style="cursor: pointer;">
                    </div>
                  </div>
                </div>


                <div class="d-flex justify-content-between align-items-center my-4 border-top pt-4">
                  <p class="lead fw-bold mb-0">좋아요 한 영화들</p>
                  <div class="text-muted" @click="showAll('like')" style="cursor: pointer;"><p class="mb-0 text-decoration-underline">Show all</p></div> 
                </div>
                

                <div v-if="displayLikes?.length === 0">
                  <h3>활동 내용이 없네여잉~</h3> 
                </div>  
                <div v-else>
                  <div class="row g-2">
                    <div class="col mb-2" v-for="(movie, index) in displayLikes" :key="index">
                      <img :src="getImgSrc(movie.poster_path)" alt="image 1" class="w-100 rounded-3" @click="openDetail(movie)" style="cursor: pointer;">
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </section>    
  </div>
</template>

<script>
import axios from 'axios'
// import bootstrap from 'bootstrap/dist/js/bootstrap.js';

export default {
  name: 'UserProfileView',
  data() {
    return {
      API_URL: this.$store.state.API_URL,

      thisUserId: this.$route.params.id,
      thisUser: null,
      followCheck: false,
      me: this.$store.state.user.id,

      cho_rank: null,
      overview_rank: null,

      displayLikes: null,
      displayWorld: null,
    }
  },
  methods: {

    getThisUser() {
      axios({ 
        method: 'get',
        url: `${this.API_URL}/accounts/profile/${this.thisUserId}/`,
      })
      .then((res) => {
        this.thisUser = res.data
        // 이 회원이 내가 팔로우 했다면
        this.followCheck = this.thisUser.followers.some(userId => userId === this.me)
      })
      .then(() => {
        this.getLikeMovies()
        this.getWorldCupMovies()
      })
      .catch((err) => {
        console.log(err)
      })
    },

    follow() {
      axios({
        method: 'post',
        url: `${this.API_URL}/accounts/${this.thisUserId}/follow/`,
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then(() => {
        this.followCheck = !this.followCheck
        this.getThisUser()
      })
      .catch((err) => {
        console.log(err)
        alert('로그인 후에 이용해주세요')
      })
    },

    getImageSrc(base64String) {
      return `data:image/png;base64, ${base64String}`; // Base64 데이터를 이미지 src 형식으로 변환
    },

    goToFriendList(){
      this.$router.push({name : 'friendslist', params:{id: this.thisUserId}})
    },

    getRank(game) {
      axios({
        method: 'get',
        url: `${this.API_URL}/accounts/${game}/getrank/${this.thisUserId}/`,
      })
      .then((res) => {
        if (game === 'cho_points'){
          this.cho_rank = res.data.rank
        } else{
          this.overview_rank = res.data.rank
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getLikeMovies() {
      let m = this.thisUser.like_movies
      if (m.length <= 4) {
        this.displayLikes = m
      }else {
        this.displayLikes = m.slice(0, 4)
      }
      this.like_movies = m
    },

    getWorldCupMovies() {
      let m = this.thisUser.worldcup_movies

      if (m.length <= 4) {

        this.displayWorld = m
      }else {
        this.displayWorld = m.slice(0, 4)
      }
      this.worldcup_movies = m

    },

    getImgSrc(src) {
      return "https://image.tmdb.org/t/p/w500" + src
    },

    showAll(type) {
      this.$router.push({name: 'showallmovie', params: {type: type, id: this.thisUserId}})
    },

  },
  created() {
    this.getThisUser()
    this.getRank('cho_points')
    this.getRank('overview_points')
  },
}
</script>

<style>
</style>