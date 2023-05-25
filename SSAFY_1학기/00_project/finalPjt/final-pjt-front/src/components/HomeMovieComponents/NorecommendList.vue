<template>
  <section id="trend" class="pt-4 mt-5">
    <div class="container">
      <div class="row trend_1" style="display:flex; justify-content: space-between;">
        <div class="hr-line"></div>
        <div class="col-md-6 col-6">
          <div class="d-flex justify-content-start">
            <h4 class="trend_1l" style="text-align:left;">{{ user?.username || 'Anonymous' }}님 추천<span class="col_red"> 영화</span></h4>
          </div>
        </div>
        <div class="col-md-6 col-6 text-end">
          <h6 class="mb-0 txt" style="margin-right:10px;">
            {{ aditionalMsg }}
          </h6>
        </div>
      </div>
    </div>
    <div class="typewriter ps-2 mt-3">{{ recommendationMessage }}</div>
    <div v-if="user?.username" class="d-flex justify-content-end align-items-center pe-4">
      <i class="fa fa-light fa-hand-point-right fa-beat fa-2xxl pe-3" style="color: #e4ce3f; font-size: 30px;"></i>
      <router-link v-if="user !== null &&  user?.username !=='' " :to="{ name: 'worldcup' }" class="btn btn-success">월드컵 하러가기</router-link>
      <i class="fa fa-light fa-hand-point-left fa-beat fa-2xl ps-3" style="color: #e4ce3f; font-size: 30px;"></i>
    </div>
  </section>
</template>

<script>
export default {
  name: 'NorecommendList',
  data() {
    return {
      user: null,
    }
  },
  computed: {
    recommendationMessage() {
      if (this.user?.username ==='') {
        return '회원가입을 해주시면 유저님만을 위한 영화를 추천해드립니다.';
      } else {
        return `확보된 데이터가 없습니다 활동을 해주세요~~`;
      }
    },

    aditionalMsg(){
      if (this.user?.username !=='') {
        return `영화 추천을 위해 영화 상세페이지에서 한개 이상의 영화에 대해 좋아요를 눌러주시기 바라며 Community 내 영화 월드컵을 1회 이상 진행 해주시기 바랍니다.`;
      }
      return ''
    }
  },
  created() {
    this.user = this.$store.state.user;
    this.$store.dispatch('getuser')
  },
}
</script>

<style scoped>
.typewriter {
  font-size: 20px;
  font-family: Raleway;
  font-weight: bold;
	width: 21.5ch;
	white-space: nowrap;
	overflow: hidden;
	border-right: 4px solid #212121;
	animation: cursor 1s step-start infinite, 
    text 5s steps(18) alternate infinite;
}

@keyframes cursor {
	0%, 100% { 
    border-color: #212121; 
  }
}

@keyframes text {
	0% { 
    width: 0; 
  }
	100% { 
    width: 55ch; 
  }
}
</style>