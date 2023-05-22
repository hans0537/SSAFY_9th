<template>
  <div class="container">
    <section class="h-100 gradient-custom-2">
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col col-lg-9 col-xl-7">
            <div class="card">
              <div class="rounded-top text-white d-flex flex-row" style="background-color: #000; height:200px;">
                <div class="ms-4 mt-5 d-flex flex-column" style="width: 150px;">

                  <div class="image-container" style="width: 150px; height: 180px;">
                    
                    <img v-if="thisUser?.image_base64" :src="getImageSrc(thisUser?.image_base64)"
                      alt="프로필 이미지" class="img-fluid img-thumbnail mt-4 mb-2 py-3"
                      style="max-width: 100%; max-height: 100%; z-index: 2;">
                  
                    <img v-else src="../assets/baseProfile.png"
                      alt="프로필 이미지" class="img-fluid img-thumbnail mt-4 mb-2 py-3"
                      style="max-width: 100%; max-height: 100%; z-index: 1;">
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
                    <p class="mb-1 h5">253</p>
                    <p class="small text-muted mb-0">Photos</p>
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
                  <div class="p-4" style="background-color: #f8f9fa;">
                    <p class="font-italic mb-1">Web Developer</p>
                    <p class="font-italic mb-1">Lives in New York</p>
                    <p class="font-italic mb-0">Photographer</p>
                  </div>
                </div>
                <div class="d-flex justify-content-between align-items-center mb-4">
                  <p class="lead fw-normal mb-0">Recent photos</p>
                  <p class="mb-0"><a href="#!" class="text-muted">Show all</a></p>
                </div>
                <div class="row g-2">
                  <div class="col mb-2">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/Lightbox/Original/img%20(112).webp"
                      alt="image 1" class="w-100 rounded-3">
                  </div>
                  <div class="col mb-2">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/Lightbox/Original/img%20(107).webp"
                      alt="image 1" class="w-100 rounded-3">
                  </div>
                </div>
                <div class="row g-2">
                  <div class="col">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/Lightbox/Original/img%20(108).webp"
                      alt="image 1" class="w-100 rounded-3">
                  </div>
                  <div class="col">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/Lightbox/Original/img%20(114).webp"
                      alt="image 1" class="w-100 rounded-3">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-1.webp"
          alt="Generic placeholder image" class="img-fluid img-thumbnail mt-4 mb-2"
          style="width: 150px; z-index: 1">
    </section>    
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
// import bootstrap from 'bootstrap/dist/js/bootstrap.js';

export default {
  name: 'UserProfileView',
  data() {
    return {
      thisUserId: this.$route.params.id,
      thisUser: null,
      followCheck: false,
      me: this.$store.state.user.id,
    }
  },
  methods: {

    getThisUser() {
      axios({ 
        method: 'get',
        url: `${API_URL}/accounts/profile/${this.thisUserId}/`,
      })
      .then((res) => {
        console.log(res)
        this.thisUser = res.data
        console.log(this.thisUser.followers)
        console.log(this.me)

        // 이 회원이 내가 팔로우 했다면
        this.followCheck = this.thisUser.followers.some(userId => userId === this.me)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    follow() {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/${this.thisUserId}/follow/`,
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then((res) => {
        console.log(res.data)
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
    }
  },
  created() {
    this.getThisUser()
  },
}
</script>

<style>
</style>