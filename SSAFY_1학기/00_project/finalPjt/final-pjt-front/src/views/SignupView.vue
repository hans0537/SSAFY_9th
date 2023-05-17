<template>
  <section class="vh-100" style="background-color: #eee;">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-lg-12 col-xl-11">
          <div class="card text-black" style="border-radius: 25px;">
            <div class="card-body p-md-5">
              <div class="row justify-content-center">
                <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">

                  <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Sign up</p>

                  <form class="mx-1 mx-md-4">

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">

                        <b-form-input id="input-username" :class="{ 'active': username }" class="form-control border" style="margin-bottom: 0px;" v-model="username" :state="nameState" aria-describedby="input-username-feedback" trim></b-form-input>
                        <label class="form-label" for="input-username">Username</label>

                        <b-form-invalid-feedback id="input-username-feedback" style="text-align: right;">
                          알파벳/숫자 3글자 이상
                        </b-form-invalid-feedback>
                      </div>

                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">


                        <b-form-input id="input-password" class="form-control border" style="margin-bottom: 0px;" :class="{ 'active': password1 }" type="password" placeholder="PASSWORD" v-model="password1" :state="pwState" aria-describedby="input-pw-feedback" trim></b-form-input>
                        <label class="form-label" for="input-password">Password</label>

                        <b-form-invalid-feedback id="input-pw-feedback" style="text-align: right;">
                          비밀번호 10자 이상
                        </b-form-invalid-feedback>
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-key fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">


                        <b-form-input id="input-password2" class="form-control border" style="margin-bottom: 0px;" :class="{ 'active': password2 }" type="password" placeholder="PASSWORD" v-model="password2" :state="pwCheckState" aria-describedby="input-pwCheck-feedback" trim></b-form-input>
                        <label class="form-label" for="input-password2">Repeat your password</label>

                        <b-form-invalid-feedback id="input-pwCheck-feedback" style="text-align: right;">
                          비밀번호가 같지 않습니다
                        </b-form-invalid-feedback>

                      </div>
                    </div>

                    <div class="form-check d-flex justify-content-center mb-5">
                      <b-form-checkbox
                        id="checkSignUp"
                        name="checkSignUp"
                      >
                      </b-form-checkbox>
                      <label class="form-check-label" for="checkSignUp"> I agree all statements in <a href="#!">Terms of service</a> </label>
                    </div>

                    <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                      <button type="button" @click="signup" class="btn btn-primary btn-lg" >Register</button>
                    </div>

                  </form>

                </div>
                <div class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">

                  <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/draw1.webp"
                    class="img-fluid" alt="Sample image">

                </div>
              </div>
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
  name: "SignupView",
  data() {
    return {
      username: '',
      password1: '',
      password2: '',
    }
  },
  computed: {
    nameState(){
      return this.username.length >= 3 ? true: false
    },
    pwState(){
      return this.password1.length >= 10 ? true: false
    },
    pwCheckState() {
      return this.password2 && this.password1 === this.password2 ? true: false
    }
  },
  methods: {
    signup() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/auth/signup/',
        data: {
          username: this.username,
          password1: this.password1,
          password2: this.password2
        }
      })
      .then((res) => {
        console.log(res)
        this.$store.dispatch('signup', res.data.access)
      })
      .catch((err) => console.log(err))
    }
  }
}
</script>

<style>
  .cascading-right {
    margin-right: -50px;
  }

  @media (max-width: 991.98px) {
    .cascading-right {
      margin-right: 0;
    }
  }
</style>
