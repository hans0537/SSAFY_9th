<template>
<section id="header" class="container mt-5">
  <nav class="navbar navbar-expand-md">
    <div class="container">
      <div class="collapse navbar-collapse d-flex justify-content-center">

        <div class="navbar-nav mb-0">
          
          <router-link to="/community/articles" class="nav-link" :class="{ 'active': $route.path === '/community/articles' }">자유게시판</router-link>

          <router-link to="/community/choquiz" class="nav-link" :class="{ 'active': $route.path === '/community/choquiz' }">영화 초성 퀴즈</router-link>

          <router-link to="/community/overquiz" class="nav-link" :class="{ 'active': $route.path === '/community/overquiz' }">영화 줄거리 퀴즈</router-link>

          <router-link to="/community/worldcup" class="nav-link" :class="{ 'active': $route.path === '/community/worldcup' }">영화 월드컵</router-link>
        </div>
      </div>
    </div>
  </nav>

  <router-view/>

</section>
<!-- 
<div class="container" style="background-color: rgb(238, 238, 238)">
  <div class="nav-box">
    <div class="row contact_1 bg_gray  pt-5 pb-5">
      <div class="col-md-3">
        <div class="contact_1i row">
          <div class="col-md-10 col-10">
            <div class="contact_1ir">
              <h5 class="col_red">커뮤니티</h5>
            </div>
          </div>
        </div>
      </div>   
      
      <div class="col-md-3">
        <div class="contact_1i row">
          <div class="col-md-10 col-10">
            <div class="contact_1ir">
              <h5 class="col_red">초성 퀴즈</h5>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-3">
        <div class="contact_1i row">
          <div class="col-md-10 col-10">
            <div class="contact_1ir">
              <h5 class="col_red">줄거리 퀴즈</h5>
            </div>
          </div>
        </div>
      </div>

      <div class="col-md-3">
        <div class="contact_1i row">
          <div class="col-md-10 col-10">
            <div class="contact_1ir">
              <h5 class="col_red">영화 월드컵</h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div> -->
</template>

<script>
export default {
  name: 'CommunityView',
}
</script>

<style scoped>
.nav-box {
  position: relative;
  top: 30px;
  margin: 0 auto;
  background-color: white;
  width: 90%;
  height: 70px;
  border-radius: 10px;
}
</style>