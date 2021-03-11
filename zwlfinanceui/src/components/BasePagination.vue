<template>
  <v-container>
    <v-pagination
      v-model="page"
      @input="$emit('on-page-change', $event)"
      :length="numberOfPages"
    ></v-pagination>
  </v-container>
</template>

<script>
export default {
  name: "BasePagination",
  props: {
    hasPrevious: Boolean,
    hasNext: Boolean,
    currentPage: Number,
    numberOfPages: Number,
  },
  data: function() {
    return {
      page: this.currentPage
    }
  },
};
</script>
