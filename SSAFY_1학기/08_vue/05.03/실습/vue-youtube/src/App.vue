<template>
  <div id="app">
    <div class="container">
      <div class="d-flex justify-content-center">
        <h1 class="mt-3">SSAFY TUBE</h1>
      </div>
      <div class="mt-3" v-if="isSelectedVideo">
        <div>
          <h4>
            {{videoTitle}}
          </h4>
        </div>
        <div class="ratio">
          <iframe :src="videoSrc" frameborder="0" style="height: 500px"></iframe>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import _ from "lodash"

const URL = "https://www.googleapis.com/youtube/v3/search"
const API_KEY = "AIzaSyBJNMqfSCoTBI63Q8Bp-8Ai9O1vAkjraIE"

export default {
  name: 'App',
  data() {
    return {
      videos: [],
      selectedVideo: [],
    }
  },
  computed: {
    videoSrc() {
      return `http://www.youtube.com/embed/${this.selectedVideo.id.videoId}`
    },
    videoTitle() {
      return _.unescape(this.selectedVideo.snippet.title)
    },
    isSelectedVideo() {
      if (this.selectedVideo){
        return true
      }else{
        return false
      }
    },
  },
  created() {
    axios.get(URL, {
      params: {
        key: API_KEY,
        type: 'video',
        part: "snippet",
        q: "코딩노래"
      }
    }).then(res => {
      console.log(res.data)
      this.videos = res.data.items
      this.selectedVideo = this.videos[0]
    })
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
