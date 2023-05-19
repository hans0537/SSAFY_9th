<template>
  <div>
    <h1>현재 상영작</h1>
    <NowMovieItems />
  </div>
</template>

<script>
import NowMovieItems from './NowMovieItems.vue';
export default {
  name:'NowMovieView',
  components: {
    NowMovieItems
  }
}
</script>

<style>

</style>