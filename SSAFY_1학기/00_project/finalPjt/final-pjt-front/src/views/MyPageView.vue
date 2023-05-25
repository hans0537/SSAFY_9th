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
                    
                    <img v-if="user?.image_base64" :src="getImageSrc(user?.image_base64)"
                      alt="프로필 이미지" class="img-fluid img-thumbnail mt-4 mb-2 py-3" style="max-width: 100%; max-height: 100%">
                  
                    <img v-else src="../assets/baseProfile.png"
                      alt="프로필 이미지" class="img-fluid img-thumbnail mt-4 mb-2 py-3" style="max-width: 100%; max-height: 100%">
                  </div>
                
                  <!-- Edit Profile Modal -->
                  <div class="modal" tabindex="-1" role="dialog" id="editProfileModal">
                    <div class="modal-dialog" role="document">
                      <div class="modal-content">
                        <div class="modal-header">
                          <h5 class="modal-title" style="color: black;">프로필 이미지 변경</h5>
                          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>

                        <div class="modal-body">
                          <form>
                            <div class="mb-3">
                              <label for="profileImg" class="form-label">이미지 업로드</label>
                              <input type="file" class="form-control border" id="profileImg" :v-model="uploadImg" @change="handleFileChange"/>
                              <div>
                                <img class="mt-3" style="width: 100%" v-if="uploadImg" :src="uploadImgUrl" alt="Uploaded Image">
                              </div>
                            </div>
                          </form>
                        </div>

                        <div class="modal-footer">
                          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="closeEditProfileModal">취소</button>
                          <button type="button" class="btn btn-primary" @click="profileUpload">저장</button>
                        </div>
                      </div>
                    </div>
                  </div>

                </div>
                <div class="ms-3" style="margin-top: 130px;">
                  <h4 class="text-start">{{user?.username}}</h4>
                  <p>{{user?.email}}</p>
                </div>
              </div>

              <div class="p-4 text-black d-flex justify-content-between" style="background-color: #f8f9fa;">
                <button type="button" class="btn btn-outline-dark" data-mdb-ripple-color="dark"
                  @click="openModal"
                  style="width: 150px;">
                  Edit profile
                </button>

                <div class="d-flex justify-content-end text-center py-1">
                  <div>
                    <p class="mb-1 h5">{{user?.like_movies?.length + user?.worldcup_movies?.length}}</p>
                    <p class="small text-muted mb-0">My Movies</p>
                  </div>
                  <div class="px-3" @click="goToFriendList" style="cursor: pointer;">
                    <p class="mb-1 h5">{{user?.followers_cnt}}</p>
                    <p class="small text-muted mb-0">Followers</p>
                  </div>
                  <div @click="goToFriendList" style="cursor: pointer;">
                    <p class="mb-1 h5">{{user?.followings_cnt}}</p>
                    <p class="small text-muted mb-0">Following</p>
                  </div>
                </div>
              </div>
              
              <div class="card-body p-4 text-black">
                <div class="mb-5">
                  <p class="lead fw-normal mb-1">활동 내용</p>
                  <div class="p-4 text-start" style="background-color: #f8f9fa;">
                    <p class="font-italic mb-1"> - 등록한 게시글: {{user?.articles?.length }}개</p>
                    <p class="font-italic mb-1"> - 나의 영화: {{user?.like_movies.length + user?.worldcup_movies?.length}} 개</p>
                    <p class="font-italic mb-0"> - 초성 게임 등수: {{cho_rank}} 등</p>
                    <p class="font-italic mb-0"> - 줄거리 게임 등수: {{overview_rank}} 등</p>
                  </div>
                </div>



                <div class="d-flex justify-content-between align-items-center my-4">
                  <p class="lead fw-bold mb-0">{{user?.username}}님 추천 영화</p>
                  <div class="text-muted" @click="showAll('recommend')" style="cursor: pointer;"><p class="mb-0 text-decoration-underline">Show all</p></div> 
                </div>
                <div v-if="displayrecommend?.length === 0">
                  <h3>활동 내용이 없네여잉~</h3> 
                </div>  
                <div v-else>
                  <div class="row g-2">
                    <div class="col-3" v-for="(movie, index) in displayrecommend" :key="index">
                      <img :src="getImgSrc(movie.poster_path)" alt="image 1" class="w-100 rounded-3" @click="openDetail(movie)" style="cursor: pointer; height:200px;">
                    </div>
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
                    <div class="col-3" v-for="(movie, index) in displayWorld" :key="index">
                      <img :src="getImgSrc(movie.poster_path)" alt="image 1" class="w-100 rounded-3" @click="openDetail(movie)" style="cursor: pointer; height:200px;">
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
                    <div class="col-3" v-for="(movie, index) in displayLikes" :key="index">
                      <img :src="getImgSrc(movie.poster_path)" alt="image 1" class="w-100 rounded-3" @click="openDetail(movie)" style="cursor: pointer; height:200px;">
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
import bootstrap from 'bootstrap/dist/js/bootstrap.js';
import _ from 'lodash'
export default {
  name: 'MyPageView',
  data() {
    return {
      API_URL: this.$store.state.API_URL,

      uploadImg: null,
      uploadImgUrl: null,
      editProfileModal: null, 

      displayLikes: null,
      displayWorld: null,
      displayrecommend: null,
      like_movies: null,
      worldcup_movies: null,
      recommend_movies: null,

      cho_rank: null,
      overview_rank: null,

    }
  },
  computed: {
    user() {
      return this.$store.state.user
    }
  },
  methods: {
    openModal() {
      // Open the edit profile modal
      this.editProfileModal = new bootstrap.Modal(document.getElementById('editProfileModal'));
      this.editProfileModal.show();
    },

    handleFileChange(event) {
      const file = event.target.files[0];
      this.uploadImg = file;

      // FileReader 객체를 사용하여 이미지 파일을 읽고 데이터 URL로 변환
      const reader = new FileReader();
      reader.onload = (e) => {
        this.uploadImgUrl = e.target.result;
      };
      reader.readAsDataURL(file);
    },    
    closeEditProfileModal() {
      if (this.editProfileModal) {
        this.editProfileModal.hide();
      }
    },
    profileUpload() {
      axios({
        method: 'put',
        url: `${this.API_URL}/accounts/update/`,
        data: { username: this.user.username, followings: this.user.followings, profile: this.uploadImg },
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`,
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(() => {
        this.editProfileModal.hide();

        this.$store.dispatch('getuser')
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getImageSrc(base64String) {
      return `data:image/png;base64, ${base64String}`; // Base64 데이터를 이미지 src 형식으로 변환
    },

    goToFriendList(){
      this.$router.push({name : 'friendslist', params:{id: this.user.id}})
    },

    openDetail(movie) {
      this.$store.commit('setSelectedMovie', movie);

      this.$router.push({ name: 'moviedetail' });
    },

    showAll(type) {
      this.$router.push({name: 'showallmovie', params: {type: type, id:'me'}})
    },

    getMyRank(game) {
      axios({
        method: 'get',
        url: `${this.API_URL}/accounts/${game}/getmyrank/`,
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`,
        }
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
      let m = this.user.like_movies
      if (m.length <= 4) {
        this.displayLikes = m
      }else {
        this.displayLikes = m.slice(0, 4)
      }
      this.like_movies = m
    },

    getrecommendMovies() {
      let m = null
      if (this.user?.like_movies.length===0 || this.user?.worldcup_movies.length === 0) {
        m = null
      } else {
        m = this.$store.state.recommendmovie
      }
      if (m) {
        let a1 = [0,1,2,3,4]
        let b1 = _.sampleSize(a1, 1)[0] // 배열에서 추출된 첫 번째 요소를 가져옴
        this.displayrecommend = m[b1]
        this.recommend_movies = m[b1]
      } else {
        this.displayrecommend = []
        this.recommend_movies = []
      }
    },

    getWorldCupMovies() {
      let m = this.user.worldcup_movies

      if (m.length <= 4) {
        this.displayWorld = m
      }else {
        this.displayWorld = m.slice(0, 4)
      }
      this.worldcup_movies = m
    },

    getImgSrc(src) {
      return "https://image.tmdb.org/t/p/w500" + src
    }
  },
  created() {
    this.$store.dispatch('getuser')
    this.getMyRank('cho_points')
    this.getMyRank('overview_points')
    this.getLikeMovies()
    this.getWorldCupMovies()
    this.getrecommendMovies()
  }
}
</script>

<style>
</style>