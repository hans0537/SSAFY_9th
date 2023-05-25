<template>
  <div id="app" style="background-color: #eee;">
    <nav class="navbar navbar-expand-lg sticky-top" style="background-color: white;">
      <!-- Container wrapper -->
      <div class="container-fluid">
        <a class="navbar-brand" href="/">
          <img
            src="./assets/logo.png"
            class="mx-4"
            height="50"
            alt="Logo"
            loading="lazy"
          />
        </a>
        <!-- Toggle button -->
        <button
          class="navbar-toggler"
          type="button"
          data-mdb-toggle="collapse"
          data-mdb-target="#navbarRightAlignExample"
          aria-controls="navbarRightAlignExample"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <i class="fas fa-bars"></i>
        </button>

        <!-- Collapsible wrapper -->
        <div class="collapse navbar-collapse" id="navbarRightAlignExample">
          <!-- Left links -->
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <b-nav-item><router-link to="/" class="w3-bar-item w3-button">Home</router-link></b-nav-item>
            </li>
            <li class="nav-item">
              <b-nav-item><router-link to="/movie/all" class="w3-bar-item w3-button">Movie</router-link></b-nav-item>
            </li>
            <li class="nav-item">
              <b-nav-item><router-link to="/community/articles" class="w3-bar-item w3-button">Community</router-link></b-nav-item>
            </li>
            <li class="nav-item" v-if="isLogin">
              <b-nav-item><router-link to="/mypage" class="w3-bar-item w3-button">MyPage</router-link></b-nav-item>
            </li>
            <li class="nav-item" v-if="isLogin">
              <b-nav-item @click="logout"><router-link to="//" class="w3-bar-item w3-button">Logout</router-link></b-nav-item>
            </li>
            <li class="nav-item" v-if="!isLogin">
              <b-nav-item><router-link to="/login" class="w3-bar-item w3-button">Login</router-link></b-nav-item>
            </li>
            <li class="nav-item" v-if="!isLogin">
              <b-nav-item><router-link to="/signup" class="w3-bar-item w3-button">SignUp</router-link></b-nav-item>
            </li>

          </ul>
          <!-- Left links -->
        </div>
        <!-- Collapsible wrapper -->
      </div>
      <!-- Container wrapper -->
    </nav>

    <router-view/>
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
      },
      getLatest() {
      this.$store.dispatch('getLatest')
      },
      getUpComing() {
        this.$store.dispatch('getUpComing')
      },
      getPopular() {
        this.$store.dispatch('popularMovie')
      },
      getall() {
        this.$store.dispatch('getall')
      },
    },
    created() { 
      this.getUser()
      this.getall();
      this.getLatest();
      this.getUpComing();
      this.getPopular();
      this.$store.state.dataLoaded = true;
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
  color: #E309E8;
}

</style>
