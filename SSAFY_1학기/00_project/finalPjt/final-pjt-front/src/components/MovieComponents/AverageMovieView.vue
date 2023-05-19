<template>
  <div>
    <h1>평정 영화</h1>
    <div class="container">
      <div v-for="(movies, index) in AverageMovie" :key="index">
        <div>
          <div class="row">
            <AverageItems v-for="movie in movies" :key="movie.id" :movie="movie" class="col-2 mb-5"/>
          </div>
        </div>
      </div>
    </div>
        <!-- Pagination -->
        <nav aria-label="Page navigation example" class="d-flex justify-content-center mt-3">
      <ul class="pagination">
        <li class="page-item disabled">
          <a class="page-link" href="#" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
        <li class="page-item active"><a class="page-link" href="#">1</a></li>
        <li class="page-item"><a class="page-link" href="#">2</a></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
        <li class="page-item"><a class="page-link" href="#">4</a></li>
        <li class="page-item"><a class="page-link" href="#">5</a></li>
        <li class="page-item">
          <a class="page-link" href="#" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>  
    <!-- Pagination -->  
  </div>
</template>

<script>
import AverageItems from './AverageItems.vue';

export default {
  name: 'AverageMovieView',
  components: {
    AverageItems
  },
  created(){
    this.$store.dispatch('popularMovie')
  },
  computed: {
    AverageMovie() {
      const tmp = this.$store.state.popularMovie;
      console.log(tmp);
      let res = [];
      let temp = [];
      for (let i = 1; i <= tmp.length; i++) {
        temp.push(tmp[i - 1]);
        if (i % 4 === 0) {
          res.push(temp);
          temp = [];
        }
      }
      return res;
    }
  }
};
</script>

<style>

</style>
