<template>
  <div class="about">
    <h1>Cat Image</h1>
    <img v-if="catImg" :src="catImg" alt=""> <br>
    <button @click="uploadImg">Get Cat</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CatView',
  data() {
    return {
      catImg: '',
      resource: '',
    }
  },
  methods: {
    getCatImg() {
      const apiURL = 'https://api.thecatapi.com/v1/images/search'
      axios({
        method:'get',
        url: apiURL,
      })
      .then((response) => {
        this.resource = response.data[0]
      })
      .catch((error) => {
        console.log(error)
      })
    },
    uploadImg() {
      this.getCatImg()
      this.catImg = this.resource.url
    }
  },
  created(){
    this.getCatImg()
  },
  updated() {
    console.log(this.resource)
  }
}
</script>