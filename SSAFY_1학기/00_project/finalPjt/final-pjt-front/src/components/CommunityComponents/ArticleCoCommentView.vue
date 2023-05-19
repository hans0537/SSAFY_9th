<template>
  <div class="d-flex flex-start mt-4">
    <a class="me-3" href="#">
      <img class="rounded-circle shadow-1-strong"
        src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/img%20(11).webp" alt="avatar"
        width="65" height="65" />
    </a>
    <div class="flex-grow-1 flex-shrink-1">
      <div>
        <div class="d-flex justify-content-between align-items-center">
          <p class="mb-1 fw-bold">
            {{cocomment?.user.username}}
          </p>
        </div>
        <p class="small text-start"> {{formatDate(cocomment?.created_ats)}} </p>
        <p class="small mb-0 border rounded ps-3 text-start">
          {{cocomment?.content}}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleCoCommentView',
  props: {
    cocomment: Object,
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
  }
}
</script>

<style>

</style>