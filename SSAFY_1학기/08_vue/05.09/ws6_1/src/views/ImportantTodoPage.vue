<template>
  <div>
    <h1>중요 할일</h1>
    <div v-for="todo in importTodo" :key="todo.id">
        <button>체크</button>
        {{todo.content}}
        <button>중요</button>
    </div>
  </div>
</template>

<script>
export default {
    name: 'ImportantTodoPage',
    data() {
        return {}
    },
    computed:{
        importTodo() {
            const todoList = this.$store.state.todo.list

            const importList = todoList.filter((todo) => {
                if (!todo.isCompleted && todo.isImportant){
                    return todo
                }
            })
            return importList
        }
    },
}
</script>

<style>

</style>