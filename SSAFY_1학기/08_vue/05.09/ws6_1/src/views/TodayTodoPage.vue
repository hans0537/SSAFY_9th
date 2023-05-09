<template>
  <div>
    <h1>오늘 할일</h1>
    <div v-for="todo in todayTodo" :key="todo.id">
        <button>체크</button>
        {{todo.content}}
        <button>중요</button>
    </div>
  </div>
</template>

<script>
export default {
    name: 'TodayTodoPage',
    data() {
        return {

        }
    },
    computed:{
        todayTodo() {
            const today = new Date()
            const todoList = this.$store.state.todo.list

            const todayList = todoList.filter((todo) => {
                const dueDate = new Date(todo.dueDateTime);
                if (!todo.isCompleted && 
                    (dueDate.getFullYear() == today.getFullYear() && 
                    dueDate.getMonth() == today.getMonth() && 
                    dueDate.getDate() == today.getDate())){
                    return todo
                }
            })
            return todayList
        }
    },
}
</script>

<style>

</style>