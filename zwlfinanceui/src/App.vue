<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">

    <div id="topnavbar">
      <router-link to="/">Home</router-link>&nbsp;

      <span v-if="this.$store.state.isLoggedIn">
        <router-link to="/expense">Expense</router-link>&nbsp;
        <a href="/accounts/logout/">Logout</a>
      </span>
      
      <span v-else>
        <router-link to="/login" v-slot="{ href }" custom>
          <a :href="'/accounts/login/?next=' + href">Login</a>
        </router-link>
      </span>
    </div>
    
    <div class="content">
      <router-view name="public"></router-view>
      <router-view name="content" v-if="this.$store.state.isLoggedIn"></router-view>
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
