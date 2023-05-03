<template>
  <div>
    <h2>여기는 child2</h2>
  </div>

</template>

<script>
import EventBus from "@/EventBus"

export default {
    name: "ChildComponent2",
    methods: {

    },
    created() {
        console.log("C2 CREATED")
        EventBus.$on("fromC1", (message) => {
            alert(`C1에서 온 메세지: ${message}`)
        })
    },
    mounted() {
        console.log("C2 MOUNTED")
    },
}
</script>

<style>

</style>