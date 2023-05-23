<template>
    <div class="container">
      <br>
      <br>
      <div style="display: flex;">
        <img :src="imgSrc" class="w-30 img-height" alt="img25">
        <div style="text-align: start; margin: 20px;">
          <h2>{{ movie2?.title }}</h2>
          <div style="display: flex; align-items: baseline;">
            <h5 style="margin-right: 10px;">{{ movie2?.original_title }}</h5>
          </div>
          <h5 style="margin-top: 10px;">
            <p style="color: darkgray; display: inline; margin-right: 10px;">개봉:</p> {{ movie2?.release_date }}
          </h5>
          <h5 style="margin-top: 10px;">
            <p style="color: darkgray; display: inline; margin-right: 10px;">평점:</p> {{ movie2?.vote_average.toFixed(1) }}
          </h5>
          <h5 style="margin-top: 10px;">
            <p style="color: darkgray; display: inline; margin-right: 10px;">장르:</p> {{ genreList  }}
          </h5>
          <h5 style="margin-top: 10px;">
            <p style="color: darkgray; display: inline; margin-right: 10px;">상영시간:</p> {{ movie2?.runtime  }}분
          </h5>
        </div>
      </div>
      <br>
      <hr>
      <br>
      <div class="row">
        <div class="col-md-5">
          <div style="text-align:start">
            <h4 class="fw-bold fs-4">줄거리</h4>
            <p class="fs-5">{{ movie2?.overview }}</p>
          </div>
        </div>
        <div class="col-md-2">
        </div>
        <div class="col-md-5" style="text-align:start">
          <h4 class="fw-bold fs-4">키워드</h4>
          <div v-for="keyword in keywordsList" :key="keyword.id">
          <li class="fs-5"> {{ keyword }}</li>
          </div>
        </div>
      </div>
      <br>
      <br>
      <br>
      <div style="text-align:start">
        <h4 class="fw-bold fs-4">출연진</h4>
        <br>
        <div class="container">
          <div class="row">
            <ActorViewVue v-for="actor in ActorsData" :key="actor.id" :actor="actor" class="col-2 mb-5"/>
          </div>
        </div>
      </div>
      <!-- 영상가져오기 -->
      <div class="mt-3" v-if="isSelectedVideo" style="max-height: calc(100vh - 500px);">
        <div class="ratio ratio-16*9">
          <iframe :src="videoSrc" frameborder="0" style="height:500px"></iframe>
        </div>
        <div>
          <h4>
            {{videoTitle}}
          </h4>
        </div>
      </div>
      <div style="margin-top:35rem">
        <div class="container mt-5 pt-5">
          <div class="row d-flex justify-content-center">
              <div>
        <div class="card">
          <div class="card-body">
              <div class="small d-flex justify-content-start fw-bold">
                <div class="d-flex align-items-center me-3" @click="like" style="cursor: pointer;">
                  <i class="far fa-thumbs-up me-2" :class="{ 'fa-solid' : likeCheck }" style="color: blue;"></i>
                  <p class="mb-0">Like</p>
                  <span class="ms-1 fs-6">{{movie?.like_users.length}}</span>
                </div>
                <div class="d-flex align-items-center me-3" @click="commentToggle" style="cursor: pointer;">
                  <i class="far fa-comment-dots me-2" style="color: blue;"></i>
                  <p class="mb-0">Review</p>
                  <span class="ms-1 fs-6">{{movie?.review_count}}</span>
                </div>
            </div>
            <div v-if="commentShow" class="card-footer py-3 border-0" style="background-color: #f8f9fa;">
              <div class="d-flex flex-start w-100">
              <img v-if="checkUser.image_base64" class="rounded-circle shadow-1-strong me-3"
                  :src="getImageSrc(checkUser.image_base64)" alt="avatar" width="40"
                  height="40" />

              <img v-else class="rounded-circle shadow-1-strong me-3"
                src="../../assets/baseProfile.png" alt="avatar" width="40"
                height="40" />
                <div class="form-outline w-100">
                  <b-form-textarea
                    id="comment"
                    v-model="comment"
                    class="form-control" rows="4"
                    max-rows="6"
                    style="background: #fff;" :class="{'active' : comment}"
                    @keyup.enter="createComment"
                  ></b-form-textarea>
                  <label class="form-label" for="comment">Review</label>
                </div>
              </div>
            </div>
            <div class="float-end mt-2 pt-1">
              <button type="button" class="me-2 btn btn-primary btn-sm" @click="createComment">리뷰 등록</button>
              <button type="button" class="btn btn-outline-primary btn-sm" @click="commentCancel">취소</button>
            </div>
          </div>
        </div>
        <div>
          <div class="row d-flex justify-content-center">
            <div>
              <div class="card">
                <div class="card-body p-4">
                  <h4 class="fw-bold" style="text-align:start;">리뷰</h4>
                  <div class="row">
                    <div class="col">
                      <MovieCommentViewVue 
                      v-for="comment in commentsList" :key="comment.id" 
                      :comment="comment" :movieId="movie.id " 
                      :checkUser="checkUser"
                      @get-comments="getComments"/>
                    </div>
                  </div>
                </div>
              </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import axios from "axios"
import _ from "lodash"
import MovieCommentViewVue from './MovieCommentView.vue';
import ActorViewVue from './ActorView.vue';
const URL = "https://www.googleapis.com/youtube/v3/search"
const API_KEY = 'AIzaSyB4_Ve145IcMWtdgu865J-xRWXHBRdwau0'

