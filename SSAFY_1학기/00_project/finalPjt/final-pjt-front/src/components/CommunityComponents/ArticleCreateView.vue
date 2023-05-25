<template>
  <div class="container">
    <!-- Heading -->
    <!--Grid row-->
    <div class="row d-flex justify-content-center">
      <h2 class="my-5 text-center">게시글 작성하기</h2>
      <!--Grid column-->
      <div class="col-md-8 mb-4">
          <!--Card-->
          <div class="card p-4">
            <div class="form-outline mb-4">
              <b-form-input id="input-title" :class="{ 'active': title }" class="form-control form-control-lg border" style="margin-bottom: 0px;" v-model="title"></b-form-input>
              <label class="form-label" for="input-title">제목</label>
            </div>

            <div class="form-outline mb-4">
              <b-form-textarea
                id="textarea"
                v-model="content"
                :class="{ 'active': content }"
                rows="10"
                max-rows="10"
                class="border"
              ></b-form-textarea>
              <label class="form-label" for="textarea">내용</label>
            </div>

            <div class="form-outline mb-4">
              <input type="file" class="form-control border" id="customFile" :v-model="uploadImg" @change="handleFileChange"/>
              <div>
                <img class="mt-3" style="width: 100%" v-if="uploadImg" :src="uploadImgUrl" alt="Uploaded Image">
              </div>
            </div>

          <div class="row mb-3">
            <div class="col-md-6 mb-2">
              <button class="btn btn-primary" type="button" style="width: 95%;" @click="createArticle">작성하기</button>
            </div>

            <div class="col-md-6 mb-2">
              <button class="btn btn-primary" type="reset" style="width: 95%;" @click="reset">초기화</button>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateView',
  data() {
    return {
      API_URL: this.$store.state.API_URL,

      title: null,
      content: null,
      uploadImg: null,
      uploadImgUrl: null,
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  methods: {
    loginCheck(){
      if (!this.isLogin) {
        alert('로그인후 작성 가능합니다')
        this.$router.push({name:'login'})
      }
    },
    createArticle() {
      const title = this.title
      const content = this.content
      const hit = 0

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${this.API_URL}/articles/`,
        data: { title, content, image: this.uploadImg, hit },
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`,
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(() => {
        this.$router.push({name: 'articles'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    handleFileChange(event) {
      const file = event.target.files[0];
      this.uploadImg = file;

      // FileReader 객체를 사용하여 이미지 파일을 읽고 데이터 URL로 변환
      const reader = new FileReader();
      reader.onload = (e) => {
        this.uploadImgUrl = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    reset() {
      this.title = null
      this.content = null
      this.uploadImg = null
      this.uploadImgUrl = null
    },
  }
}
</script>

<style>

</style>
