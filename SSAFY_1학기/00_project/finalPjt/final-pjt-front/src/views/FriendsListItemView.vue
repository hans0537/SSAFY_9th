<template>
  <div class="col-xl-3 col-sm-6 mb-5">
    <div class="bg-white rounded shadow-sm py-5 px-4">
      
      <img v-if="user?.image_base64" :src="getImageSrc(user?.image_base64)" alt="" width="100" class="profile-image img-fluid rounded-circle mb-3 img-thumbnail shadow-sm">
      <img v-else src="../assets/baseProfile.png" alt="asdf" width="100" class="profile-image img-fluid rounded-circle mb-3 img-thumbnail shadow-sm">
      
      <h5 class="mb-0">{{user?.username}}</h5><span class="small text-uppercase text-muted">{{user?.email}}</span>
      
      <div class="row mx-0 mt-3 border-top border-bottom">
        <div class="col-6 text-center border-end py-3">
          <h5 class="mb-0">{{user?.followers.length}}</h5>
          <small class="text-muted">Followers</small>
        </div>
        <div class="col-6 text-center py-3">
          <h5 class="mb-0">{{user?.followings.length}}</h5>
          <small class="text-muted">Following</small>
        </div>
      </div>
      <div v-if="user?.id !== me" class="d-flex justify-content-between mt-3">
        <button type="button" class="btn btn-info px-4" @click="goToThisProfile">프로필</button>

        <button v-if="!checkFollow" type="button" class="btn btn-success px-4" @click="follow">팔로우</button>
        <button v-else type="button" class="btn btn-danger px-4" @click="follow">언팔로우</button>
      </div>
      <div v-else class="d-flex justify-content-center mt-3">
        <button type="button" class="btn btn-info" @click="goToMyProfile">내 프로필</button>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'FriendsListItemView',
  data() {
    return {
      me: this.$store.state.user.id,
    }
  },
  props: {
    user: Object,
  },
  computed: {
    checkFollow() {
      return this.user.followers.some(id => id === this.me)
    }
  },
  methods: {

    getImageSrc(base64String) {
      return `data:image/png;base64, ${base64String}`; // Base64 데이터를 이미지 src 형식으로 변환
    },

    follow() {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/${this.user.id}/follow/`,
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then((res) => {
        console.log(res.data)
        this.$emit('get-friend');
      })
      .catch((err) => {
        console.log(err)
        alert('로그인 후에 이용해주세요')
      })
    },

    goToMyProfile() {
      this.$router.push({name: 'mypage'})
    },

    goToThisProfile() {
      this.$router.push({ name: 'userprofile', params: {id: this.user.id} })
    },
  }
}
</script>

<style scoped>
.profile-image {
  width: 100px;
  height: 100px;
  object-fit: cover;
}
</style>