import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [
    ],
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    // SIGN_UP(state, token) {
    //   state.token = token
    // },

    // signup & login -> 완료되면 토큰 발급후 articleview 로 이동
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'ArticleView'}) // store/index.js $router 접근 불가 -> import 해야함
    },
    
  },
  actions: {
    getArticles(context) {
      const token = this.state.token
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
      })
        .then((res) => {
        // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },

    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
      .then((res) => {
        console.log(res)
        // context.commit('SIGN_UP', res.data.key)
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    login(context, payload) {
      const {username, password} = payload

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then((res) => {
        console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
