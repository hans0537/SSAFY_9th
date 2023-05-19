import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'
const API_KEY = 'a719d72e722ce5b82da9a04d59337764'
const TMDB_URL = 'https://api.themoviedb.org/3'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [],
    accessToken: null,
    latestList: null,
    upcomingList: null,
    popularMovie:null,
  },
  getters: {
    isLogin(state) {
      return state.accessToken ? true : false
    }
  },
  mutations: {
    GET_LATEST(state, latest) {
      state.latestList = latest
    },

    GET_UPCOMING(state, upcoming) {
      state.upcomingList = upcoming
    },
    
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },

    SAVE_SIGNUP_TOKEN(state, access) {
      state.accessToken = access
      router.push({name: 'login'})
    },
    SAVE_LOGIN_TOKEN(state, access) {
      state.accessToken = access
      router.go(-1)
    },
    
    GET_POPULAR(state,popular) {
      state.popularMovie = popular
    },
    LOGOUT(state) {
      state.accessToken = null
    }
  },
  actions: {
    login(context, access) {
      context.commit('SAVE_LOGIN_TOKEN', access)
    },
    signup(context, access){
      context.commit('SAVE_SIGNUP_TOKEN', access)
    },
    logout(context){
      context.commit('LOGOUT')
    },

    // 상영중인 최신 영화
    getLatest(context) {
      axios({
        method: 'get',
        url: `${TMDB_URL}/movie/now_playing?language=ko-KR&api_key=${API_KEY}`,
      })
      .then((res) => {
        // console.log(res)
        context.commit('GET_LATEST', res.data.results)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    
    // 개봉 예정작
    getUpComing(context) {
      axios({
        method: 'get',
        url: `${TMDB_URL}/movie/upcoming?language=ko-KR&api_key=${API_KEY}`,
      })
      .then((res) => {
        context.commit('GET_UPCOMING', res.data.results)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    // 인기영화
    popularMovie(context) {
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/movies/',
      })
      .then(res =>{
        context.commit('GET_POPULAR',res.data)
      })
    },

    // 게시글 가져오기
    getArticles(context) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/articles/',
        headers: {
          Authorization: `Bearer ${context.state.accessToken}`
        }
      })
      .then((res) => {
        console.log(res.data, context)
        context.commit('GET_ARTICLES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  modules: {
  }
})
