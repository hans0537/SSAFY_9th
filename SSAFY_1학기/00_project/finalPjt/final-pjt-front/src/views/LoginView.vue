<template>
<section class="vh-100" style="background-color:  #eee;">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card shadow-2-strong" style="border-radius: 1rem;">
          <div class="card-body p-5 text-center">

            <h3 class="mb-5">Sign in</h3>
            <div class="form-outline mb-4">
              <b-form-input id="input-username" :class="{ 'active': username }" class="form-control form-control-lg border" style="margin-bottom: 0px;" v-model="username" trim></b-form-input>
              <label class="form-label" for="input-username">Username</label>
            </div>

            <div class="form-outline mb-4">
              <b-form-input id="input-password" class="form-control form-control-lg border" style="margin-bottom: 0px;" :class="{ 'active': password }" type="password" placeholder="PASSWORD" v-model="password" trim></b-form-input>
              <label class="form-label" for="input-password">Password</label>
            </div>

            <!-- Checkbox -->
            <div class="form-check d-flex justify-content-between mb-4" style="padding-left: 0px;">
              <div class="d-flex justify-content-start">
                <b-form-checkbox
                  id="checkID"
                  v-model="rememberID"
                  name="checkID"
                >
                </b-form-checkbox>
                <label class="form-check-label" for="checkID"> 아이디 저장 </label>
              </div>

              <div class="d-flex justify-content-between">
                <router-link to="/findUsername" class="text-decoration-none">아이디 찾기</router-link>&nbsp;|&nbsp;  
                <router-link to="/findPw" class="text-decoration-none">비밀번호 찾기</router-link>
              </div>

            </div>

            <button class="btn btn-primary btn-lg btn-block" @click="login">Login</button>

            <hr class="my-4">

            <!-- <button @click="kakaoLogin"
            class="btn btn-lg btn-block btn-primary" style="background-color: #dd4b39;"
              type="button"><i class="fab fa-google me-2"></i> Sign in with google</button> -->

            <!-- <button class="btn btn-lg btn-block btn-primary mb-2" style="background-color: #3b5998;"
              type="submit"><i class="fab fa-facebook-f me-2"></i>Sign in with facebook</button> -->

          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-html="htmlData">

  </div>
</section>
</template>

<script>
import axios from 'axios'

// const redirect_uri = 'http://127.0.0.1:8000/accounts/kakao'
// const kakao_API = '7d4a55845458a5954269e348d1f652b1'
// import { mapActions } from 'vuex';

export default {
  name: "LoginView",
  data() {
    return {
      API_URL: this.$store.state.API_URL,

      username: '',
      password: '',
      rememberID: false,
      htmlData: '',
      link: '',

    }
  },
  methods: {
    // ...mapActions(['login']),
    login() {
      axios({
        method: 'post',
        url: `${this.API_URL}/auth/login/`,
        data: {
          username: this.username,
          password: this.password
        }
      })
      .then((res) => {
        this.$store.dispatch('login', res.data.access)

        if(this.rememberID) {
          localStorage.setItem('rememberID', this.username)
        }else {
          localStorage.removeItem('rememberID')
        }
      })
      .catch((err) => {
        console.log(err)
        alert('아이디와 비밀번호를 다시 확인해주세요')
      }) 
    },

//     kakaoLogin() {
//   const redirectUri = encodeURIComponent(redirect_uri);
//   const kakaoAuthUrl = `https://kauth.kakao.com/oauth/authorize?client_id=${kakao_API}&redirect_uri=${redirectUri}&response_type=code`;

//   // 클라이언트가 카카오 인증 서버로 리다이렉트
//   window.location.href = kakaoAuthUrl;
// },

// // 인증 코드를 받았을 때 호출되는 함수
// handleAuthCode() {
//   // 현재 URL에서 인증 코드 추출
//   const urlParams = new URLSearchParams(window.location.search);
//   const authCode = urlParams.get('code');

//   if (authCode) {
//     // 서버에 인증 코드 전송하여 로그인 정보 요청
//     axios.get(`http://127.0.0.1:8000/accounts/kakao/?code=${authCode}`)
//       .then((res) => {
//         // 카카오 로그인 성공
//         const userData = res.data.user;
//         // 로컬 스토리지에 사용자 정보 저장
//         localStorage.setItem('user', JSON.stringify(userData));
//         window.location.href = 'http://localhost:8080/';

    //   axios.get('http://127.0.0.1:8000/accounts/kakao/')
    //     .then((res) => {
    //     // 로그인 성공한 경우 서버에서 반환한 데이터를 사용해 로그인 처리
    //       // 홈 화면으로 이동
    //       console.log(res)
    //       this.$router.push('/home');
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //       // 요청 실패
    //       // 에러 처리 로직 작성
    //     });
    // }
  },
}
</script>

<style>
</style>