<template>
    <div class ="welcome">
        <h1>ZWL - Expense</h1>
        
        <router-view 
            @expense-created="expenseCreated"
            @change-page="changePage"
            :expenses="formattedExpenses"
            :currentPage="currentPage"
            :hasPrevious="hasPrevious"
            :hasNext="hasNext">
        </router-view>
    </div>
</template>

<script>
export default {
    name: 'Expense',
    data: function() {
        return {
            expenses: null,
            currentPage: 1,
            hasPrevious: false,
            hasNext: false,
        } 
    },
    computed: {
        formattedExpenses: function() {
            if (this.expenses) {
                return this.expenses.map(expense => {
                    expense.tagNames = expense.tags.map(tag => tag.name).join(', ');
                    return expense;
                })
            }
            return null;
        },
    },
    methods: {
        changePage: function(newPage) {
            this.currentPage = newPage;
            this.refreshExpenses();
        },
        expenseCreated: function() {
            this.refreshExpenses();
            this.$router.push('/expense/list');
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
    },
    mounted: function() {
        this.refreshExpenses();
    },
}
</script>
