<template>
  <div>
    연봉 입력 (만원): <input type="number"  v-model.number="salary" @keyup.enter="salInput">
    세액감면액 (만원): <input type="number" v-model.number="discount" @keyup.enter="disInput">
    <hr>
    <h2>종합소득금액 : </h2>
    <h2>종합소득공제 : (-)</h2>
    <h2>과세표준 : </h2>
  </div>
</template>

<script>
export default {
  name: 'InCom',

}
</script>

<style>

</style>