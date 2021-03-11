<template>
  <v-container>
    <router-view
      @expense-created="expenseCreated"
      @on-page-change="changePage"
      :expenses="formattedExpenses"
      :currentPage="currentPage"
      :hasPrevious="hasPrevious"
      :hasNext="hasNext"
      :numberOfPages="numberOfPages"
    >
    </router-view>
  </v-container>
</template>

<script>
export default {
  name: "Expense",
  data: function () {
    return {
      expenses: null,
      currentPage: 1,
      hasPrevious: false,
      hasNext: false,
      numberOfPages: 1,
      pageSize: 10
    };
  },
  computed: {
    formattedExpenses: function () {
      if (this.expenses) {
        return this.expenses.map((expense) => {
          expense.tagNames = expense.tags.map((tag) => tag.name).join(", ");
          return expense;
        });
      }
      return null;
    },
  },
  methods: {
    changePage: function (newPage) {
      this.currentPage = newPage;
      this.refreshExpenses();
    },
    expenseCreated: function () {
      this.refreshExpenses();
      this.$router.push("/expense/list");
    },
    refreshExpenses: function () {
      const axios = require("axios");
      axios
        .get(`/expense/api/expenses/?format=json&page=${this.currentPage}&limit=${this.pageSize}`)
        .then((response) => {
          this.expenses = response.data.results;
          this.hasPrevious = response.data.previous !== null;
          this.hasNext = response.data.next !== null;
          this.numberOfPages = Math.ceil(response.data.count / this.pageSize);
        })
        .catch((error) => {
          if (error.response.status == 403) {
            this.$store.dispatch("logout");
          }
        });
    },
  },
  mounted: function () {
    this.refreshExpenses();
  },
};
</script>
