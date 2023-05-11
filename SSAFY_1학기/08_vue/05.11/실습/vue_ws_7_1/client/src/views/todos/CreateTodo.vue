<template>
  <div>
    <input 
      type="text" 
      v-model.trim="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    createTodo: function () {
      const title = this.title
      if(!title) {
        alert('할일을 작성해주세요')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/todos/`,
        data: { title }
      })
      .then((res) => {
        console.log(res)
        this.$router.push({name: "TodoList"})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
