<template>
  <div id="app" style="background-color: #eee">
    
    <!-- Navbar (sit on top) -->
    <div class="w3-top" style="position: fixed;">
      <div class="w3-bar w3-white w3-wide w3-padding w3-card">
        <!-- Logo -->
        <router-link to="/" class="w3-bar-item w3-button"><b>BR</b> Architects</router-link>
        <!-- Float links to the right. Hide them on small screens -->
        <b-nav class="w3-right w3-hide-small">
          <span>
            <b-nav-item><router-link to="/" class="w3-bar-item w3-button">Home</router-link></b-nav-item>
          </span>
          <span>
            <b-nav-item><router-link to="/movie/all" class="w3-bar-item w3-button">Movie</router-link></b-nav-item>
          </span>
            <b-nav-item><router-link to="/community/articles" class="w3-bar-item w3-button">Community</router-link></b-nav-item>
          <span v-if="isLogin">
            <b-nav-item><router-link to="/mypage" class="w3-bar-item w3-button">MyPage</router-link></b-nav-item>
          </span>
          <span v-if="isLogin">
            <b-nav-item style="margin-top:8px;" @click="logout">Logout</b-nav-item>
          </span>
          <span v-if="!isLogin">
            <b-nav-item><router-link to="/login" class="w3-bar-item w3-button">Login</router-link></b-nav-item>
          </span>
          <span v-if="!isLogin">
            <b-nav-item><router-link to="/signup" class="w3-bar-item w3-button">SignUp</router-link></b-nav-item>
          </span>
        </b-nav>
      </div>
    </div>

    <div style="margin-top: 60px;">
      <router-view/>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'app',
    data() {
      return {
        // isLogin: false,
      }
    },
    // 서버에 저장된 최고평점 영화 가져오기(3500개 정도라 시간이 걸려서 처음 페이지 열리자마자 가져오기)
    mounted() {
    if (this.$store.state.popularMovie === null && this.$store.getters.isLogin) {
      this.$store.dispatch('popularMovie');
      }
    },
    computed: {
      // 로그인 여부 확인
      isLogin() {
        return this.$store.getters.isLogin
      }
    },
    methods: {
      logout() {
        this.$store.dispatch('logout')
      },

      getUser() {
        this.$store.dispatch('getuser')
      }
    },
    created() { 
      this.getUser()
    },
    // mounted() {
    //   this.isLogin = 
    //   console.log(!this.isLogin)
    // }
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
