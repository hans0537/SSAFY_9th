<template>
  <tr>
    <th scope="row" @click="articleDetail">{{(index + 1) + numSelected * (page - 1)}}</th>
    <td class="fw-bold"  @click="articleDetail">{{article?.title}}</td>
    <td @click="articleDetail">{{ formatDate(article?.created_at)}}</td>
    <td @click="goToUserProfile">
      <div class="team">
        <a href="javascript: void(0);" class="team-member" data-toggle="tooltip" data-placement="top" title="" data-original-title="Roger Drake">
            <img v-if="article?.user.image_base64"  :src="getImageSrc(article?.user.image_base64)" class="rounded-circle avatar-xs" alt="" />
            <img v-else src="../../assets/baseProfile.png" class="rounded-circle avatar-xs" alt="" />
        </a>
        <span class="text-success fs-6 fw-bold ms-2"><i class="mdi mdi-checkbox-blank-circle mr-1"></i> {{article?.user.username}}</span>
      </div>
    </td>
    <td @click="articleDetail">
      <div class="team">
        <a href="javascript: void(0);" class="team-member" data-toggle="tooltip" data-placement="top" title="" data-original-title="Roger Drake">
            <img src="https://bootdey.com/img/Content/avatar/avatar6.png" class="rounded-circle avatar-xs" alt="" />
        </a>
      </div>
    </td>
    <td @click="articleDetail">
      <p>{{article?.hit}}</p>
    </td>

    <td>
      <div class="action" v-if="article.user.username===checkUser">
        <span class="text-success mr-4" data-toggle="tooltip" data-placement="top" title="" data-original-title="Edit" @click="goToUpdate">
          <i @mouseover="upHere1 = true" @mouseleave="upHere1 = false" class="fa-solid fa-pencil fa-xl me-2" :class="{'fa-bounce' : upHere1}" style="color: #198754;"></i>
        </span>

        <span class="text-danger" data-toggle="tooltip" data-placement="top" title="" data-original-title="Close" @click="articleDelete">
          <i @mouseover="upHere2 = true" @mouseleave="upHere2 = false" class="fa-solid fa-trash fa-xl"  :class="{'fa-bounce' : upHere2}" style="color: #ff0000;"></i>
        </span>
      </div>
    </td>
  </tr>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ArticlesListView',
  data(){
    return {
      upHere1: false,
      upHere2: false,
    }
  },
  props: {
    article: Object,
    index: Number,
    numSelected: Number,
    page: Number,
    checkUser: String,
  },
  methods: {
    formatDate(dateString) {
      const date = new Date(dateString);
      const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
      return date.toLocaleDateString('en-US', options);
    },

    articleDetail() {
      // 조회수 증가
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/articles/hit/${this.article.id}/`,
        data: {
          title: this.article.title,
          content: this.article.content,
          hit: this.article.hit + 1,
        },
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then((res) => {
        console.log(res)
        this.$router.push({ name: 'articleDetail', params: { id: this.article.id } });
      })
      .catch((err) => {
        alert('열람 권한이 없습니다. 로그인 하십시오')
        console.log(err)
      })
    },

    articleDelete(){
      if (!confirm("해당 게시글을 삭제 하시겠습니까?")) {
        return
      } else {
        axios({
          method: 'delete',
          url: `http://127.0.0.1:8000/articles/${this.article.id}/`,
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`
          }
        })
        .then((res) => {
          console.log(res)
          // 삭제 후 목록 다시 불러오기
          this.$emit('delete-article');
        })
        .catch((err) => {console.log(err)})
      }
    },

    goToUpdate() {
      this.$router.push({ name: 'articleUpdate', params: { id: this.article.id } });
    },

    goToUserProfile() {
      if(this.article.user.username === this.checkUser){
        this.$router.push({ name: 'mypage'})
      }else {
        this.$router.push({ name: 'userprofile', params: {id: this.article.user.id} })
      }
    },

    getImageSrc(base64String) {
      return `data:image/png;base64, ${base64String}`; // Base64 데이터를 이미지 src 형식으로 변환
    },
  }
}


</script>

<style>
body{
    background:#f3f3f3;
    margin-top:20px;
    color: #616f80;
}
.card {
    border: none;
    margin-bottom: 24px;
    -webkit-box-shadow: 0 0 13px 0 rgba(236,236,241,.44);
    box-shadow: 0 0 13px 0 rgba(236,236,241,.44);
}

.avatar-xs {
    height: 2.3rem;
    width: 2.3rem;
}  

</style>