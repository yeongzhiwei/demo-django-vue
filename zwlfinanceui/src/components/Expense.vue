<template>
    <div class ="welcome">
        <h1>ZWL - Expense</h1>

        <CreateExpense v-on:expenseCreated="refreshExpenses" />
        <ExpenseList v-bind:expenses="expenses" />
        <Pagination v-bind:hasPrevious="hasPrevious" v-bind:hasNext="hasNext" v-bind:currentPage="currentPage" v-on:goto="changePage" />
    </div>
</template>

<script>
import ExpenseList from './ExpenseList.vue'
import CreateExpense from './CreateExpense.vue'
import Pagination from './Pagination.vue'

export default {
    name: 'Expense',
    components: {
        CreateExpense,
        ExpenseList,
        Pagination,
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
