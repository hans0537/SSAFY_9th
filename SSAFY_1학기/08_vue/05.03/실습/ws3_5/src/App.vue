<template>
  <div id="app">
    <div class="container">
      <h1>App</h1>
      <input type="text" v-model="appData">
      <p>parentData: {{parentData}}</p>
      <p>childData: {{childData}}</p>
    </div>
    <AppParent :app-data="appData" @parent-input="getParentData" @child-input="getChildData"/>
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  components: {
    AppParent
  },
  data() {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    getParentData(data) {
      this.parentData = data
    },
    getChildData(data) {
      this.childData = data
    }
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

.container {
  height: 500px;
  width: 500px;
  margin: 0 auto;
  border: 1px solid black;
  display: flex;
  justify-content: center;
}
</style>
