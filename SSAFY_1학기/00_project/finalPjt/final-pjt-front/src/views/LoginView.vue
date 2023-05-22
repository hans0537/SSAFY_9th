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

            <button class="btn btn-lg btn-block btn-primary" style="background-color: #dd4b39;"
              type="submit"><i class="fab fa-google me-2"></i> Sign in with google</button>

            <button class="btn btn-lg btn-block btn-primary mb-2" style="background-color: #3b5998;"
              type="submit"><i class="fab fa-facebook-f me-2"></i>Sign in with facebook</button>

          </div>
        </div>
      </div>
    </div>
  </div>

</section>
</template>

<script>
import axios from 'axios'

export default {
  name: "LoginView",
  data() {
    return {
      username: '',
      password: '',
      rememberID: false,
    }
  },
  computed: {
  },
  methods: {
    login() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/auth/login/',
        data: {
          username: this.username,
          password: this.password
        }
      })
      .then((res) => {
        this.$store.dispatch('login', res.data.access)
      })
      .catch((err) => {
        console.log(err)
        alert('아이디와 비밀번호를 다시 확인해주세요')
      }) 
    }
  }
}
</script>

<style>
</style>