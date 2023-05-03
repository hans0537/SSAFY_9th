<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <ChildComponent name="임준환" @money="giveMoney"/>
    <ChildComponent2/>
    <MyComponent />

  </div>
</template>

<script>
import ChildComponent from './components/ChildComponent.vue'
import ChildComponent2 from './components/ChildComponent2.vue'
import MyComponent from '@/components/MyComponent'

export default {
  name: 'App',
  components: {
    MyComponent,
    ChildComponent,
    ChildComponent2,
  },
  methods: {
    giveMoney(money) {
      alert(`용돈 ${money}원`)
    }
  },
  created() {
    console.log("APP CREATED")
  },
  mounted() {
    console.log("APP MOUNTED")
  },

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
