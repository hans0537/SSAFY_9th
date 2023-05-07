import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  // 상태 (데이터같은 느낌)
  state: {
    message: 'message in store'
  },
  getters: {
    messageLength(state) {
      return state.message.length
    },
    doubleLength(state, getters) {
      return getters.messageLength * 2
    }
  },
  // 상태를 직접적으로 접근하여 변경 
  mutations: {
    CHANGE_MESSAGE(state, payload) {
      // console.log(state)
      // console.log(message)
      state.message = payload
    }
  },
  // 상태 바꾸는거 이외의 동작
  // 상태를 바꾸려면 mutations을 호출 commit
  actions: {
    changeMessage(context, message) {
      context.commit('CHANGE_MESSAGE', message)
    }
  },
  modules: {
  }
})
