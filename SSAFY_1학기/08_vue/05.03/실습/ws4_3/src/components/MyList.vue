<template>
  <div class="consultation-status">

    <h2>상담 신청 현황</h2>
    <h3>상담 선생님</h3>
    <p>성함: {{obj.selectedTeacher}}</p>

    <div class="line"></div>
    <h3>예약 현황</h3>
    <p>시간들: <span v-for="(time, index) in obj.selectedTimes" :key="index">{{time}} </span></p>
    
    <div class="line"></div>

    <img src="../assets/ssafy-logo.png" alt="logo">

  </div>
</template>

<script>
export default {
    name: "MyList",
    props: {
        obj: Object,
    },
}
</script>

<style>
.consultation-status {
  width: 450px;
  border: 1px solid black;
  background-color: #658dc63d;
}
</style>