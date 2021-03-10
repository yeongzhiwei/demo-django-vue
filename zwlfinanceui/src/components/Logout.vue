<template>
  <div></div>
</template>

<script>
export default {
  name: "Logout",
  mounted: function () {
    this.$store.dispatch("logout");
    this.$router.push({ name: "welcome" });
  },
};
</script>
