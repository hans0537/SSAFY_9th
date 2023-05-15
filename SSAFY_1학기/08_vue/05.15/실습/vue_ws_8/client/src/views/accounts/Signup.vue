<template>
  <div>
    <form @submit.prevent="signup">
      <div>
        <label for="username">Username: </label>
        <input type="text" id="username" v-model="username">
      </div>

      <div>
        <label for="pw">Password: </label>
        <input type="password" id="pw" v-model="pw">
      </div>

      <div>
        <label for="confirm_pw">Confirm Password: </label>
        <input type="password" id="confirm_pw" v-model="confirm_pw">
      </div>

      <button type="submit">회원가입</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Singup',
  data: function () {
    return {
      username: '',
      pw: '',
      confirm_pw: '',
    }
  },
  methods: {
    signup: function () {
      if (!this.username){
        alert('username을 입력하세요')
        return
      } else if (!this.pw){
        alert('비밀번호를 입력하세요')
        return
      } else if (!this.confirm_pw){
        alert('비밀번호 확인을 입력하세요')
        return
      } else if (this.pw !== this.confirm_pw) {
        alert('비밀번호가 일치하지 않습니다.')
        return
      }

      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: {
          username: this.username,
          password1: this.pw,
          password2: this.confirm_pw,
        }
      })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
