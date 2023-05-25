<template>
  <div class="container">
    <section id="header" class="mt-5">
      <nav class="navbar community-nav">
        <div class="container">
          <router-link to="/community/articles" class="nav-link" :class="{ 'active': $route.path === '/community/articles' }"><h5 class="mt-1">자유게시판</h5></router-link>
          <router-link to="/community/choquiz" class="nav-link" :class="{ 'active': $route.path === '/community/choquiz' }"><h5 class="mt-1">영화 초성 퀴즈</h5></router-link>
          <router-link to="/community/overquiz" class="nav-link" :class="{ 'active': $route.path === '/community/overquiz' }"><h5 class="mt-1">영화 줄거리 퀴즈</h5></router-link>
          <router-link to="/community/worldcup" class="nav-link" :class="{ 'active': $route.path === '/community/worldcup' }"><h5 class="mt-1">영화 월드컵</h5></router-link>
        </div>
      </nav>
    </section>

    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'CommunityView',
}
</script>

<style scoped>
nav a {
  font-weight: bold;
  color: white;
  padding: 0px 70px;
}

nav a.router-link-exact-active {
  color: #E309E8;
}

.selected {
  color: black;
}

.community-nav{
  background-color:black;
  width: 98%;
  margin: 0px auto;
  margin-bottom: 30px;
  border-radius: 10px;
}
</style>