<template>
  <div>
    <h3>This is child component</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>

    <button @click="childToParent">클릭!</button>

    <input type="text" v-model="childInputData" @keyup.enter="childInput">
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  data: function() {
    return {
      childInputData: null,
    }
  },
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  methods: {
    childToParent: function() {
      this.$emit('child-to-parent', 'child Data')
    },
    childInput() {
      this.$emit('child-input', this.childInputData)
      this.childInputData = ''
    }
  }
}
</script>

<style>
  
</style>
