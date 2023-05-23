<template>
  <div>
    <hr>
    <nav class="navbar" style="background-color:azure;">
      <div class="container" style="display:flex; justify-content: space-between;">
        <router-link to="/movie/genre/action" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/action' }"><h5 class="mt-1">액션</h5></router-link>
        <router-link to="/movie/genre/adventure" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/adventure' }"><h5 class="mt-1">모험</h5></router-link>
        <router-link to="/movie/genre/animation" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/animation' }"><h5 class="mt-1">애니메이션</h5></router-link>
        <router-link to="/movie/genre/comedy" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/comedy' }"><h5 class="mt-1">코미디</h5></router-link>
        <router-link to="/movie/genre/crime" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/crime' }"><h5 class="mt-1">범죄</h5></router-link>
        <router-link to="/movie/genre/documentary" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/documentary' }"><h5 class="mt-1">다큐멘터리</h5></router-link>
        <router-link to="/movie/genre/drama" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/drama' }"><h5 class="mt-1">드라마</h5></router-link>
        <router-link to="/movie/genre/family" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/family' }"><h5 class="mt-1">가족</h5></router-link>
        <router-link to="/movie/genre/fantasy" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/fantasy' }"><h5 class="mt-1">판타지</h5></router-link>
      </div>
      <div class="container" style="display:flex; justify-content: space-between;">
        <router-link to="/movie/genre/history" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/history' }"><h5 class="mt-1">역사</h5></router-link>
        <router-link to="/movie/genre/horror" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/horror' }"><h5 class="mt-1">공포</h5></router-link>
        <router-link to="/movie/genre/music" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/music' }"><h5 class="mt-1">음악</h5></router-link>
        <router-link to="/movie/genre/mystery" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/mystery' }"><h5 class="mt-1">미스터리</h5></router-link>
        <router-link to="/movie/genre/romance" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/romance' }"><h5 class="mt-1">로맨스</h5></router-link>
        <router-link to="/movie/genre/science" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/science' }"><h5 class="mt-1">SF</h5></router-link>
        <router-link to="/movie/genre/tv" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/tv' }"><h5 class="mt-1">TV영화</h5></router-link>
        <router-link to="/movie/genre/thriller" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/thriller' }"><h5 class="mt-1">스릴러</h5></router-link>
        <router-link to="/movie/genre/war" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/war' }"><h5 class="mt-1">전쟁</h5></router-link>
        <router-link to="/movie/genre/western" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/western' }"><h5 class="mt-1">서부</h5></router-link>
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