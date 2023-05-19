<template>
<div class="container">
  <div class="row">
    <div class="col">
      <div class="card">
        <div class="card-body d-flex justify-content-between">
          <b-form-select v-model="numSelected" :options="numOptions" class="form-select" style="width: 100px"></b-form-select>
          <form>
            <div class="form-group mb-0">
              <div class="input-group mb-0 d-flex align-items-center">
                <b-form-select v-model="searchSelected" :options="searchOptions" class="me-1 form-select" style="width: 40px; border-radius: 4px;"></b-form-select>
                <input type="text" class="form-control" placeholder="검색" aria-describedby="project-search-addon" />
                <div class="input-group-append">
                    <button class="btn btn-danger ms-1" type="button" id="project-search-addon"><i class="fa fa-search search-icon font-12"></i></button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <!-- end row -->
  <div class="row">
      <div class="col-lg-12">
          <div class="card">
              <div class="card-body">
                  <div class="table-responsive project-list">
                      <table class="table project-table table-centered table-nowrap">
                          <thead>
                              <tr>
                                  <th scope="col">#</th>
                                  <th scope="col">제목</th>
                                  <th scope="col">작성일</th>
                                  <th scope="col">작성자</th>
                                  <th scope="col">좋아요</th>
                                  <th scope="col">조회수</th>
                                  <th scope="col">삭제</th>
                              </tr>
                          </thead>
                          <tbody>
                            <ArticlesListView v-for="(article, index) in articles" :key="article.id" :article="article" :index="index"/>
                          </tbody>
                      </table>
                  </div>
                  <!-- end project-list -->

                <div class="pt-3 d-flex justify-content-center">
                  <ul class="pagination mb-0">
                      <li class="page-item disabled">
                          <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
                      </li>
                      <li class="page-item"><a class="page-link" href="#">1</a></li>
                      <li class="page-item active"><a class="page-link" href="#">2</a></li>
                      <li class="page-item"><a class="page-link" href="#">3</a></li>
                      <li class="page-item">
                          <a class="page-link" href="#">Next</a>
                      </li>
                  </ul>
                </div>
                <router-link :to="{ name: 'articlesCreate' }" class="btn btn-primary float-end" style="position: relative; top: -36px">글작성</router-link>
              </div>
          </div>
      </div>
  </div>
  <!-- end row -->
</div>
</template>

<script scoped>
import ArticlesListView from '@/components/CommunityComponents/ArticlesListView.vue'

export default {
  name: 'ArticlesView',
  components: {
    ArticlesListView
  },
  data() {
    return {
      numSelected: 10,
      numOptions: [
        { value: 10, text: '10개씩' },
        { value: 15, text: '15개씩' },
        { value: 20, text: '20개씩' },
        { value: 25, text: '25개씩' },
        { value: 30, text: '30개씩' }
      ],

      searchSelected: "title",
      searchOptions: [
        { value: "title", text: '제목' },
        { value: "content", text: '내용' },
        { value: "user", text: '작성자' },
      ],
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
  mounted() {
    this.getArticles()
  },
  methods: {
    getArticles(){
      this.$store.dispatch('getArticles')
    }
  }
}
</script>

<style scoped>
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