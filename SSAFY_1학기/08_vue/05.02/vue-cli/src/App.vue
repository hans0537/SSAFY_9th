<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <MyComponent /> <!-- 사용한다 -->
    <MyComponent /> <!-- 사용한다 -->
    <HelloWorld msg="반가워 vue... 잘해보자 만반잘부"/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <button class="btn btn-primary">bootstrap</button>
    <hr>
    <MovieComponent title="범죄도시3" description="마동석" />
    <MovieComponent title="아바타" description="투르크막뚜르" />

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import MyComponent from './components/MyComponent.vue' // 1. 불러온다
// import MyComponent from '@/components/MyComponent' 
import MovieComponent from "@/components/MovieComponent.vue"

export default {
  name: 'App',
  components: {
    HelloWorld,
    MyComponent,  // 2. 등록한다
    MovieComponent,
  }
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
