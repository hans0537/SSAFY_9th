<template>
<section class="vh-100" style="background-color:  #eee;">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card shadow-2-strong" style="border-radius: 1rem;">
          <div class="card-body p-5 text-center">

            <h3 class="mb-5">Find Username</h3>
            <div class="form-outline mb-4">
              <b-form-input id="input-email" :class="{ 'active': email }" class="form-control form-control-lg border" style="margin-bottom: 0px;" v-model="email" trim></b-form-input>
              <label class="form-label" for="input-email">Email</label>
            </div>

            <button class="btn btn-primary btn-lg btn-block" @click="findUsername">Find</button>

            <hr class="my-4">

            <h5 v-if="username">username : {{username}}</h5>
            <button v-if="username" class="btn btn-primary btn-lg btn-block" @click="goToLogin">Login</button>
            <button v-if="username" class="btn btn-primary btn-lg btn-block" @click="goToPw">Find Password</button>

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
  name: "FindUsernameView",
  data() {
    return {
      username: '',
      email: '',
    }
  },
  computed: {
  },
  methods: {
    goToLogin() {
      this.$router.push({name: 'login'})
    },

    goToPw() {
      this.$router.push({name: 'findPw'})
    },

    findUsername() {
      console.log(this.email)
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/findUsername/`,
        params: {
          email: this.email
        }
      })
      .then((res) => {
        console.log(res)
        this.username = res.data.username
        // this.$store.dispatch('login', res.data.access)
      })
      .catch((err) => {
        console.log(err)
        alert('해당 이메일은 등록되어 있지 않습니다.')
      }) 
    }
  }
}
</script>

<style>
</style>