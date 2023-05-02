<template>
  <div id="app">
    <HomeBox/>
    <AboutBox/>
  </div>
</template>

<script>
import AboutBox from '@/views/AboutBox'
import HomeBox from '@/views/HomeBox'

export default {
  name: 'App',
  components: {
    AboutBox,
    HomeBox,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
