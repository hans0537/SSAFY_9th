<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name: 'CreateView' }">[CREATE]</router-link>
    <ArticleList />
    <hr>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      // 로그인이 되어 있으면 getArticles action 실행
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      }else {
        // 로그인 X 이면 login 페이지로 이동
        alert('로그인 하십시오')
        this.$router.push({name:'LogInView'})
      }
    }
  }
}
</script>

<style>

</style>
