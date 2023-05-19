<template>
<section id="trend" class="pt-4 pb-5 mt-5" >
  <div class="container">
    <div class="row trend_1" style="display:flex; justify-content: space-between;">
      <div class="col-md-6 col-6">
        <h4 class="trend_1l" style="text-align:left;">Latest <span class="col_red">Movies</span></h4>
      </div>
      <div class="col-md-6 col-6 text-end">
        <h6 class="mb-0"><a class="button" href="#" style="text-decoration: none;"> View All</a></h6>
      </div>
    </div>

    <div class="row trend_2 mt-4">
      <div id="carouselExampleCaptions1" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleCaptions1" data-bs-slide-to="0" class="active" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions1" data-bs-slide-to="1" aria-label="Slide 2" aria-current="true"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions1" data-bs-slide-to="2" aria-label="Slide 3" aria-current="true"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions1" data-bs-slide-to="3" aria-label="Slide 4" aria-current="true"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions1" data-bs-slide-to="4" aria-label="Slide 5" class="" aria-current="true"></button>
        </div>
        
        <div class="carousel-inner"> 
          <div class="carousel-item" v-for="(movies, index) in latestList" :key="index" :class="index===0 ? 'active' : ''">
            <div class="trend_2i row">
              <LatestListItem 
              v-for="movie in movies" :key="movie.id" :movie="movie"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import LatestListItem from '@/components/HomeMovieComponents/LatestListItem'

export default {
  name: 'LatestList',
  components: {
    LatestListItem,
  },
  computed: {
    latestList() {
      const tmp = this.$store.state.latestList
      let res = []
      let temp = []
      for (let i = 1; i <= tmp.length; i++) {
        temp.push(tmp[i - 1])
        if(i % 4 == 0) {
          res.push(temp)
          temp = []
        }
      }
      return res
    }
  }
}
</script>

<style>
</style>
