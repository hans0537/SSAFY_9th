<template>
  <div id="app">
    <h1>소득세 계산기</h1>
    <InCom/>
    <TaxRate/>
    <FinalTax/>
  </div>
</template>

<script>
import InCom from './components/InCom.vue'
import TaxRate from './components/TaxRate.vue'
import FinalTax from './components/FinalTax.vue'

export default {
  name: 'App',
  components: {
    InCom,
    TaxRate,
    FinalTax
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
