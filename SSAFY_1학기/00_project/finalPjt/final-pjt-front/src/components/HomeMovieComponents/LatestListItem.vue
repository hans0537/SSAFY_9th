<template>
  <div class="col-md-3 col-6 mb-5">
    <div class="trend_2im clearfix position-relative" @mouseover="showDetails = true" @mouseleave="showDetails = false" @click="openDetail">
      <div class="trend_2im1 clearfix">
        <div class="grid">
          <figure class="effect-jazz mb-0">
            <a>
              <img :src="imgSrc" class="w-100 img-height" alt="img25">
              <div class="image-details" v-if="showDetails" >
                <h6 class="col_red">{{ movie?.title }}</h6>
                <p class="mb-2">{{ overview }}</p>
                <p>{{ movie?.vote_average }}</p>
                <span class="col_red">
                  <i v-for="index in 5" :key="index" class="fa" :class="['fa-star', index <= fullStarCount ? 'filled' : 'fa-regular', index === halfStarIndex ? 'fa-duotone fa-star-half-stroke' : '']" :style="index === halfStarIndex ? 'color: red' : ''"></i>
                </span>
                <p class="mb-0">{{ movie2?.review_count }} Views</p>
              </div>
            </a>
          </figure>
        </div>
      </div>
      <div class="trend_2im2 clearfix text-center position-absolute w-100 top-0">
        <span class="fs-1">
          <a class="col_red"><i class="fa"></i></a>
        </span>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'
export default {
  name: "LatestListItem",
  props: {
    movie: Object,
  },
  components: {
  },
  data() {
    return {
      API_URL: this.$store.state.API_URL,

      imgSrc: "https://image.tmdb.org/t/p/w500" + this.movie?.poster_path,
      overview: this.movie?.overview.slice(0, 20) + "...",
      showDetails: false,
      movie2:null,
    }
  },
  computed: {
    fullStarCount() {
      return Math.floor(this.movie?.vote_average / 2);
    },
    halfStarIndex() {
      return Math.ceil(this.movie?.vote_average / 2);
    },
  },
  methods: {
    openDetail() {
      this.$store.commit('setSelectedMovie', this.movie);

      this.$router.push({ name: 'moviedetail' });
    },
    getReviewcount() {
        axios({
          method: 'get',
          url: `${this.API_URL}/movies/${this.movie?.id}/`,
        })
        .then((res) => {
          this.movie2 = res.data
        })
        .catch((err) => {
          if (err.response && err.response.status === 404) {
            // 리뷰가 없는 경우
            this.movie2 = { review_count: 0 };
          } else {
            console.log(err);
          }
        });
      },
  },
  created() {
    this.getReviewcount()
  }
};
</script>

<style>
.img-height {
  height: 400px;
}

.image-details {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: white;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.image-details h6,
.image-details p,
.image-details span,
.image-details p {
  margin-bottom: 10px;
}

.trend_2im:hover .image-details {
  opacity: 1;
}

.fa-star {
  color: rgba(255, 255, 255);
  opacity:1;
}

.fa-star.filled {
  color: rgba(255, 0, 0);
}

.fa-regular {
  color: #ff0000
}

</style>