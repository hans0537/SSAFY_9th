<template>
<section class="vh-100" style="background-color:  #eee;">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card shadow-2-strong" style="border-radius: 1rem;">
          <div class="card-body p-5 text-center">

            <h3 class="mb-5">Find Password</h3>

            <div class="form-outline mb-4">
              <b-form-input id="input-username" :class="{ 'active': username }" class="form-control form-control-lg border" style="margin-bottom: 0px;" v-model="username" trim></b-form-input>
              <label class="form-label" for="input-username">Username</label>
            </div>

            <div class="form-outline mb-4">
              <b-form-input id="input-email" :class="{ 'active': email }" class="form-control form-control-lg border" style="margin-bottom: 0px;" v-model="email" trim></b-form-input>
              <label class="form-label" for="input-email">Email</label>
            </div>

            <button class="btn btn-primary btn-lg btn-block" @click="findPw">Find</button>

            <hr class="my-4">

            <h5 v-if="find">{{this.username}}님 비밀번호를 변경해 주세요</h5>
            <form>
              <div v-if="find" class="form-outline mb-4">
                <b-form-input id="input-password1" class="form-control form-control-lg border" style="margin-bottom: 0px;" :class="{ 'active': password1 }" type="password" placeholder="PASSWORD" v-model="password1" trim autocomplete="new-password"/>
                <label class="form-label" for="input-password1">Password</label>
              </div>

              <div v-if="find" class="form-outline mb-4">
                <b-form-input id="input-password2" class="form-control form-control-lg border" style="margin-bottom: 0px;" :class="{ 'active': password2 }" type="password" placeholder="PASSWORD" v-model="password2" trim autocomplete="new-password"/>
                <label class="form-label" for="input-password2">Confirm Password</label>
              </div>
            </form>
            
            <button v-if="find" class="btn btn-primary btn-lg btn-block" @click="changePW">비밀번호 변경하기</button>

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
  name: "FindPwView",
  data() {
    return {
      API_URL: this.$store.state.API_URL,

      username: '',
      email: '',
      find: false,

      password1 : '',
      password2 : '',
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

    findPw() {
      const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

      if (this.username.length < 3) {
        alert("알파벳/숫자 3글자 이상 적어주세요")
        return
      } else if (!emailRegex.test(this.email)) {
        alert("올바른 이메일을 입력해주세요")
        return
      }

      axios({
        method: 'get',
        url: `${this.API_URL}/accounts/findPw/`,
        params: {
          email: this.email,
          username: this.username,
        }
      })
      .then(() => {
        this.find = true
      })
      .catch((err) => {
        console.log(err)
        alert('해당 유저는 등록되어 있지 않습니다.')
      }) 
    },

    changePW() {
      if (this.password1.length < 10) {
        alert("비밀번호 10자 이상 적어주세요")
        return
      } else if (this.password1 !== this.password2){
        alert("비밀번호가 일치하지 않습니다")
        return
      }

      axios({
        method: 'put',
        url: `${this.API_URL}/accounts/findPw/`,
        data: {
          username: this.username,
          followers: [],
          password1: this.password1,
          password2: this.password2,
        },
        params: {
          email: this.email,
          username: this.username,
        }
      })
      .then(() => {
        alert('비밀번호 변경에 성공했습니다. 로그인 하십시오')
        this.$router.push({name: 'login'})
      })
      .catch((err) => {
        console.log(err)
        alert('비밀번호 변경에 실패 하셨습니다.')
      }) 
    },


  }
}
</script>

<style>
</style>