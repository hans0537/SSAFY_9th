<template>
  <div class="option-list">
    <h1>3. 옵션을 고르세요.</h1>
    <OptionListItem v-for="option in optionList" :key="option.type" :option="option" />
  </div>
</template>

<script>
import OptionListItem from '@/components/OptionListItem'

export default {
  name: 'OptionList',
  components: {
    OptionListItem,
  },
  computed: {
    optionList: function () {
      return this.$store.state.optionList
    },
  },
  methods: {
    // increase: function () {
    // },
    // decrease: function () {
    // },
  },
}
</script>

<style>
.option-list {
  padding: 20px;
  background-color: white;
  border-radius: 10px;
}
</style>