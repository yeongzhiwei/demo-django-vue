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
                <th>{{ getTagNames(expense.tags) }} </th>
                <th>{{ expense.status}} </th>
                <th><a href="#" v-on:click.stop="$emit('click-id', expense.id)">link</a></th>
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
    methods: {
        getTagNames: function(tags) {
            return tags.map(tag => tag.name).join(', ')
        }
    }
}
</script>

<style scoped>
table, th, td {
    border: 1px solid black;
}
</style>