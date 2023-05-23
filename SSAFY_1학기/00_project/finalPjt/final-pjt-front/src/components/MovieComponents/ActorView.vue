<template>
  <div class="col-md-2 col-6">
    <div class="trend_2im clearfix position-relative" @mouseover="showDetails = true" @mouseleave="showDetails = false">
      <div class="trend_2im1 clearfix">
        <div class="grid">
          <figure class="effect-jazz mb-0">
              <img :src="imgSrc" class="w-100 img-height" alt="img25" style="height: 200px;">
              <div class="image-details" v-if="showDetails" >
                <p class="mb-2">Name : {{ actor.name }}</p>
                <p class="mb-2">Character : {{ actor.character }}</p>
              </div>
          </figure>
        </div>
      </div>
      <div class="trend_2im2 clearfix text-center position-absolute w-100 top-0">
        <span class="fs-1">
          <a class="col_red" href="#"><i class="fa"></i></a>
        </span>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name:'ActorView',
  props: {
    actor: Object,
  },
  components: {

  },
  data() {
    return {
      imgSrc: this.actor.profile_path
        ? `https://image.tmdb.org/t/p/w500${this.actor.profile_path}`
        : require("../../assets/baseProfile.png"),
      showDetails: false,
      
    }
  },
  computed: {
  },
  methods: {
  },
  created() {
  }
}
</script>

<style>

</style>