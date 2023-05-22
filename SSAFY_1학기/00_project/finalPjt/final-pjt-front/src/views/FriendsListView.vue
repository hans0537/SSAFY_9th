<template>
  <div class="container py-5">
    <div class="row mb-4">
      <div class="col-lg-5">
        <h5 class="text-start display-6 font-weight-light">Followers</h5>
      </div>
    </div>
    <div class="row text-center">
      <FriendsListItemView v-for="(user, index) in followersList" :key="index"
        :user="user"
        @get-friend="getFriends"/>
    </div>
    <hr>
    
    <div class="row mb-4">
      <div class="col-lg-5">
        <h5 class="text-start display-6 font-weight-light">Followings</h5>
      </div>
    </div>
    <div class="row text-center">
      <FriendsListItemView v-for="(user, index) in followingsList" :key="index"
        :user="user"
        @get-friend="getFriends"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

import FriendsListItemView from './FriendsListItemView.vue'

export default {
  name: 'FriendsListView',
  components: {
    FriendsListItemView
  },
  data() {
    return {
      userId: this.$route.params.id,
      followersList: null,
      followingsList: null,

    }
  },
  methods: {
    getFriends() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/${this.userId}/friends/`,
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`,
        }
      })
      .then((res) => {
        console.log(res)
        this.followersList = res.data.followers
        this.followingsList = res.data.followings
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created() {
    this.getFriends()
  },
}
</script>

<style scoped>
body{
    background:#eee;
    margin-top:20px;
}
.img-thumbnail {
    padding: .25rem;
    background-color: #fff;
    border: 1px solid #dee2e6;
    border-radius: .25rem;
    max-width: 100%;
    height: auto;
}

.social-link {
    width: 30px;
    height: 30px;
    border: 1px solid #ddd;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #666;
    border-radius: 50%;
    transition: all 0.3s;
    font-size: 0.9rem;
}
</style>