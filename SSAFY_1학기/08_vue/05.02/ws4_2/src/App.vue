<template>
  <div id="app">
    <h1>SSAFY 상담 예약 시스템</h1>

    <div class="wrapper">
      <div class="reservation-page">
        <h2>예약 페이지</h2>
        <h3>선생님 선택</h3>
        <button class="teacher-btn" :class="{ 'active': selectedTeacher === 'Eric' }" @click="teacherSelect('Eric')">Eric</button>
        <button class="teacher-btn" :class="{ 'active': selectedTeacher === 'Tony' }" @click="teacherSelect('Tony')">Tony</button>

        <div class="line"></div>
        <h3>시간 선택</h3>

        <span v-for="(time, index) in times" :key="index">
          <br v-if="index % 6 === 0">
          <span class="times" :class="{ 'selected': selectedTimes.includes(time) }" @click="select(index)">{{time}}</span>
        </span>

      </div>
      <div class="consultation-status">
        <h2>상담 신청 현황</h2>
        <h3>상담 선생님</h3>
        <p>성함: {{selectedTeacher}}</p>

        <div class="line"></div>
        <h3>예약 현황</h3>
        <p>시간들: <span v-for="(time, index) in selectedTimes" :key="index">{{time}} </span></p>
        
        <div class="line"></div>

        <img src="./assets/ssafy-logo.png" alt="logo">
      </div>
  </div>
  </div>
</template>

<script>


export default {
  name: 'App',
  data() {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30",
        "12:00","12:30","13:00","13:30","14:00","14:30",
        "15:00","15:30","16:00","16:30","17:00","17:30",
      ],
      cnt: 0,
      selectedTeacher: '',
      selectedTimes: [],
    }
  },
  methods: {
    teacherSelect(name) {
      if(this.selectedTeacher === name){
        this.selectedTeacher = ''
        this.selectedTimes = []
        this.cnt = 0
      }else if (this.selectedTeacher != name) {
        this.selectedTeacher=name        
        this.selectedTimes = []
        this.cnt = 0
      }else {
        this.selectedTeacher=name
      }
    },
    select(index) {
      if (this.selectedTeacher===''){
        alert('상담 선생님을 선택하세요')
      }else if (this.selectedTimes.includes(this.times[index])){
        this.cnt --
        this.selectedTimes.splice(this.selectedTimes.indexOf(this.times[index]),1)
      } else if (this.cnt === 5) {
        alert('5타임까지만 신청할 수 있습니다.')
      } else {
        this.cnt ++
        this.selectedTimes.push(this.times[index])
      }
    }
  }
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap");
#app {
  font-family: "Noto Sans KR", sans-serif;
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
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

.wrapper {
  display: flex;
  justify-content: space-between;
  width: 900px;
  margin: 0 auto;
}

.reservation-page {
  width: 450px;
  border: 1px solid black;
}

.consultation-status {
  width: 450px;
  border: 1px solid black;
  background-color: #658dc63d;
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

.line {
  margin: 20px auto;
  width: 80%;
  border: 0.5px solid #0F4C81;
}

img {
  margin: 30px 0;
}
</style>
