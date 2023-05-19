<template>
<div class="d-flex flex-start mb-5">
  <img class="rounded-circle shadow-1-strong me-3"
    src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/img%20(10).webp" alt="avatar" width="65"
    height="65" />
  <div class="flex-grow-1 flex-shrink-1">
    <div>
      <div class="d-flex justify-content-between align-items-center">
        <p class="mb-1 fw-bold">
          {{comment?.user.username}} 
        </p>
        <div style="cursor: pointer; color: blue;" @click="cocommentToggle"><i class="fas fa-reply fa-xs"></i><span class="small"> reply</span></div>
      </div>
      <p class="small text-start"> {{formatDate(comment?.created_ats)}} </p>
      <p class="small mb-0 border rounded ps-3 text-start">
        {{comment?.content}}
      </p>
    </div>

    <div v-if="cocommentShow" class="card py-3 border-0" style="background-color: #f8f9fa;">
      <div class="d-flex flex-start w-100">
        <img class="rounded-circle shadow-1-strong me-3"
          src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/img%20(19).webp" alt="avatar" width="40"
          height="40" />
        <div class="form-outline w-100">
          <b-form-textarea
            id="comment"
            v-model="cocomment"
            class="form-control" rows="4"
            max-rows="6"
            style="background: #fff;"
            :class="{'active' : cocomment}"
          ></b-form-textarea>
          <label class="form-label" for="comment">Comment</label>
        </div>
      </div>
      <div class="d-flex justify-content-end mt-2 pt-1">
        <button type="button" class="me-2 btn btn-primary btn-sm" @click="createCoComment">댓글 달기</button>
        <button type="button" class="btn btn-outline-primary btn-sm" @click="cocommentCancel">취소</button>
      </div>
    </div>
    <ArticleCoCommentView 
      :v-if="comment.child_comments"
      v-for="cocomment in comment.child_comments" :key="cocomment.id"
      :cocomment="cocomment"/>

  </div>
</div>
</template>

<script>
import axios from 'axios'
import ArticleCoCommentView from '@/components/CommunityComponents/ArticleCoCommentView'

export default {
  name: 'ArticleCommentView',
  components: {
    ArticleCoCommentView
  },
  data() {
    return {
      cocommentShow: false,
      cocomment: '',
    }
  },
  props: {
    comment: Object,
    articleId: String,
  },
  methods: {
    formatDate(dateString) {
      const date = new Date(dateString);
      const now = new Date();

      const diff = Math.floor((now - date) / 1000); // 시간 차이를 초 단위로 계산
      const minute = 60;
      const hour = minute * 60;
      const day = hour * 24;

      if (diff < minute) {
        return "방금 전";
      } else if (diff < hour) {
        const minutesAgo = Math.floor(diff / minute);
        return `${minutesAgo}분 전`;
      } else if (diff < day) {
        const hoursAgo = Math.floor(diff / hour);
        return `${hoursAgo}시간 전`;
      } else {
        const daysAgo = Math.floor(diff / day);
        return `${daysAgo}일 전`;
      }
    },

    cocommentToggle(){
      this.cocommentShow = !this.cocommentShow
    },

    createCoComment() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/articles/${parseInt(this.articleId)}/comments/${this.comment.id}/`,
        data: {
          content: this.cocomment
        },
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then((res) => {
        console.log(res.data)
        this.cocomment = ''
        this.cocommentShow = false
        this.$emit('get-comments')
      })
      .catch((err) => console.log(err))
    },

    cocommentCancel() {
      this.cocomment = ''
      this.cocommentShow = false
    },
  }
}
</script>

<style>

</style>