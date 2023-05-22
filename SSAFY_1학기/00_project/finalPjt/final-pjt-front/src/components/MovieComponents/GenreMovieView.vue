<template>
  <div>
    <hr>
    <nav class="navbar bg-dark" data-bs-theme="dark">
      <div class="container" style="display:flex; justify-content: space-between;">
        <router-link to="/movie/genre/action" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/action' }">액션</router-link>
        <router-link to="/movie/genre/adventure" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/adventure' }">모험</router-link>
        <router-link to="/movie/genre/animation" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/animation' }">애니메이션</router-link>
        <router-link to="/movie/genre/comedy" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/comedy' }">코미디</router-link>
        <router-link to="/movie/genre/crime" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/crime' }">범죄</router-link>
        <router-link to="/movie/genre/documentary" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/documentary' }">다큐멘터리</router-link>
        <router-link to="/movie/genre/drama" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/drama' }">드라마</router-link>
        <router-link to="/movie/genre/family" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/family' }">가족</router-link>
        <router-link to="/movie/genre/fantasy" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/fantasy' }">판타지</router-link>
      </div>
      <div class="container" style="display:flex; justify-content: space-between;">
        <router-link to="/movie/genre/history" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/history' }">역사</router-link>
        <router-link to="/movie/genre/horror" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/horror' }">공포</router-link>
        <router-link to="/movie/genre/music" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/music' }">음악</router-link>
        <router-link to="/movie/genre/mystery" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/mystery' }">미스터리</router-link>
        <router-link to="/movie/genre/romance" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/romance' }">로맨스</router-link>
        <router-link to="/movie/genre/science" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/science' }">SF</router-link>
        <router-link to="/movie/genre/tv" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/tv' }">TV영화</router-link>
        <router-link to="/movie/genre/thriller" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/thriller' }">스릴러</router-link>
        <router-link to="/movie/genre/war" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/war' }">전쟁</router-link>
        <router-link to="/movie/genre/western" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/western' }">서부</router-link>
      </div>
    </nav>
    <router-view/>

  </div>
</template>

<script>
export default {
  name:'GenreMovieView',
  data() {
    return {

    }
  },
  computed: {

  }
}
</script>

<style>

</style>