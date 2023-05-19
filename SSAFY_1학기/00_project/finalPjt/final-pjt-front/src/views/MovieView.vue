<template>
  <div>
    <br>
    <!--Main layout-->
    <main>
    <div class="container">
      <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark mt-3 mb-5 shadow p-2" style="background-color: #607D8B">
      <!-- Container wrapper -->
      <div class="container-fluid">

        <!-- Navbar brand -->
        <a class="navbar-brand" href="#">카테고리:</a>

        <!-- Toggle button -->
        <button 
          class="navbar-toggler" 
          type="button" 
          data-mdb-toggle="collapse" 
          data-mdb-target="#navbarSupportedContent2" 
          aria-controls="navbarSupportedContent2" 
          aria-expanded="false" 
          aria-label="Toggle navigation">
          <i class="fas fa-bars"></i>
        </button>

        <!-- Collapsible wrapper -->
        <div class="collapse navbar-collapse" id="navbarSupportedContent2">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0 mt-3">

            <!-- Link -->
            <p class="me-3" :class="{ 'selected': select_cate === 'all' }" @click="allmovie" @mouseover="changeCursor('pointer')">전체</p>
            <p class="me-3" :class="{ 'selected': select_cate === 'genre' }" @click="genremovie" @mouseover="changeCursor('pointer')">장르</p>
            <p class="me-3" :class="{ 'selected': select_cate === 'average' }" @click="averagemovie" @mouseover="changeCursor('pointer')">최고 평정</p>
            <p class="me-3" :class="{ 'selected': select_cate === 'now' }" @click="nowmovie" @mouseover="changeCursor('pointer')">현재 상영작</p>
            <p :class="{ 'selected': select_cate === 'upcome' }" @click="upcomingmovie" @mouseover="changeCursor('pointer')">상영 예정작</p>
          </ul>

          <!-- Search -->
          <form class="w-auto py-1" style="max-width: 12rem">
            <input type="search" class="form-control rounded-0" placeholder="Search" aria-label="Search">
          </form>
          <span class="ms-3" id="search-addon">
            <i class="fas fa-search"></i>
          </span>
        </div>
      </div>
      <!-- Container wrapper -->
    </nav>
    <!-- Navbar -->
    <AllMovieView v-if="select_cate === 'all'"/>
    <AverageMovieView v-else-if="select_cate === 'average'" />
    <GenreMovieView v-else-if="select_cate === 'genre'" />
    <UpcomingView v-else-if="select_cate === 'upcome'" />
    <NowMovieView v-else-if="select_cate === 'now'" />
    <!-- Products -->
      <section>
      <div class="text-center">
        <div class="row">
          
        </div>
      </div>
    </section>
    </div>
    </main>
    <!--Main layout-->
  </div>
</template>

<script>
import AllMovieView from '@/components/MovieComponents/AllMovieView';
import AverageMovieView from '../components/MovieComponents/AverageMovieView';
import GenreMovieView from '../components/MovieComponents/GenreMovieView';
import NowMovieView from '../components/MovieComponents/NowMovieView';
import UpcomingView from '../components/MovieComponents/UpcomingView';
export default {
  name: "MovieView",
  data() {
    return {
      select_cate: 'all',
    }
  },
  components: {
    AllMovieView,
    AverageMovieView,
    GenreMovieView,
    NowMovieView,
    UpcomingView
  },
  methods: {
    allmovie() {
      this.select_cate = 'all'
    },
    averagemovie() {
      this.select_cate = 'average';
    },
    genremovie() {
      this.select_cate = 'genre';
    },
    nowmovie() {
      this.select_cate = 'now';
    },
    upcomingmovie() {
      this.select_cate = 'upcome';
    },
    changeCursor(cursorType) {
      document.body.style.cursor = cursorType;
    },
  }
}
</script>

<style>
.selected {
  color: black;
}
</style>