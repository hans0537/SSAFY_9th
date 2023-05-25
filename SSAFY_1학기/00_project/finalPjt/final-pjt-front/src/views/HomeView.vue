<template>
  <div class="home container">
    <div id="carouselExampleAutoplaying" class="carousel slide mt-3" data-bs-ride="carousel" data-bs-interval="3000">
      <div class="carousel-inner">
        <div class="carousel-item active" style="overflow: hidden;">
          <img src="../assets/homeimg2.png" class="d-block w-100" style="height:400px;" alt="...">
        </div>
        <div class="carousel-item" style="overflow: hidden;">
          <img src="../assets/homeimg1.gif" class="d-block w-100" style="height:400px;" alt="...">
        </div>
        <div class="carousel-item" style="overflow: hidden;">
          <img src="../assets/homeimg3.png" class="d-block w-100" style="height:400px;" alt="...">
        </div>
        <div class="carousel-item" style="overflow: hidden;">
          <img src="../assets/homeimg4.gif" class="d-block w-100" style="height:400px;" alt="...">
        </div>
        <div class="carousel-item" style="overflow: hidden;">
          <img src="../assets/homeimg5.png" class="d-block w-100" style="height:400px;" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
      </button>
    </div>

    <div>
      <template v-if="likeMovies && worldcupMovies">
        <recommendListVue />
      </template>
      <template v-else>
        <NorecommendList />
      </template>
    </div>
    <LatestList/>

    <UpComingList/>

    <popularList />


  </div>

</template>

<script>
import LatestList from '@/components/HomeMovieComponents/LatestList'
import UpComingList from '@/components/HomeMovieComponents/UpComingList'
import popularList from '@/components/HomeMovieComponents/popularList'
import recommendListVue from '../components/HomeMovieComponents/recommendList.vue'
import NorecommendList from '@/components/HomeMovieComponents/NorecommendList.vue'

export default {
  name: 'HomeView',
  components: {
    LatestList,
    UpComingList,
    popularList,
    recommendListVue,
    NorecommendList
  },
  data() {
    return {
      // user: null,
    }
  },
  computed: {
    likeMovies() {
      return this.$store.state.user?.like_movies?.length > 0;
    },
    worldcupMovies() {
      return this.$store.state.user?.worldcup_movies?.length > 0;
    },
  },
  methods: {
  }
}
</script>


<style scoped>

</style>