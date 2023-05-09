<template>
  <div>
    <h1>모든 할일</h1>
    <input type="text" v-model="newTodo" @keyup.enter="todoInput">
    <div v-for="todo in todoList" :key="todo.id">
        <button>체크</button>
        {{todo.content}}
        <button>중요</button>
    </div>
  </div>
</template>

<script>
export default {
    name: 'AllTodoPage',
    data() {
        return {
            newTodo: ''
        }
    },
    methods:{
        todoInput() {
            if(this.newTodo) {
                this.$store.dispatch('createTodo', this.newTodo)
                this.newTodo = ''
            }else {
                alert('todo를 입력하세요')
            }
        }
    },
    computed: {
        todoList() {
            return this.$store.state.todo.list
        }
    }

}
</script>

<style>

</style>