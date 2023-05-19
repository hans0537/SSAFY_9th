<template>
  <tr @click="articleDetail">
    <th scope="row">{{index + 1}}</th>
    <td>{{article?.title}}</td>
    <td>{{ formatDate(article?.created_at)}}</td>
    <td>
        <span class="text-success font-12"><i class="mdi mdi-checkbox-blank-circle mr-1"></i> {{article?.user}}</span>
    </td>
    <td>
        <div class="team">
            <a href="javascript: void(0);" class="team-member" data-toggle="tooltip" data-placement="top" title="" data-original-title="Roger Drake">
                <img src="https://bootdey.com/img/Content/avatar/avatar6.png" class="rounded-circle avatar-xs" alt="" />
            </a>

            <a href="javascript: void(0);" class="team-member" data-toggle="tooltip" data-placement="top" title="" data-original-title="Reggie James">
                <img src="https://bootdey.com/img/Content/avatar/avatar7.png" class="rounded-circle avatar-xs" alt="" />
            </a>

            <a href="javascript: void(0);" class="team-member" data-toggle="tooltip" data-placement="top" title="" data-original-title="Gerald Mayberry">
                <img src="https://bootdey.com/img/Content/avatar/avatar8.png" class="rounded-circle avatar-xs" alt="" />
            </a>
        </div>
    </td>
    <td>
      <p>{{article?.hit}}</p>
    </td>

    <td>
        <div class="action">
            <a href="#" class="text-success mr-4" data-toggle="tooltip" data-placement="top" title="" data-original-title="Edit"> <i class="fa fa-pencil h5 m-0"></i></a>
            <a href="#" class="text-danger" data-toggle="tooltip" data-placement="top" title="" data-original-title="Close"> <i class="fa fa-remove h5 m-0"></i></a>
        </div>
    </td>
  </tr>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ArticlesListView',
  props: {
    article: Object,
    index: Number,
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
        console.log(err)
      })
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