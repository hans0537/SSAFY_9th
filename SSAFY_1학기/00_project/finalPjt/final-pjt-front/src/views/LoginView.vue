<template>
<section class="vh-100" style="background-color:  #eee;">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card shadow-2-strong" style="border-radius: 1rem;">
          <div class="card-body p-5 text-center">

            <h3 class="mb-5">Sign in</h3>
            <div class="form-outline mb-4">
              <b-form-input id="input-username" :class="{ 'active': username }" class="form-control form-control-lg border" style="margin-bottom: 0px;" v-model="username" :state="nameState" aria-describedby="input-username-feedback" trim></b-form-input>
              <label class="form-label" for="input-username">Username</label>

              <b-form-invalid-feedback id="input-username-feedback" style="text-align: right;">
                알파벳/숫자 3글자 이상
              </b-form-invalid-feedback>
            </div>

            <div class="form-outline mb-4">
              <b-form-input id="input-password" class="form-control form-control-lg border" style="margin-bottom: 0px;" :class="{ 'active': password }" type="password" placeholder="PASSWORD" v-model="password" :state="pwState" aria-describedby="input-pw-feedback" trim></b-form-input>
              <label class="form-label" for="input-password">Password</label>

              <b-form-invalid-feedback id="input-pw-feedback" style="text-align: right;">
                비밀번호 10자 이상
              </b-form-invalid-feedback>
            </div>

            <!-- Checkbox -->
            <div class="form-check d-flex justify-content-start mb-4" style="padding-left: 0px;">
              <b-form-checkbox
                id="checkID"
                v-model="rememberID"
                name="checkID"
              >
              </b-form-checkbox>
              <label class="form-check-label" for="checkID"> 아이디 저장 </label>

              <!-- <input class="form-check-input me-2" type="checkbox" value="" id="form1Example3" /> -->
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
    nameState(){
      return this.username.length >= 3 ? true: false
    },
    pwState(){
      return this.password.length >= 10 ? true: false
    }
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
        console.log(res)
        this.$store.dispatch('login', res.data.access)
      })
      .catch((err) => console.log(err))
    }
  }
}
</script>

<style>
</style>