import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [
    ],
    access: null,
  },
  getters: {
    isLogin(state) {
      return state.access ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SAVE_ACCESS_TOKEN(state, access) {
      state.access = access
      router.push({name: 'home'})
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/articles/',
        headers: {
          Authorization: `Bearer ${context.state.access}`
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
    login(context, access) {
      context.commit('SAVE_ACCESS_TOKEN', access)
    },
    signup(context, access){
      context.commit('SAVE_ACCESS_TOKEN', access)
    },
  },
  modules: {
  }
})
