<template>
    <div class="row row-cols-1 row-cols-md-3 g-4 card-group">
        <MovieCard
        v-for="movie in movies" :key="movie.id"
        :movie="movie"
        />
    </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import axios from 'axios'

export default {
    name: 'MovieView',
    components: {MovieCard},
    data() {
        return {
            movies : null
        }
    },
    methods: {
        getTopMovies() {
            axios({
                method: 'get',
                url: `https://api.themoviedb.org/3/movie/top_rated?api_key=${process.env.VUE_APP_MOVIE_API_KEY}&language=ko-kr`
            })
            .then((res) => {
                console.log(res)
                this.movies = res.data.results
            })
            .catch((err) => {
                console.log(err)
            })
        }
    },
    created() {
        this.getTopMovies()
    }
}
</script>

<style>

</style>