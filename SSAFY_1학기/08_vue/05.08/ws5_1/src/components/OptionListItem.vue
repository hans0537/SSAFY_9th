<template>
  <div class="menu-item d-flex justify-content-bw">
    <p class="size-item d-flex align-items-center justify-content-center">{{ option.type }}</p>
    <div class="size-item d-flex align-items-center">
      <button class="btn" @click="decrease">-</button>
      {{ option.count }}
      <button class="btn" @click="increase">+</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      this.$store.dispatch("increaseCount", this.option)
    },
    decrease() {
      this.$store.dispatch("decreaseCount", this.option)
    },
  },
}
</script>

<style>
.btn {
  background: none;
  border-radius: 100%;
  width: 20px;
}
</style>