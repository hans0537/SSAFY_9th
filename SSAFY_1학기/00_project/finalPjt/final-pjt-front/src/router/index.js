import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import MovieView from '../views/MovieView.vue'
import CommunityView from '../views/CommunityView.vue'
import MyPageView from '../views/MyPageView.vue'
import ArticlesView from '@/components/CommunityComponents/ArticlesView'
import ChoQuizView from '@/components/CommunityComponents/ChoQuizView'
import OverQuizView from '@/components/CommunityComponents/OverQuizView'
import WorldcupView from '@/components/CommunityComponents/WorldcupView'
import ArticleCreateView from '@/components/CommunityComponents/ArticleCreateView'
import ArticleDetailView from '@/components/CommunityComponents/ArticleDetailView'


import store from '../store/index'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView,
    children: [
      {
        path: '/community/articles',
        name: 'articles',
        component: ArticlesView
      },
      {
        path: '/community/articles/create',
        name: 'articlesCreate',
        component: ArticleCreateView
      },
      {
        path: '/community/articles/:id',
        name: 'articleDetail',
        component: ArticleDetailView,
      },
      {
        path: '/community/choquiz',
        name: 'choquiz',
        component: ChoQuizView
      },
      {
        path: '/community/overquiz',
        name: 'overquiz',
        component: OverQuizView
      },
      {
        path: '/community/worldcup',
        name: 'worldcup',
        component: WorldcupView
      },
    ]
  },

  {
    path: '/mypage',
    name: 'mypage',
    component: MyPageView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  // 로그인 여부
  const isLoggedIn = store.getters.isLogin

  // 로그인이 필요한 페이지 지정
  const authPages = ['articlesCreate', 'choquiz', 'overquiz', 'worldcup', 'mypage']
  
  // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
  const isAuthRequired = authPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('해당 서비스는 로그인후에 이용 가능합니다')
    next({ name: 'login'})
  } else {
    next()
  }
})

export default router
