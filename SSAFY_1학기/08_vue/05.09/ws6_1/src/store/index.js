import Vue from 'vue'
import Vuex from 'vuex'
import todo from './modules/todo'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
    CREATE_TODO(state, todoObj) {
      state.todo.list.push(todoObj)
    }
  },
  actions: {
    createTodo(context, todo) {
      let nowDateObj = new Date()
      const id = nowDateObj.getTime()
      nowDateObj.setHours(0, 0, 0, 0);
      const duedatetime = `${nowDateObj.getFullYear()}-${(nowDateObj.getMonth() + 1).toString().padStart(2, '0')}-${nowDateObj.getDate().toString().padStart(2, '0')}T${nowDateObj.getHours().toString().padStart(2, '0')}:${nowDateObj.getMinutes().toString().padStart(2, '0')}`;
      
      const todoObj = {
        id: id,
        content: todo,
        dueDateTime: duedatetime,
        isCompleted: false,
        isImportant: false,
      }
      context.commit("CREATE_TODO", todoObj)

    }
  },
  modules: {
    todo
  }
})
