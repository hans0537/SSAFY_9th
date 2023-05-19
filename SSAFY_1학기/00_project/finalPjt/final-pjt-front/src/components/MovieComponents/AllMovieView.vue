<template>
  <div>
    <h1>전체 영화</h1>
    <AllMovieItems />
  </div>
</template>

<script>
import AllMovieItems from './AllMovieItems.vue';
export default {
  name:'AllMovieView',
  components: {
    AllMovieItems
  }
}
</script>

<style>

</style>