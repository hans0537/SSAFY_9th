<template>
  <b-container class="article-list">
    <ArticleListItem 
    v-for="article in articles" :key="article.id" :article="article"
    />
  </b-container>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>
