import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  // 로컬스토리지 저장
  plugins: [createPersistedState()],
  state: {
    // 식별자
    watchId: 1,
    watchList: [
    ]
  },
  getters: {
  },
  mutations: {
    ADD_WATCH_MOVIE(state,movie) {
      state.watchList.push({id:state.watchId, title:movie, is_watched:false})
      // 1씩 증가후 식별자 부여
      state.watchId += 1
    },
    WATCH_COMPLETED(state,watch) {
      state.watchList = state.watchList.map((e) => {
        if (e.id === watch.id) {
          e.is_watched = !e.is_watched
        }
        return e
      })
    }
  },
  actions: {
    addWatchMovie(context,movie) {
      context.commit('ADD_WATCH_MOVIE',movie)
    },
    watchCompleted(context,watch) {
      context.commit('WATCH_COMPLETED',watch)
    }
  },
  modules: {
  }
})
