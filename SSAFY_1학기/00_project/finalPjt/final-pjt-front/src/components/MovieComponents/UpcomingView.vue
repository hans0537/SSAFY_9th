<template>
  <div>
    <h1>상영 예정작</h1>
    <UpcomingItems />
  </div>
</template>

<script>
import UpcomingItems from './UpcomingItems.vue';
export default {
  name:'NowMovieView',
  components: {
    UpcomingItems
  }
}
</script>

<style>

</style>