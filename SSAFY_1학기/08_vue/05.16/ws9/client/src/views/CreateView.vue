<template>
  <b-container role="group" class="p-5 create-form">
    <h1>게시물 작성</h1>
    <b-row>
      <label for="input-title">제목</label>
      <b-form-input id="input-title" placeholder="제목" v-model="title" :state="titleState" aria-describedby="input-title-feedback" trim></b-form-input>

      <b-form-invalid-feedback id="input-title-feedback" class="text-right">
        제목은 필수로 작성...
      </b-form-invalid-feedback>
    </b-row>
    
    <b-row>
      <label for="input-content">내용</label>
      <b-form-textarea id="textarea-content" v-model="content" style="height: 300px"></b-form-textarea>
    </b-row>

    <br>
    <b-button variant="success" @click="create">작성하기</b-button>
  </b-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateView',
  data() {
    return {
      title: '',
      content: '',
    }
  },
  created() {
    if(!this.$store.getters.isLogin) {
      alert('로그인이 필요한 페이지입니다...')
      this.$router.push({ name: 'LogInView' })
    }
  },
  computed: {
    titleState() {
      return this.title !== '' ? true : false
    }
  },
  methods: {
    create() {
      const title = this.title
      const content = this.content
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/articles/',
        data: {
          title, content
        },
        headers: {
          Authorization: `Bearer ${this.$store.state.access}`
        }
      })
      .then((res) => {
        console.log(res)
        this.$router.push({name : 'article'})
      })
      .catch(err => console.log(err))
    }
  }

}
</script>

<style>
.create-form {
  background-color: rgb(160, 198, 255);
  box-shadow: 20px 20px 10px 0px lightgray;
}
</style>