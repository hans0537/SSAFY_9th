<template>
    <div>
        <h1>AppChild</h1>
        <input type="text" v-model="childData" @keyup.enter="childInput">
        <p>appData: {{appData}}</p>
        <p>parentData: {{parentData}}</p>
        <p>childData: {{childData}}</p>
        <AppChild/>
    </div>
</template>

<script>
export default {
    name: "AppChild",
    data() {
        return {
            childData: ''
        }
    },
    props: {
        appData: String,
        parentData: String,
    },
    methods: {
        childInput() {
            this.$emit('child-input', this.childData)
        }
    },
}
</script>

<style>

</style>