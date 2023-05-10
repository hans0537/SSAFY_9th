<template>
  <li class="d-flex justify-content-bw order-item">
    <div class="d-flex">
      <img class="menu-img" :src="order.menu.image" alt="" />
      <div
        class="d-flex flex-column justify-content-center"
        style="margin-left: 10px"
      >
        <p>{{ order.menu.title }}</p>
        <p>사이즈: {{ order.size.name }}</p>
      </div>
    </div>
    <div class="d-flex flex-column justify-content-center">
      <div>가격: {{ totalPrice }}원</div>
      <div>
        |
        <span v-for="option in order.optionList" :key="option.title"
          >{{ option.title }} {{ option.count }}회 |
        </span>
      </div>
    </div>
  </li>
</template>

<script>
export default {
  name: "OrderListItem",
  props: {
    order: Object,
  },
  computed: {
    totalPrice() {
      return (
        this.order.menu.price +
        this.order.size.price +
        this.order.optionList.reduce((sum, option) => {
          if (option.count > 0) {
            sum += option.count * option.price;
          }
          return sum;
        }, 0)
      );
    },
  },
};
</script>

<style>
.order-item {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid gray;
}

.flex-column {
  flex-direction: column;
}
</style>