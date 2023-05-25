<template>
  <div class="d-flex flex-start mb-5">
  
    <img v-if="comment?.user.image_base64" class="rounded-circle shadow-1-strong me-3"
      :src="getImageSrc(comment?.user.image_base64)" alt="avatar" width="65"
      height="65" />
  
    <img v-else class="rounded-circle shadow-1-strong me-3"
      src="../../assets/baseProfile.png" alt="avatar" width="65"
      height="65" />
  
    <div class="flex-grow-1 flex-shrink-1">
      <div>
        <div class="d-flex justify-content-between align-items-center">
          <p class="mb-1 fs-5 fw-bold">
            {{comment?.user.username}} 
          </p>
        </div>
        <p class="small text-start"> {{formatDate(comment?.created_at)}} </p>
  
        <div class="d-flex justify-content-between">
  
          <b-form-textarea
            v-if="updateShow"
            v-model="newComment"
            class="form-control" rows="2"
            max-rows="4"
            style="background: #fff;" :class="{'active' : newComment}"
            @keyup.enter="updateComment"
          ></b-form-textarea>
  
          <p v-if="!updateShow" class="small mb-0 fs-6 text-start" style="word-break: break-word;">
            {{comment?.content}}
          </p>
  
          <div class="action text-end" style="width: 50%;" v-if="comment.user.username===checkUser.username">
            <span class="text-success mr-4" data-toggle="tooltip" data-placement="top" title="" data-original-title="Edit" @click="updateToggle">
              <i @mouseover="upHere1 = true" @mouseleave="upHere1 = false" class="fa-solid fa-pencil fa-sm me-2" :class="{'fa-bounce' : upHere1}" style="color: #198754; cursor: pointer;"></i>
            </span>
  
            <span class="text-danger" data-toggle="tooltip" data-placement="top" title="" data-original-title="Close" @click="commentDelete">
              <i @mouseover="upHere2 = true" @mouseleave="upHere2 = false" class="fa-solid fa-trash fa-sm"  :class="{'fa-bounce' : upHere2}" style="color: #ff0000; cursor: pointer;"></i>
            </span>
          </div>
        </div>
  
      </div>
  
      <div v-if="cocommentShow" class="card py-3 border-0" style="background-color: #f8f9fa;">
        <div class="d-flex flex-start w-100">
          <img v-if="checkUser.image_base64" class="rounded-circle shadow-1-strong me-3"
            :src="getImageSrc(checkUser.image_base64)" alt="avatar" width="40"
            height="40" />
  
          <img v-else class="rounded-circle shadow-1-strong me-3"
            src="../../assets/baseProfile.png" alt="avatar" width="40"
            height="40" />
  
          <div class="form-outline w-100">
            <b-form-textarea
              id="comment"
              v-model="cocomment"
              class="form-control" rows="4"
              max-rows="6"
              style="background: #fff;"
              :class="{'active' : cocomment}"
              @keyup.enter="createCoComment"
            ></b-form-textarea>
            <label class="form-label" for="comment">Comment</label>
          </div>
        </div>
        <div class="d-flex justify-content-end mt-2 pt-1">
          <button type="button" class="me-2 btn btn-primary btn-sm" @click="createCoComment">댓글 달기</button>
          <button type="button" class="btn btn-outline-primary btn-sm" @click="cocommentCancel">취소</button>
        </div>
      </div>
  
      <hr >
  
    </div>
  </div>
</template>
  
<script>
  import axios from 'axios'
  
  export default {
    name: 'MovieCommentView',
    components: {
      
    },
    data() {
      return {
        API_URL: this.$store.state.API_URL,

        cocommentShow: false,
        cocomment: '',
  
        upHere1: false,
        upHere2: false,
  
        updateShow: false,
        newComment: '',
  
      }
    },
    props: {
      comment: Object,
      movieId: Number,
      checkUser: Object,
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
  
      commentDelete() {
        if (!confirm("해당 댓글을 삭제 하시겠습니까?")) {
          return
        } else {
          axios({
            method: 'delete',
            url: `${this.API_URL}/movies/${this.movieId}/review/${this.comment.id}/`,
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`
            }
          })
          .then(() => {
            // 삭제 후 목록 다시 불러오기
            this.$emit('get-comments');
          })
          .catch((err) => {console.log(err)})
        }
      },
  
      updateComment() {
        axios({
          method: 'put',
          url: `${this.API_URL}/movies/${this.movieId}/review/${this.comment.id}/`,
          data: {
            content: this.newComment
          },
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`
          }
        })
        .then((res) => {
          console.log(res.data)
          this.newComment = ''
          this.updateShow = false
          // 수정 후 목록 다시 불러오기
          this.$emit('get-comments');
        })
        .catch((err) => console.log(err))
      },
  
  
      updateToggle() {
        this.updateShow = !this.updateShow
        this.newComment = this.comment.content
      },
  
      getComments() {
        this.$emit('get-comments')
      },
  
      getImageSrc(base64String) {
        return `data:image/png;base64, ${base64String}`; // Base64 데이터를 이미지 src 형식으로 변환
      },
    }
  }
  </script>
  
  <style>
  
  </style>