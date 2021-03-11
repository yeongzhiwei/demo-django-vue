<template>
  <v-app>
    <v-app-bar app color="primary" dark>  
      <v-img
        alt="Vuetify Name"
        class="shrink mt-1 hidden-sm-and-down"
        contain
        min-width="100"
        src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
        width="100"
      />

      <v-spacer></v-spacer>

      <v-btn to="/">Home</v-btn>

      <template v-if="this.$store.state.isLoggedIn">
        <v-btn to="/expense/list" class="mx-2">Expense</v-btn>
        <v-btn to="/expense/create" class="mx-2">Create Expense</v-btn>
        <v-btn href="/accounts/logout/">Logout</v-btn>
      </template>

      <template v-else>
        <v-btn href="/accounts/login/?next=/vue/login">Login</v-btn>
      </template>
    </v-app-bar>

    <v-main>
      <router-view name="public"></router-view>
      <router-view
        name="content"
        v-if="this.$store.state.isLoggedIn"
      ></router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",
};
</script>
