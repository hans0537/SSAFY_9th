<template>
  <div>
    <h1>Hello</h1>
    <h3>name : {{user.name}}</h3>
    <h3>email : {{user.email}}</h3>
    <button @click="back2">뒤로 2칸</button>
    <button @click="replacePage">페이지 교체</button>
  </div>
</template>

<script>
export default {
  name: "HelloView",
  data() {
    return {
        user: this.$route.params.user
    }
  },
  methods: {
    back2() {
      this.$router.go(-2)
    },
    replacePage(){
      this.$router.replace({name:'about'})
    }
  }
}
</script>

<style>

</style>