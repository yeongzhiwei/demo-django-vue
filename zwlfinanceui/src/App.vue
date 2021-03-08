<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    
    <div id="topnavbar">
      <router-link to="/welcome">Welcome</router-link>&nbsp;
      <router-link to="/expense">Expense</router-link>
    </div>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
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
