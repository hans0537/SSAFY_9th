<template>
  <section id="header" class="container mt-5">
    <nav class="navbar bg-dark" data-bs-theme="dark">
      <div class="container">
        <router-link to="/movie/all" class="nav-link" :class="{ 'active': $route.path === '/movie/all' }">전체</router-link>
        <router-link to="/movie/genre/action" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/action' }">장르</router-link>
        <router-link to="/movie/average" class="nav-link" :class="{ 'active': $route.path === '/movie/average' }">인기 영화</router-link>
        <router-link to="/movie/now" class="nav-link" :class="{ 'active': $route.path === '/movie/now' }">현재 상영작</router-link>
        <router-link to="/movie/upcoming" class="nav-link" :class="{ 'active': $route.path === '/movie/upcoming' }">상영 예정작</router-link>
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
