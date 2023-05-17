<template>
  <div>
    <b-card :title="article.title">
      <b-card-text>
        {{article.content}}
      </b-card-text>

      <b-card-text>작성자: {{article.author.username}}</b-card-text>
      <hr>
      <b-card-text>{{article.updated_at}}</b-card-text>

    </b-card>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  }
}
</script>

<style>

</style>
