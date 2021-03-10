<template>
    <div class ="welcome">
        <h1>ZWL - Expense</h1>

        <ExpenseCreate v-on:expense-created="refreshExpenses" />
        <ExpenseList v-bind:expenses="expenses" />
        <BasePagination v-bind:hasPrevious="hasPrevious" v-bind:hasNext="hasNext" v-bind:currentPage="currentPage" v-on:goto="changePage" />
    </div>
</template>

<script>
import ExpenseCreate from './ExpenseCreate.vue'
import ExpenseList from './ExpenseList.vue'
import BasePagination from './BasePagination.vue'

export default {
    name: 'Expense',
    components: {
        ExpenseCreate,
        ExpenseList,
        BasePagination,
    },
    data: function() {
        return {
            expenses: null,
            currentPage: 1,
            hasPrevious: false,
            hasNext: false,
        } 
    },
    methods: {
        changePage: function(newPage) {
            this.currentPage = newPage;
            this.refreshExpenses();
        },
        refreshExpenses: function() {
            const axios = require('axios');
            axios
                .get(`/expense/api/expenses/?format=json&page=${this.currentPage}`)
                .then(response => {
                    this.expenses = response.data.results;
                    this.hasPrevious = response.data.previous !== null;
                    this.hasNext = response.data.next !== null;
                })
                .catch(error => {
                    if (error.response.status == 403) {
                        this.$store.dispatch("logout");
                    }
                })
        }
    },
    mounted: function() {
        this.refreshExpenses();
    },
}
</script>
