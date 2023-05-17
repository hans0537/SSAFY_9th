<template>
  <b-container role="group" class="p-5 login-form">
    <h1>로그인</h1>
    <b-row>
      <label for="input-username">아이디</label>
      <b-form-input id="input-username" placeholder="ID" v-model="username" :state="nameState" aria-describedby="input-username-feedback" trim></b-form-input>

      <b-form-invalid-feedback id="input-username-feedback" class="text-right">
        알파벳/숫자 3글자 이상
      </b-form-invalid-feedback>
    </b-row>
    
    <b-row>
      <label for="input-password">비밀번호</label>
      <b-form-input id="input-password" type="password" placeholder="PASSWORD" v-model="password" :state="pwState" aria-describedby="input-pw-feedback" trim></b-form-input>

      <b-form-invalid-feedback id="input-pw-feedback" class="text-right">
        비밀번호 10자 이상
      </b-form-invalid-feedback>
    </b-row>
    <br>
    <b-button variant="success" @click="login">로그인</b-button>
  </b-container>
</template>

<script>
import axios from 'axios'

export default {
  name: "LoginView",
  data() {
    return {
      username: '',
      password: '',
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
.login-form {
  background-color: rgb(160, 198, 255);
  box-shadow: 20px 20px 10px 0px lightgray;
}
</style>