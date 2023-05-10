<template>
  <div class="menu-list">
    <h1>3. 옵션을 고르세요.</h1>
    <ul class="option-list">
      <option-list-item
        v-for="option in optionList"
        :key="option.title"
        :option="option"
      ></option-list-item>
    </ul>
  </div>
</template>

<script>
import OptionListItem from "./OptionListItem.vue";
import { mapState } from "vuex";

export default {
  name: "OptionList",
  components: { OptionListItem },
  computed: {
    ...mapState({
      // 내가 쓰고 싶은 이름 : state 에서 가져올 상태(data) 이름
      optionList: (state) => state.optionList,
    }),
  },
  methods: {
    increase: function () {},
    decrease: function () {},
  },
};
</script>

<style>
</style>