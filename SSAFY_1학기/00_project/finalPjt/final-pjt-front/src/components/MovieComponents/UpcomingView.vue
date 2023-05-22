<template>
  <div>
    <div style="display: flex; justify-content: end;">
      <form class="w-auto py-1" style="max-width: 12rem; display:flex; align-items: center;" @submit.prevent="searchmovie">
        <input ref="searchInput" type="search" class="form-control rounded-0" placeholder="Search" aria-label="Search">
        <span class="ms-3" type="submit" id="search-addon" @click="searchmovie">
          <i class="fas fa-search"></i>
        </span>
        <span class="ms-3" @click="clearSearch">
          <i class="fas fa-times"></i>
        </span>
      </form>

    </div>
    <div class="container">
      <div v-for="(movies, index) in AverageMovie" :key="index">
        <div>
          <div class="row">
            <UpcomingItems v-for="movie in movies" :key="movie.id" :movie="movie" class="col-2 mb-5"/>
          </div>
        </div>
      </div>
    </div>
        <!-- Pagination -->
        <div class="overflow-auto" style="display: flex; justify-content: center;">
      <!-- Use text in props -->
      <b-pagination
        v-model="currentPage"
        :total-rows="filteredMovies.length"
        :per-page="perPage"
        first-text="First"
        prev-text="Prev"
        next-text="Next"
        last-text="Last"
      ></b-pagination>
    </div>
    <!-- Pagination -->  
  </div>
</template>

<script>
import UpcomingItems from './UpcomingItems.vue';
export default {
  name:'NowMovieView',
  data() {
    return {
      rows: 20,
      perPage: 20,
      currentPage: 1,
      tmp:null,
      search_movie: null,
    }
  },
  components: {
    UpcomingItems
  },
  computed: {
    AverageMovie() {
      const tmp1 = this.tmp.slice((this.currentPage - 1) * 20, this.currentPage * 20);
      let res = [];
      let temp = [];
      if (this.search_movie === null) {
        for (let i = 1; i <= tmp1.length; i++) {
          temp.push(tmp1[i - 1]);
          if (i % 4 === 0) {
            res.push(temp);
            temp = [];
          }
        }
        if (temp.length > 0) {
          res.push(temp);
        }
      } else {
        const searchKeyword = this.search_movie;
        for (let i = 1; i <= this.tmp.length; i++) {
          
          if (this.tmp[i - 1].title.includes(searchKeyword)) {
            temp.push(this.tmp[i - 1]);
          }
        }
        res.push(temp);
        temp = [];
      }
      return res;
    },
    pagedMovies() {
      const startIndex = (this.currentPage - 1) * this.perPage;
      return this.filteredMovies.slice(startIndex, startIndex + this.perPage);
    },

    filteredMovies() {
      if (this.search_movie === null) {
        return this.tmp;
      } else {
        const searchKeyword = this.search_movie.toLowerCase().trim();
        return this.tmp.filter(movie => movie.title.toLowerCase().includes(searchKeyword));
      }
    }
  },
  methods: {
    getPagelen() {
      this.tmp = this.$store.state.upcomingList.sort((a, b) => -(a.popularity - b.popularity));
      this.rows = this.$store.state.upcomingList.length;
    },
    searchmovie() {
      // 가장 가까운 form의 input 요소 찾기
      const searchInput = this.$refs.searchInput;
      
      // 검색어 가져오기
      this.search_movie = searchInput.value.trim();
    },
    clearSearch() {
      const searchInput = this.$refs.searchInput;
      searchInput.value = ''; // 검색어 입력란 비우기
      this.search_movie = null; // 검색어 초기화
    }
  },
  created() {
    this.getPagelen();
  }
}
</script>

<style>

</style>