<template>
  <div class="menu-item d-flex justify-content-bw align-items-center">
    <div class="item d-flex align-items-center justify-content-center">
      {{ option.title }}
    </div>
    <div class="item d-flex align-items-center justify-content-cente">
      <div class="opt-btn" @click="decrease(option.title)">-</div>
      <div>{{ option.count }}</div>
      <div class="opt-btn" @click="increase(option.title)">+</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "OptionListItem",
  props: {
    option: Object,
  },
  methods: {
    increase(title) {
      this.$store.commit("increaseOption", title);
    },
    decrease(title) {
      this.$store.commit("decreaseOption", title);
    },
  },
};
</script>

<style>
.opt-btn {
  width: 30px;
  height: 30px;
  border: 1px solid black;
  border-radius: 15px;
  padding: 5px;
  margin-left: 15px;
  margin-right: 15px;
}

.opt-btn:hover {
  cursor: pointer;
  background-color: forestgreen;
  color: white;
}
</style>