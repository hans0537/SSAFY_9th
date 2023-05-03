<template>
  <div id="app">
    <h1>SSAFY 상담 예약 시스템</h1>
    <div class="wrapper">
      <TimeTable :obj="obj" @teacher="getTeacher" @select="timeSelect"/>
      <MyList :obj="obj"/>
    </div>
  </div>
</template>

<script>
import TimeTable from '@/components/TimeTable'
import MyList from '@/components/MyList'

export default {
  name: 'App',
  components: {
    TimeTable,
    MyList,
  },
  data() {
    return {
      obj: {
        times: [
        "09:00","09:30","10:00","10:30","11:00","11:30",
        "12:00","12:30","13:00","13:30","14:00","14:30",
        "15:00","15:30","16:00","16:30","17:00","17:30",
        ],
        cnt: 0,
        selectedTeacher: '',
        selectedTimes: [],
      }
    }
  },
  methods: {
    getTeacher(name){
      if(this.obj.selectedTeacher === name){
        this.obj.selectedTeacher = ''
        this.obj.selectedTimes = []
        this.obj.cnt = 0
      }else if (this.obj.selectedTeacher != name) {
        this.obj.selectedTeacher=name        
        this.obj.selectedTimes = []
        this.obj.cnt = 0
      }else {
        this.obj.selectedTeacher=name
      }
    },
    timeSelect(index){
      if (this.obj.selectedTeacher===''){
        alert('상담 선생님을 선택하세요')
      }else if (this.obj.selectedTimes.includes(this.obj.times[index])){
        this.obj.cnt --
        this.obj.selectedTimes.splice(this.obj.selectedTimes.indexOf(this.obj.times[index]),1)
      } else if (this.obj.cnt === 5) {
        alert('5타임까지만 신청할 수 있습니다.')
      } else {
        this.obj.cnt ++
        this.obj.selectedTimes.push(this.obj.times[index])
      }
    }
  }
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap");

#app {
  font-family: "Noto Sans KR", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.wrapper {
  display: flex;
  justify-content: space-between;
  width: 900px;
  margin: 0 auto;
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
