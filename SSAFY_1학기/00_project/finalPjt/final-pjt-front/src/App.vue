<template>
  <div id="app">
    
    <!-- Navbar (sit on top) -->
    <div class="w3-top">
      <div class="w3-bar w3-white w3-wide w3-padding w3-card">
        <!-- Logo -->
        <a href="#home" class="w3-bar-item w3-button"><b>BR</b> Architects</a>

        <!-- Float links to the right. Hide them on small screens -->
        <b-nav class="w3-right w3-hide-small">
          <b-nav-item><router-link to="/" class="w3-bar-item w3-button">Home</router-link></b-nav-item>
          <b-nav-item><router-link to="/login" class="w3-bar-item w3-button">Login</router-link></b-nav-item>
          <b-nav-item><router-link to="/signup" class="w3-bar-item w3-button">SignUp</router-link></b-nav-item>
        </b-nav>
      </div>
    </div>

    <router-view/>

  </div>
</template>

<script>

  export default {
    name: 'app',
    data() {
      return {
      }
    },
    methods: {
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
