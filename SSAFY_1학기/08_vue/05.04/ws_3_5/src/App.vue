<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <h1>APP</h1>
    <input type="text" v-model="appData" />
    <div>appData : {{ appData }}</div>
    <div>parentData : {{ parentData }}</div>
    <div>childData : {{ childData }}</div>
    <AppParent
      :app-data="appData"
      @parentChanged="parentChanged"
      @childChanged="childChanged"
    ></AppParent>
  </div>
</template>

<script>
import AppParent from "@/components/AppParent";

export default {
  name: "App",
  data() {
    return {
      appData: "",
      parentData: "",
      childData: "",
    };
  },
  methods: {
    parentChanged(parentData) {
      this.parentData = parentData;
    },
    childChanged(childData) {
      this.childData = childData;
    },
  },
  components: {
    AppParent,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  border: 1px solid black;
}
</style>
