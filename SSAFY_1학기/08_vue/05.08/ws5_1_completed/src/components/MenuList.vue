<template>
  <div class="menu-list">
    <h1>1. 음료를 고르세요.</h1>
    <div class="menu-box">
      <menu-list-item
        v-for="menu in menuList"
        :key="menu.title"
        :menu="menu"
      ></menu-list-item>
    </div>
  </div>
</template>

<script>
import MenuListItem from "@/components/MenuListItem";

export default {
  name: "MenuList",
  components: {
    MenuListItem,
  },
  computed: {
    menuList() {
      return this.$store.state.menuList;
    },
  },
  methods: {
    selectMenu() {},
  },
};
</script>

<style>
.menu-list {
  width: 400px;
  padding: 20px;
  background-color: white;
  border-radius: 10px;
  margin-left: 10px;
  margin-right: 10px;
}
.menu-box {
  height: 220px;
  overflow-y: scroll;
}
</style>