export default {
  name: 'MovieDetail',
  data() {
    return {
      id: parseInt(this.$route.params.id),
      videos:[],
      selectedVideo:{},
      commentShow: false,
      checkUser: this.$store.state.user,
      likeCheck: false,
      comment: '',
      commentsList: '',
      movie:null,
      movie2:null,
      movie3:null,
      ActorsData: [],
      keywords:null,
    }
  },
  components: {
    MovieCommentViewVue,
    ActorViewVue
  },
  methods: {
    getMovie() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/`,
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then((res) => {
        this.movie = res.data
        // 가져온 게시글 좋아요 목록에 회원이 있다면
        this.likeCheck = res.data.like_users.some(user => user.username === this.checkUser.username)
      })
      .catch((err) => console.log(err))
    },
    getMovie2() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movie.id}?language=ko-kr`,
        headers: {
          Authorization: "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjU2OWZjNjEwNTVkYzZhNjA3M2JiOTNlYjgxYmNiMSIsInN1YiI6IjY0MWQ0NTBlMzQ0YThlMDA5YjBiMDE2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bHKaUaJcO2JnSsD5myVc7n4CcFdrW6YE_879_00jYhw"
        }
      })
      .then((res) => {
        this.movie2 = res.data
      })
      .catch((err) => console.log(err))
    },
    commentToggle() {
      this.commentShow = !this.commentShow
    },
    getMovie3() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movie.id}/credits?language=ko-kr`,
        headers: {
          Authorization: "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjU2OWZjNjEwNTVkYzZhNjA3M2JiOTNlYjgxYmNiMSIsInN1YiI6IjY0MWQ0NTBlMzQ0YThlMDA5YjBiMDE2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bHKaUaJcO2JnSsD5myVc7n4CcFdrW6YE_879_00jYhw"
        }
      })
      .then((res) => {
        this.movie3 = res.data
        this.ActorsData = _.take(this.movie3.cast, 6)
      })
      .catch((err) => console.log(err))
    },
    getKeywards() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movie.id}/keywords`,
        headers: {
          Authorization: "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjU2OWZjNjEwNTVkYzZhNjA3M2JiOTNlYjgxYmNiMSIsInN1YiI6IjY0MWQ0NTBlMzQ0YThlMDA5YjBiMDE2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bHKaUaJcO2JnSsD5myVc7n4CcFdrW6YE_879_00jYhw"
        }
      })
      .then((res) => {
        this.keywords = res.data.keywords
      })
      .catch((err) => console.log(err))
    },
    getComments() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/review/`,
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then((res) => {
        const clst = []
        for (let i=0; i<res.data.length; i++) {
          if (res.data[i].movie.title===this.movie.title) {
            clst.push(res.data[i])
          }
        }
        this.commentsList = clst
      })
      .catch((err) => console.log(err))
    },
    createComment() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/review/`,
        data: {
          content: this.comment
        },
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then(() => {
        this.comment = ''
        this.commentShow = false
        this.getComments()
        this.getMovie()
      })
      .catch((err) => console.log(err))
    },

    commentCancel() {
      this.comment = ''
      this.commentShow = false
    },
    like() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/like/`,
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then(() => {
        this.likeCheck = !this.likeCheck
        this.getMovie()
      })
      .catch((err) => {
        console.log(err)
        alert('로그인 후에 이용해주세요')
      })
    },
    getImageSrc(base64String) {
      return `data:image/png;base64, ${base64String}`; // Base64 데이터를 이미지 src 형식으로 변환
    },
  },
  computed:{
    videoSrc() {
      return `http://www.youtube.com/embed/${this.selectedVideo.id.videoId}`
    },
    videoTitle() {
      return  _.unescape(this.selectedVideo.snippet.title)
    },
    isSelectedVideo() {
      if (Object.keys(this.selectedVideo).length) {
        return true
      } else {
        return false
      }
    },
    imgSrc() {
      return "https://image.tmdb.org/t/p/w500" + this.movie.poster_path
    },
    genreList() {
      if (this.movie2 && this.movie2.genres) {
        return this.movie2.genres.map(genre => genre.name).join('/');
      }
      return '';
    },
    keywordsList() {
      if (this.keywords) {
        return this.keywords.map(keyword => keyword.name);
      }
      return '';
    },
    Actors() {
    if (this.movie3 && this.movie3.cast) {
      let res = [];
      let temp = [];
      for (let i = 1; i <= 4; i++) {
        temp.push(this.movie3.cast[i - 1]);
        if (i % 4 === 0) {
          res.push(temp);
          temp = [];
        }
      }
      return res;
    }
    return [];
  }
  },
  mounted() {
    this.getMovie()
    this.getMovie2()
    this.getMovie3()
    this.getKeywards()
    this.getComments()
  },
  created() {
    this.movie = this.$store.state.selectedmovie
    this.getComments()
     axios.get(URL, {
       params:{
         key:API_KEY,
         type:'video',
         part:'snippet',
         q: this.movie.title + '예고편'
       },
      
     }).then(res=>{
       this.videos=res.data.items
       this.selectedVideo=this.videos[0]
     })
     .catch(err => {
       console.log(err)
     })
  }
};
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  width: 1200px;
  height:900px;
  text-align: center;
}

iframe {
  width: 100%;
  height: 100%;
}
</style>
