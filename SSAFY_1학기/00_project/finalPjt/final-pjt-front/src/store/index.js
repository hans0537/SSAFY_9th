import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

Vue.use(Vuex)

// const persistedState = createPersistedState({
//   storage: window.localStorage,
//   reducer: state => ({
//     user: state.user,
//     accessToken: state.accessToken
//   })
// })

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    articles: [],
    accessToken: null,
    latestList: [],
    upcomingList: [],
    popularMovie: [],
    allmovie: [],
    user: null,
    selectedmovie:null,
    recommendmovie:[],
    dataload:false,
    // 로컬용
    API_URL: 'http://127.0.0.1:8000',
    // 서버용
    // API_URL: 'https://ithubproject.com',
  },
  getters: {
    isLogin(state) {
      return state.accessToken ? true : false
    }
  },
  mutations: {
    setRecommendMovies(state, movies) {
      state.recommendmovie = movies;
    },
    GET_LATEST(state, latest) {
      state.latestList = latest
    },

    GET_UPCOMING(state, upcoming) {
      state.upcomingList = upcoming
    },
    GET_POPULAR(state, popular) {
      state.popularMovie = popular
    },

    GET_ALL(state, allmovie) {
      state.allmovie = allmovie
    },


    GET_ARTICLES(state, articles) {
      state.articles = articles
    },

    SEARCH_ARTICLES(state, articles) {
      state.articles = articles
    },

    SAVE_SIGNUP_TOKEN(state, access) {
      state.accessToken = access
      
      this.dispatch('getuser');

      setTimeout(() => {
        router.push({name: 'home'})
      }, 1000);
    },
    SAVE_LOGIN_TOKEN(state, access) {
      state.accessToken = access
      alert("로그인 성공!!")
      this.dispatch('getuser');

      setTimeout(() => {
        const currentRoute = router.currentRoute;
        if(currentRoute.name == 'login' || currentRoute.name == 'signup') {
          router.push({ name: 'home' });
        }else {
          router.go(-1)
        }
      }, 1000);

    },
    GET_USER(state, user) {
      state.user = user
    },

    LOGOUT(state) {
      state.accessToken = null
      state.user = null
      alert('로그아웃 되셨습니다.')
      // 중복 routing 오류 방지
      const currentRoute = router.currentRoute;

      if (currentRoute.name != 'home') {
        router.push({ name: 'home' });
      }

    },
    setSelectedMovie(state,movie) {
      state.selectedmovie=movie
    },

  },
  actions: {
    login(context, access) {
      context.commit('SAVE_LOGIN_TOKEN', access)
    },
    signup(context, access) {
      context.commit('SAVE_SIGNUP_TOKEN', access)
    },
    logout(context) {
      context.commit('LOGOUT')
    },

    getuser(context) {
      // 로그인 되어있으면 그 사용자를 가져오고
      // 아니면 빈 로그인 객체를 생성
      if(context.state.accessToken) {
        axios({
          url: `${context.state.API_URL}/accounts/getUser/`,
          headers: {
            Authorization: `Bearer ${context.state.accessToken}`,
          }
        })
        .then((res) => {
          context.commit('GET_USER', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      } else {
        context.commit('GET_USER',  {username: '', id: 0})
      }
    },

    // 상영중인 최신 영화
    getLatest(context) {
      axios({
        method: 'get',
        url: `${context.state.API_URL}/movies/nowmovie/`,
      })
        .then(res => {
          context.commit('GET_LATEST', res.data)
        })
    },

    // 개봉 예정작
    getUpComing(context) {
      axios({
        method: 'get',
        url: `${context.state.API_URL}/movies/upcommovie/`,
      })
        .then(res => {
          context.commit('GET_UPCOMING', res.data)
        })
    },

    // 인기영화
    popularMovie(context) {
      axios({
        method: 'get',
        url: `${context.state.API_URL}/movies/popularmovie/`,
      })
        .then(res => {
          context.commit('GET_POPULAR', res.data)
        })
    },


    // 게시글 가져오기
    getArticles(context) {
      axios({
        method: 'get',
        url: `${context.state.API_URL}/articles/`,
      })
        .then((res) => {
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },

    // 검색 게시글 가져오기
    searchArticles(context, obj) {
      axios({
        method: 'get',
        url: `${context.state.API_URL}/articles/search/`,
        params: {
          'searchValue': obj.searchValue,
          'searchSelected': obj.searchSelected
        },
      })
      .then((res) => {
        // console.log(res.data, context)
        context.commit('SEARCH_ARTICLES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getall(context) {
      axios({
        method: 'get',
        url: `${context.state.API_URL}/movies/`,
      })
        .then(res => {
          context.commit('GET_ALL', res.data)
        })
    },

  },
  modules: {
  }
})
