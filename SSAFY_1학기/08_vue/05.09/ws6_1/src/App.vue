<template>
  <div id="app" class="container">
    <div class="row">
      <nav class="col-3">
        <side-bar/>
      </nav>
      <div class="border col">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar'

export default {
  name: 'App',
  components: {
    SideBar
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
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
