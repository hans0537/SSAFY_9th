<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h1>UserName</h1>
    <input type="text" v-model="user.name">
    <h1>Email</h1>
    <input type="text" v-model="user.email">
    <button @click="movePage">이동</button>
  </div>
</template>

<script>
export default {
  name: "AboutView",
  data() {
    return {
      user: {
        name: "",
        email: ""
      }
    }
  },
  methods: {
    movePage() {
      this.$router.push({
        name: "hello",
        params: {user: this.user}
      })
    }
  }
}
</script>
