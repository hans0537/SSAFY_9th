<template>
  <div>
    <h1>장르별 영화</h1>
    <GenreMovieItems />
  </div>
</template>

<script>
import GenreMovieItems from './GenreMovieItems.vue';
export default {
  name:'GenreMovieView',
  components: {
    GenreMovieItems
  }
}
</script>

<style>

</style>