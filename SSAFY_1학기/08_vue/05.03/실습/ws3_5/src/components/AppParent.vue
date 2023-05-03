<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" v-model="parentData" @keyup.enter="parentInput">
    <p>appData: {{appData}}</p>
    <p>childData: {{childData}}</p>
    <AppChild :app-data="appData" :parent-data="parentData" @child-input="getChildData"/>
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppChild',
  components: {
    AppChild,
  },
  props: {
    appData: String,
  },
  data: function() {
    return {
        parentData: "",
        childData: "",
    }
  },
  methods: {
    parentInput() {
        this.$emit('parent-input', this.parentData)
        this.$emit('child-input', this.childData)
    },
    getChildData(data) {
        this.childData = data
    }
  },
}

</script>

<style>
  .border {
    border: solid;
  }
</style>
