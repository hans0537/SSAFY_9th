<template>
  <div class="reservation-page">

    <h2>예약 페이지</h2>
    <h3>선생님 선택</h3>
    <button class="teacher-btn" :class="{ 'active': obj.selectedTeacher === 'Eric' }" @click="teacherSelect('Eric')">Eric</button>
    <button class="teacher-btn" :class="{ 'active': obj.selectedTeacher === 'Tony' }" @click="teacherSelect('Tony')">Tony</button>

    <div class="line"></div>
    <h3>시간 선택</h3>

    <span v-for="(time, index) in obj.times" :key="index">
        <br v-if="index % 6 === 0">
        <span class="times" :class="{ 'selected': obj.selectedTimes.includes(time) }" @click="select(index)">{{time}}</span>
    </span>

  </div>
</template>

<script>
export default {
    name: "TimeTable",
    props: {
        obj: Object,
    },
    methods: {
        teacherSelect(name) {
            this.$emit("teacher", name)
        },
        select(index) {
            this.$emit("select", index)
        }
    }
}
</script>

<style>
.reservation-page {
  width: 450px;
  border: 1px solid black;
}

.teacher-btn {
  border: 2px solid #0F4C81;
  background-color: transparent;
  color: #0F4C81;
  padding: 10px 20px;
  font-size: 15px;
  margin: 0 10px;
}

.teacher-btn:hover:not(.active) {
  cursor: pointer;
  background-color: #0F4C81;
  color: #fff;
}

.teacher-btn.active {
  cursor: pointer;
  background-color: #0F4C81;
  color: #fff;
}

.checked {
  color: #0f4c81;
  background-color: #658dc63d;
}

.times {
  margin: 10px;
}
.times:hover {
  cursor: pointer;
}

.selected {
  background-color: #658dc63d;
}
</style>
