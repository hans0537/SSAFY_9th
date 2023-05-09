<template>
  <div>
    <ul>
      <li>
        <router-link to="/">모든</router-link>
      </li>
      <li>
        <router-link to="/today">오늘</router-link>
      </li>
      <li>
        <router-link to="/important">중요</router-link>
      </li>
    </ul>
  </div>

</template>

<script>

export default {
  name: "SideBar",

}
</script>

<style>

</style>