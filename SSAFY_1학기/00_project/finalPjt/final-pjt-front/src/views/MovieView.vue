<template>
  <section id="header" class="container mt-5">
    <nav class="navbar" style="background-color:azure;">
      <div class="container">
        <router-link to="/movie/all" class="nav-link" :class="{ 'active': $route.path === '/movie/all' }"><h5 class="mt-1">전체</h5></router-link>
        <router-link to="/movie/genre/action" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/action' }"><h5 class="mt-1">장르</h5></router-link>
        <router-link to="/movie/average" class="nav-link" :class="{ 'active': $route.path === '/movie/average' }"><h5 class="mt-1">인기 영화</h5></router-link>
        <router-link to="/movie/now" class="nav-link" :class="{ 'active': $route.path === '/movie/now' }"><h5 class="mt-1">현재 상영작</h5></router-link>
        <router-link to="/movie/upcoming" class="nav-link" :class="{ 'active': $route.path === '/movie/upcoming' }"><h5 class="mt-1">상영 예정작</h5></router-link>
      </div>
    </nav>
    <router-view/>
  </section>
</template>

<script>
export default {
  name: "MovieView",
  data() {
    return {
    };
  },
  methods: {
    
  },
};
</script>

<style>
.selected {
  color: black;
}
</style>
