<template>
  <div>
    <div style="display: flex; flex-wrap: wrap; justify-content: center; margin-top:30px; margin-bottom: 30px;">
      <h1>{{ viewround }}</h1>  
      <h1 v-if="viewround !== '결승' && viewround !== '최종선택'">- {{ currentPairIndex+1 }} 라운드</h1>
    </div>
    <div class="container">
      <div v-for="(movies, index) in selectMovie" :key="index" >
        <div >
          <div class="row" style="display: flex; justify-content: center;">
            <WorldcupItemView
              v-for="movie in movies"
              :key="movie.id"
              :movie="movie"
              @selected="handleMovieSelected"
            />
          </div>
        </div>
      </div>
      <div v-if="round === 1 && viewround === '최종선택'">
        <br>
        <button class="btn btn-primary mb-5" @click="handleRestartClick" style="margin-right: 20px;">다시하기</button>
        <button class="btn btn-primary mb-5" @click="movieselect">상세보기</button>
      </div>
    </div>
  </div>
</template>

<script>  
import _ from 'lodash'
import axios from 'axios'
import WorldcupItemView from './WorldcupItemView.vue'

export default {
  name: 'WorldcupView',
  components: {
    WorldcupItemView
  },
  data() {
    return {
      API_URL: this.$store.state.API_URL,

      movie: null,
      genre: null,
      movie16: null,
      selectedMovies: [], // 선택된 영화들을 저장하는 배열 추가
      isMovieLoaded: false, // 데이터 로드 여부를 저장하는 변수 추가
      round: 16,
      viewround: '16강',
      currentPairIndex: 0, // 현재 보여지는 쌍의 인덱스 추가
      resultMovie:null
    }
  },
  methods: {
    movieselect() {
      this.$store.state.selectedmovie = this.resultMovie
      this.$router.push({name:'moviedetail'})
    },
    GetMovieAndGenre() {
      this.movie = this.$store.state.allmovie
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/genre`
      })
        .then((res) => {
          this.genre = res.data.map(item => ({ id: item.id, name: item.name }))
          this.genre = _.sampleSize(this.genre, 16)
          this.movie16 = this.genre.map(genre => {
            const moviesInGenre = this.movie.filter(movie => movie.genre_ids.includes(genre.id))
            return _.sample(moviesInGenre)
          })
          this.isMovieLoaded = true; // 데이터 로드 완료 설정
        })
        .catch((err) => {
          console.log(err)
        })
    },
    handleRestartClick() {
      // 다시하기 버튼 클릭 시 처리 로직 추가
      location.reload()
    },
    handleMovieSelected(movie) {
      this.selectedMovies.push(movie); // 선택된 영화를 배열에 추가

      if (this.selectedMovies.length === 8 && this.round === 16) {
        // 8개의 영화가 선택되었을 때
        this.movie16 = this.selectedMovies; // 다음에 보여질 영화로 설정
        this.selectedMovies = []; // 선택된 영화 배열 초기화
        this.round = 8;
        this.viewround = '8강';
        this.currentPairIndex = 0; // 새로운 쌍의 인덱스를 초기화
      } else if (this.selectedMovies.length === 4 && this.round === 8) {
        // 4개의 영화가 선택되었을 때
        this.movie16 = this.selectedMovies; // 다음에 보여질 영화로 설정
        this.selectedMovies = []; // 선택된 영화 배열 초기화
        this.round = 4;
        this.viewround = '4강';
        this.currentPairIndex = 0; // 새로운 쌍의 인덱스를 초기화
      } else if (this.selectedMovies.length === 2 && this.round === 4) {
        // 2개의 영화가 선택되었을 때
        this.movie16 = this.selectedMovies; // 다음에 보여질 영화로 설정
        this.selectedMovies = []; // 선택된 영화 배열 초기화
        this.round = 2;
        this.viewround = '결승';
        this.currentPairIndex = 0; // 새로운 쌍의 인덱스를 초기화
      } else if (this.selectedMovies.length === 1 && this.round === 2) {
        // 1개의 영화가 선택되었을 때 (결승전)
        this.movie16 = [[this.selectedMovies[0]]]; // 선택된 영화를 배열로 설정
        this.resultMovie = this.selectedMovies[0]
        this.like()
        this.selectedMovies = []; // 선택된 영화 배열 초기화
        this.round = 1; 
        this.viewround = '최종선택';
        this.currentPairIndex = 0; // 새로운 쌍의 인덱스를 초기화
      } else if(this.round === 1) {
        this.movieselect()
      } else {
        // 다음 쌍의 영화를 보여줌
        this.currentPairIndex += 1;
      }
    },
    like() {
      axios({
        method: 'post',
        url: `${this.API_URL}/movies/${this.resultMovie.id}/worldcuplike/`,
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then(() => {
        axios({
          method: 'get',
          url: `${this.API_URL}/accounts/profile/${this.$store.state.user.id}/`
        })
        .then((res) => {
          this.$store.state.user = res.data
        })
        .catch((err1) => {
          console.log(err1)
        })
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  computed: {
    selectMovie() {
      if (!this.isMovieLoaded) {
        return [];
      }

      let res = [];
      let movies = this.movie16;
      if (movies.length===1) {
        return movies
      } else {
        if (movies.length > this.currentPairIndex * 2) {
          res.push([movies[this.currentPairIndex * 2], movies[this.currentPairIndex * 2 + 1]]);
        }
        return res;

      }

    }
  },
  created() {
    this.GetMovieAndGenre()
  },
}
</script>

<style>
/* 스타일은 여기에 추가 */
</style>
