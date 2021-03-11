<template>
    <div class ="expense-list">
        <h1>ZWL - Expense List</h1>
        
        <table>
            <tr>
                <th>Timestamp</th>
                <th>Amount</th>
                <th>Payee</th>
                <th>Description</th>
                <th>Tags</th>
                <th>Status</th>
                <th>Detail</th>
            </tr>
            <tr v-for="expense in expenses" :key="expense.id">
                <th>{{ expense.timestamp}} </th>
                <th>{{ expense.amount}} </th>
                <th>{{ expense.payee}} </th>
                <th>{{ expense.description}} </th>
                <th>{{ expense.tagNames }} </th>
                <th>{{ expense.status}} </th>
                <th><router-link :to='"/expense/detail/" + expense.id'>link</router-link></th>
            </tr>
        </table>
        
        <BasePagination 
            @goto="changePage"
            :hasPrevious="hasPrevious"
            :hasNext="hasNext"
            :currentPage="currentPage" />
    </div>
</template>

<script>
import BasePagination from './BasePagination.vue'

export default {
    name: 'ExpenseList',
    components: {
        BasePagination,
    },
    props: {
        expenses: Array,
        hasPrevious: Boolean,
        hasNext: Boolean,
        currentPage: Number
    },
    methods: {
        changePage: function(newPage) {
            this.$emit('change-page', newPage);
        }
    }
}
</script>

<style scoped>
table, th, td {
    border: 1px solid black;
}
</style>