<template>
    <div class ="expense-detail">
        <h1>ZWL - Expense Details</h1>
        <table>
            <tr>
                <th>Field</th>
                <th>Value</th>
            </tr>
            <tr>
                <th>Timestamp</th>
                <td>{{ expense.timestamp }}</td>
            </tr>
            <tr>
                <th>Amount</th>
                <td>{{ expense.amount }}</td>
            </tr>
            <tr>
                <th>Payee</th>
                <td>{{ expense.payee }}</td>
            </tr>
            <tr>
                <th>Description</th>
                <td>{{ expense.description }}</td>
            </tr>
            <tr>
                <th>Tags</th>
                <td>{{ expense.tagNames }}</td>
            </tr>
            <tr>
                <th>Status</th>
                <td>{{ expense.status }}</td>
            </tr>
        </table>
    </div>
</template>

<script>
export default {
    name: 'ExpenseDetail',
    props: {
        expenses: Array
    },
    computed: {
        expense: function() {
            return this.expenses.find(expense => expense.id == this.$route.params.id);
        }
    }
}
</script>

<style scoped>
table, th, td {
    border: 1px solid black;
}
</style>