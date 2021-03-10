<template>
    <div class ="welcome">
        <h1>ZWL - Expense</h1>

        <ExpenseCreate v-on:expense-created="refreshExpenses" />
        <ExpenseList v-bind:expenses="expenses" v-on:click-id="setCurrentExpenseId" />
        <BasePagination v-bind:hasPrevious="hasPrevious" v-bind:hasNext="hasNext" v-bind:currentPage="currentPage" v-on:goto="changePage" />
        <ExpenseDetail v-bind:expense="getCurrentExpense" />
    </div>
</template>

<script>
import ExpenseCreate from './ExpenseCreate.vue'
import ExpenseList from './ExpenseList.vue'
import ExpenseDetail from './ExpenseDetail.vue'
import BasePagination from './BasePagination.vue'

export default {
    name: 'Expense',
    components: {
        ExpenseCreate,
        ExpenseList,
        ExpenseDetail,
        BasePagination,
    },
    data: function() {
        return {
            expenses: null,
            currentPage: 1,
            hasPrevious: false,
            hasNext: false,
            currentExpenseId: null
        } 
    },
    computed: {
        getCurrentExpense: function() {
            return this.expenses.find(expense => expense.id === this.currentExpenseId)
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
        },
        setCurrentExpenseId: function(id) {
            this.currentExpenseId = id;
        },
    },
    mounted: function() {
        this.refreshExpenses();
    },
}
</script>
