<template>
  <div>
    <h1>Article</h1>
    <router-link :to="{ name: 'create' }">[CREATE]</router-link>
    <hr>
    <ArticleList />
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    ArticleList
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
      this.$store.dispatch('getArticles')
    }
  }
}
</script>

<style>

</style>