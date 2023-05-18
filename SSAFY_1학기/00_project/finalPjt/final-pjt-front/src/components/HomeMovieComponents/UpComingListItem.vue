<template>
  <div class="col-md-3 col-6">
    <div class="trend_2im clearfix position-relative">
        <div class="trend_2im1 clearfix">
        <div class="grid">
            <figure class="effect-jazz mb-0">
            <a href="#"><img :src="imgSrc" class="w-100" alt="img25"></a>
            </figure>
        </div>
        </div>
        <div class="trend_2im2 clearfix text-center position-absolute w-100 top-0">
        <span class="fs-1"><a class="col_red" href="#"><i class="fa"></i></a></span>
        </div>
    </div>
    <div class="trend_2ilast bg_grey p-3 clearfix" style="height:250px;">
        <h5><a class="col_red" href="#">{{movie.title}}</a></h5>
        <p class="mb-2">{{overview}}</p>
        <span class="col_red">
        <i class="fa fa-star"></i>
        <i class="fa fa-star"></i>
        <i class="fa fa-star"></i>
        <i class="fa fa-star"></i>
        <i class="fa fa-star"></i>
        </span>
        <p class="mb-0">1 Views</p>
    </div>  
  </div>
</template>

<script>
export default {
  name: 'UpComingListItem',
  props: {
    movie: Object,
  },
  data(){
    return {
      imgSrc: "https://image.tmdb.org/t/p/w500" + this.movie.poster_path,
      overview: this.movie.overview.slice(0,20) + "..."
    }
  },
}
</script>

<style>

</style>