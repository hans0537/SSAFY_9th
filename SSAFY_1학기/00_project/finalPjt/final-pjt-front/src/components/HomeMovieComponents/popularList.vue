<template>
  <section id="trend" class="pt-4 pb-5 mt-5" >
    <div class="container">
      <div class="row trend_1" style="display:flex; justify-content: space-between;">
        <div class="col-md-6 col-6">
          <h4 class="trend_1l" style="text-align:left;">Popularity <span class="col_red">Movies</span></h4>
        </div>
        <div class="col-md-6 col-6 text-end">
          <h6 class="mb-0">
            <router-link to="/movie/average" class="button" style="text-decoration: none;">View All</router-link>
          </h6>
        </div>
      </div>
  
      <div class="row trend_2 mt-4">
        <div id="carouselExampleCaptions3" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleCaptions3" data-bs-slide-to="0" class="active" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions3" data-bs-slide-to="1" aria-label="Slide 2" aria-current="true"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions3" data-bs-slide-to="2" aria-label="Slide 3" aria-current="true"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions3" data-bs-slide-to="3" aria-label="Slide 4" aria-current="true"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions3" data-bs-slide-to="4" aria-label="Slide 5" class="" aria-current="true"></button>
          </div>
          
          <div class="carousel-inner"> 
            <div class="carousel-item" v-for="(movies, index) in popularMovie" :key="index" :class="index===0 ? 'active' : ''">
              <div class="trend_2i row">
                <popularListItem 
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
import popularListItem from './popularListItem.vue'
export default {
  name: 'popularList',
  data() {
    return {
      popularList:null,
    }
  },
  components: {
    popularListItem,
  },
  computed: {
    popularMovie() {
      const tmp = this.$store.state.popularMovie
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