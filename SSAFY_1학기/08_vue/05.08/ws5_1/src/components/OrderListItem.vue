<template>
  <li class="d-flex justify-content-bw order-item">
    <div class="d-flex">
      <img :src="order.menu.image" class="menu-img" alt="">
      <div class="d-flex flex-column">
        <p>{{ order.menu.title }}</p>
        <p>사이즈 : {{ order.size.name }}</p>
      </div>
    </div>
    <div>가격: {{ totalPrice }} 
      <br>
     {{order.options[0].type}} {{order.options[0].count}}회 | 
     {{order.options[1].type}} {{order.options[1].count}}회 | 
     {{order.options[2].type}} {{order.options[2].count}}회</div>
  </li>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    totalPrice: function () {
      console.log(this.order)
      return this.order.menu.price + this.order.size.price 
      + this.order.options[0].price * this.order.options[0].count
      + this.order.options[1].price * this.order.options[1].count
      + this.order.options[2].price * this.order.options[2].count
    },
  },
}
</script>

<style>
.order-item {
  padding: 10px;
}

.flex-column {
  flex-direction: column;
}
</style>