<template>
  <div id="app">
    <img src="@/assets/스타벅스.png" alt="" />
    <h1 class="d-flex justify-content-center">Coffee Order App</h1>
    <div class="order-board d-flex justify-content-bw">
      <menu-list></menu-list>
      <size-list></size-list>
      <option-list></option-list>
    </div>
    <OrderList></OrderList>
  </div>
</template>

<script>
import MenuList from "@/components/MenuList.vue";
import SizeList from "@/components/SizeList.vue";
import OptionList from "@/components/OptionList.vue";
import OrderList from "@/components/OrderList.vue";

export default {
  name: "App",
  components: {
    MenuList,
    SizeList,
    OrderList,
    OptionList,
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  font-family: "Noto Sans KR", sans-serif;
  padding: 0;
  margin: 0;
}

#app {
  text-align: center;
  width: 1300px;
  margin: 0 auto;
}

ul {
  list-style: none;
}

.justify-content-center {
  justify-content: center;
}

.order-board {
  margin-top: 100px;
  background-color: lightgray;
  padding: 20px;
  border-radius: 10px;
}
</style>
