<template>
  <div class="home container">
    <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel" data-bs-interval="3000">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="@/assets/background.jpeg" class="d-block w-100" style="height:300px;" alt="...">
        </div>
        <div class="carousel-item">
          <img src="@/assets/logo.png" class="d-block w-100" style="height:300px;" alt="...">
        </div>
        <div class="carousel-item">
          <img src="@/assets/background.jpeg" class="d-block w-100" style="height:300px;" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
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

export default {
  name: 'HomeView',
  components: {
    LatestList,
    UpComingList,
    popularList
  },
  data() {
    return {
      dataLoaded: false
    }
  },
  created() {
    if (!this.dataLoaded) {
    this.getLatest();
    this.getUpComing();
    this.getPopular();
    this.getall();
    this.dataLoaded = true;
  }
  },
  methods: {
    getLatest(){
      this.$store.dispatch('getLatest')
    },
    getUpComing(){
      this.$store.dispatch('getUpComing')
    },
    getPopular() {
      this.$store.dispatch('popularMovie')
    },
    getall() {
      this.$store.dispatch('getall')
    }

  }
}
</script>

<style scoped>

</style>