import Vue from 'vue'
import Vuex from 'vuex'

// import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    access: null,
  },
  getters: {
    isLogin(state) {
      return state.access ? true : false
    }
  },
  mutations: {
    SAVE_ACCESS_TOKEN(state, access) {
      state.access = access
      router.push({name: 'home'})
    }
  },
  actions: {
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
