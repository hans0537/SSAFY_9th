<template>
  <section id="trend" class="pt-4 mt-5" >
    <div class="container">
      <div class="row trend_1" style="display:flex; justify-content: space-between;">
        <div class="hr-line"></div>
        <div class="col-md-6 col-6">
          <i class="fa fa-solid fa-stars fa-spin" style="color: #fbff00;"></i>
          <h4 class="trend_1l" style="text-align:left;"> {{ user?.username }}님의 추천<span class="col_red"> 영화</span></h4>
          <i class="fa fa-solid fa-stars fa-spin" style="color: #fbff00;"></i>
        </div>
        <div class="col-md-6 col-6 text-end">
          <h6 class="mb-0">
            <div class="btn btn-primary" @click="showAll('recommend')" style="text-decoration: none;">View all</div> 
          </h6>
        </div>
      </div>
  
      <div class="row trend_2 mt-1">
        <div id="carouselExampleCaptions4" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleCaptions4" data-bs-slide-to="0" class="active indigo" aria-label="슬라이드 1"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions4" data-bs-slide-to="1" class="indigo" aria-label="슬라이드 2" aria-current="true"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions4" data-bs-slide-to="2" class="indigo" aria-label="슬라이드 3" aria-current="true"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions4" data-bs-slide-to="3" class="indigo" aria-label="슬라이드 4" aria-current="true"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions4" data-bs-slide-to="4" class="indigo" aria-label="슬라이드 5" aria-current="true"></button>
          </div>
          
          <div class="carousel-inner"> 
            <div class="carousel-item" v-for="(movies, index) in popularMovie" :key="index" :class="index===0 ? 'active' : ''">
              <div class="trend_2i row">
                <recommendItem 
                v-for="movie in movies" :key="movie?.id" :movie="movie"/>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

</template>

<script>
import recommendItem from './recommendItem.vue'
import _ from 'lodash'
import { mapState, mapMutations } from 'vuex';
export default {
  name: 'recommendList',
  data() {
    return {
      user: null,
    }
  },
  components: {
    recommendItem,
  },
  computed: {
    ...mapState(['recommendMovies']), // Vuex 스토어의 recommendMovies를 computed 속성으로 추가

    popularMovie() {
      const movie1 = this.$store.state.allmovie;
      const genre_id = [];
      for (let j = 0; j < this.user.like_movies.length; j++) {
        let movi = movie1.filter(movie => movie.genre_ids.includes(this.user.like_movies[j].genre_ids[0]));
        for (let i = 0; i < movi[0].genre_ids.length; i++) {
          genre_id.push(movi[0].genre_ids[i]);
        }
      }
      for (let j = 0; j < this.user.worldcup_movies.length; j++) {
        let movi = movie1.filter(movie => movie.genre_ids.includes(this.user.worldcup_movies[j].genre_ids[0]));
        for (let i = 0; i < movi[0].genre_ids.length; i++) {
          genre_id.push(movi[0].genre_ids[i]);
        }
      }
      let genreCounts = {};
      for (let id of genre_id) {
        if (genreCounts[id]) {
          genreCounts[id]++;
        } else {
          genreCounts[id] = 1;
        }
      }

      let totalCount = Object.values(genreCounts).reduce((sum, count) => sum + count, 0);
      const ratio = 20 / totalCount;

      // 전체 합이 20 미만인 경우 비율에 맞게 조정
      if (totalCount < 20) {
        for (let genre in genreCounts) {
          genreCounts[genre] = Math.ceil(genreCounts[genre] * ratio);
        }
      } else if (totalCount > 20) {
        const sortedGenres = Object.keys(genreCounts).sort((a, b) => genreCounts[b] - genreCounts[a]);
        let remainingCount = 20;
        const adjustedGenreCounts = {};
        for (let genre of sortedGenres) {
          const count = Math.ceil(genreCounts[genre] * ratio);
          if (remainingCount >= count) {
            adjustedGenreCounts[genre] = count;
            remainingCount -= count;
          } else {
            adjustedGenreCounts[genre] = remainingCount;
            break;
          }
        }
        genreCounts = adjustedGenreCounts;
        totalCount = 20;
      }

      const sortedGenres = Object.keys(genreCounts).sort((a, b) => genreCounts[b] - genreCounts[a]);
      const topGenres = sortedGenres.slice(0, totalCount);
      const tmp = [];
      let genreIndex = 0;
      const addedMovieIds = []; // Track movie IDs already added to tmp
      while (tmp.length < 20) {
        if (genreIndex >= topGenres.length) {
          // 모든 장르의 영화를 탐색한 경우
          break;
        }
        const currentGenre = parseInt(topGenres[genreIndex]);
        const moviesInGenre = movie1.filter(movie => movie.genre_ids.includes(currentGenre));
        for (let i = 0; i < genreCounts[currentGenre]; i++) {
          if (tmp.length >= 20) {
            // tmp 배열의 길이가 20이 되면 while 문 종료
            break;
          }
          const movieToAdd = _.sampleSize(moviesInGenre,1);
          if (!addedMovieIds.includes(movieToAdd[0].id)) {
            tmp.push(movieToAdd);
            addedMovieIds.push(movieToAdd[0].id);
          }
        }
        genreIndex++;
      }
      let res = [];
      let temp = [];
      for (let i = 1; i <= tmp.length; i++) {
        temp.push(tmp[i-1][0]);
        if (i % 4 === 0) {
          res.push(temp);
          temp = [];
        }
      }
      return res;
    }
  },
  methods: {
    ...mapMutations(['setRecommendMovies']), // Vuex 스토어의 setRecommendMovies를 methods 속성으로 추가
    showAll(type) {
      this.$router.push({name: 'showallmovie', params: {type: type, id:'me'}})
    },
  },
  created() {
    this.user = this.$store.state.user;
    this.setRecommendMovies(this.popularMovie); // Vuex 스토어의 recommendMovies에 popularMovie 데이터 저장
  }
}
</script>

<style>
.indigo {
  background-color: rgb(126, 99, 247) !important;
}
</style>