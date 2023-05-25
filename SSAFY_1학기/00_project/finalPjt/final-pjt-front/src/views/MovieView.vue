<template>
<div class="container">
  <section id="header" class="mt-5">
    <nav class="navbar movie-nav">
      <div class="container">
        <router-link to="/movie/all" class="nav-link" :class="{ 'active': $route.path === '/movie/all' }"><h5 class="mt-1">전체</h5></router-link>
        <router-link to="/movie/genre/action" class="nav-link" :class="{ 'router-link-exact-active router-link-active active': moviegenre.includes($route.path)}"><h5 class="mt-1">장르</h5></router-link>
        <router-link to="/movie/average" class="nav-link" :class="{ 'active': $route.path === '/movie/average' }"><h5 class="mt-1">인기 영화</h5></router-link>
        <router-link to="/movie/now" class="nav-link" :class="{ 'active': $route.path === '/movie/now' }"><h5 class="mt-1">현재 상영작</h5></router-link>
        <router-link to="/movie/upcoming" class="nav-link" :class="{ 'active': $route.path === '/movie/upcoming' }"><h5 class="mt-1">상영 예정작</h5></router-link>
      </div>
    </nav>
  </section>

  <router-view/>
</div>
</template>

<script>
export default {
  name: "MovieView",
  data() {
    return {
      moviegenre: ['/movie/genre/action','/movie/genre/adventure','/movie/genre/animation','/movie/genre/comedy','/movie/genre/crime','/movie/genre/documentary','/movie/genre/drama',
      '/movie/genre/family','/movie/genre/fantasy','/movie/genre/history','/movie/genre/horror','/movie/genre/music','/movie/genre/mystery','/movie/genre/romance','/movie/genre/science',
      '/movie/genre/tv','/movie/genre/thriller','/movie/genre/war','/movie/genre/western']
    };
  },
  methods: {
    
  },
};
</script>

<style scoped>
nav a {
  font-weight: bold;
  color: white;
  padding: 0 50px;
}

nav a.router-link-exact-active {
  color: #E309E8;
}

.selected {
  color: black;
}

.movie-nav{
  background-color:black;
  width: 98%;
  margin: 0 auto;
  border-radius: 10px;
}
</style>
