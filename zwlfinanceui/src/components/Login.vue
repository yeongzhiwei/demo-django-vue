<template>
  <div></div>
</template>

<script>
export default {
  name: "Login",
  mounted: function () {
    this.$store.dispatch("login");
    this.$router.push({ name: "welcome" });
  },
};
</script>
