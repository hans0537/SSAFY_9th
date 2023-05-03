<template>
  <div>
    <button @click="getDogImage">멍멍아 이리온</button><br><br>
    <img v-if="imgSrc" :src="imgSrc" alt="#"><br>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name:'DogComponent',
  data() {
    return {
      imgSrc: null,
    }
  },
  methods:{
    getDogImage() {
      const dogImageSearchURL = 'https://dog.ceo/api/breeds/image/random'
      
      axios({
        method: 'get',
        url: dogImageSearchURL
      })
        .then((response) => {
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  // 페이지 열리자마자 실행되는 함수
  // 데이터 준비하는 시간
  created() {
    this.getDogImage()
    console.log('Dog created!')
    // const button = document.querySelector('button')
    // button.innerText = '멍멍!'
  },
  // 화면이 합쳐질때 실행 되는 함수
  // 따라서 버튼을 가져올 수 있는것
  mounted() {
    console.log('Dog mounted!')
    const button = document.querySelector('button')
    button.innerText = '멍멍!'
  },
  updated() {
    console.log('새로운 멍멍이!')
    console.log('Dog updated!')
  }
}
</script>

<style>

</style>
