<template>
  <div>
    <h1>Article</h1>
    <router-link :to="{ name: 'create' }">[CREATE]</router-link>
  </div>
</template>

<script>
export default {
  name: 'ArticleView',
  data(){
    return {

    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles(){
      if(this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인 하십시오!')
        this.$router.push({name: 'login'})
      }
    }
  }
}
</script>

<style>

</style>