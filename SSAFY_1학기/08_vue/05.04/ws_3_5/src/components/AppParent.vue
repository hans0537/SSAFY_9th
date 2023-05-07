<template>
  <div id="parent">
    <h1>AppParent</h1>
    <input type="text" v-model="parentData" @input="parentChanged" />
    <div>appData : {{ appData }}</div>
    <div>parentData : {{ parentData }}</div>
    <div>childData : {{ childData }}</div>
    <AppChild
      :app-data="appData"
      :parent-data="parentData"
      @childChanged="childChanged"
    ></AppChild>
  </div>
</template>

<script>
import AppChild from "@/components/AppChild";

export default {
  name: "AppParent",
  props: {
    appData: String,
  },
  data() {
    return {
      parentData: "",
      childData: "",
    };
  },
  methods: {
    parentChanged() {
      this.$emit("parentChanged", this.parentData);
    },
    childChanged(childData) {
      this.childData = childData;
      this.$emit("childChanged", childData);
    },
  },
  components: {
    AppChild,
  },
};
</script>

<style>
#parent {
  border: 1px solid red;
}
</style>