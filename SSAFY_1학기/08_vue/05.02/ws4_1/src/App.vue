<template>
  <div class="container" id="app">
    
    <h1>버튼 박스 제작</h1>
    <h2>예약 페이지</h2>
    <h3>시간 선택</h3>
    
    <span v-for="(time, index) in times" :key="index">
      <br v-if="index % 8 === 0">
      <button class="btn m-1" :class="{ 'btn-primary': !selectedTimes.includes(time), 'btn-secondary': selectedTimes.includes(time) }" @click="select(index)">{{time}}</button>
    </span>

    <hr>

    <h3>선택 시간: <span v-for="(time, index) in selectedTimes" :key="index">{{time}} </span></h3>

  </div>
</template>

<script>
export default {
  name: 'App',
  data(){
    const times = [
      "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
      "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
      "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
    ]
    return {
      times : times,
      cnt: 0,
      selectedTimes: [],
    }
  },
  methods: {
    select(index) {
      if (this.selectedTimes.includes(this.times[index])){
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
