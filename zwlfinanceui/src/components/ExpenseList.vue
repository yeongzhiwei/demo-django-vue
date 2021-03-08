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
            </tr>
            <tr v-for="expense in expenses" :key="expense.id">
                <th>{{ expense.timestamp}} </th>
                <th>{{ expense.amount}} </th>
                <th>{{ expense.payee}} </th>
                <th>{{ expense.description}} </th>
                <th>{{ expense.tags}} </th>
                <th>{{ expense.status}} </th>
            </tr>
        </table>
    </div>
</template>

<script>
export default {
    name: 'ExpenseList',
    props: {
        expenses: Array
    },
}
</script>

<style scoped>
table, th, td {
    border: 1px solid black;
}
</style>