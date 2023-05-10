<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <button @click="goHome">HOME</button>
    <a href="" class="router-link-exact-active router-link-active">HOME HOME</a>
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link :to="{ name: 'happeed' }">Start</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  methods: {
    goHome() {
      this.$router.push({ name: "home" }).catch((err) => {
        console.log(err);
        this.$router.go(0);
      });
    },
  },
};
</script>

<style>
#app {
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 700px;
}

nav {
}

nav a {
}

nav a.router-link-exact-active {
}
</style>
