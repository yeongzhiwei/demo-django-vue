<template>
  <v-container>
    <h1>ZWL - Expense List</h1>

    <v-simple-table>
      <thead>
        <tr>
          <th>Timestamp</th>
          <th>Amount</th>
          <th>Payee</th>
          <th>Description</th>
          <th>Tags</th>
          <th>Status</th>
          <th>Detail</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="expense in expenses" :key="expense.id">
          <th>{{ expense.timestamp }}</th>
          <th>{{ expense.amount }}</th>
          <th>{{ expense.payee }}</th>
          <th>{{ expense.description }}</th>
          <th>{{ expense.tagNames }}</th>
          <th>{{ expense.status }}</th>
          <th>
            <router-link :to="'/expense/detail/' + expense.id">link</router-link>
          </th>
        </tr>
      </tbody>
    </v-simple-table>

    <BasePagination
      @on-page-change="changePage"
      :hasPrevious="hasPrevious"
      :hasNext="hasNext"
      :currentPage="currentPage"
      :numberOfPages="numberOfPages"
    />
  </v-container>
</template>

<script>
import BasePagination from "./BasePagination.vue";

export default {
  name: "ExpenseList",
  components: {
    BasePagination,
  },
  data() {
    return {
      headers: [
        { text: 'Timestamp', value: 'timestamp' },
        { text: 'Amount', value: 'amount' },
        { text: 'Payee', value: 'payee' },
        { text: 'Description', value: 'description' },
        { text: 'Tags', value: 'tagNames' },
        { text: 'Status', value: 'status' },
      ]
    }
  },
  props: {
    expenses: Array,
    hasPrevious: Boolean,
    hasNext: Boolean,
    currentPage: Number,
    numberOfPages: Number
  },
  methods: {
    changePage: function (newPage) {
      this.$emit("on-page-change", newPage);
    },
  },
};
</script>
