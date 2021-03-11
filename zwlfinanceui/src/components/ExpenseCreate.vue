<template>
    <div class ="create-expense">
        <h1>ZWL - Create Expense</h1>
        
        <form v-on:submit.prevent="onSubmit">
            <div>
                <label for="timestamp">Timestamp: </label>
                <input type="datetime-local" id="timestamp" v-model="timestamp" required />
            </div>
            <div>
                <label for="amount">Amount: </label>
                <input type="number" id="amount" v-model="amount" required min="0.00" step="0.01" inputmode="decimal" />
            </div>
            <div>
                <label for="payee">Payee</label>
                <input type="text" id="payee" v-model="payee" required />
            </div>
            <div>
                <label for="description">Description</label>
                <textarea id="description" v-model="description" rows="3"></textarea>
            </div>
            <div>
                <input type="radio" id="unverified" value="Unverified" v-model="status" />
                <label for="unverified">Unverified</label>
                <br>
                <input type="radio" id="verified" value="Verified" v-model="status" />
                <label for="verified">Verified</label>
            </div>

            <input type="submit"/>
        </form>
    </div>
</template>

<script>
export default {
    name: 'ExpenseCreate',
    data: function() {
        return {
            timestamp: null,
            amount: 0,
            payee: null,
            description: null,
            tagNames: [],
            status: "Unverified",
        }
    },
    methods: {
        onSubmit: function() {
            const Cookies = require('js-cookie');

            const data = {
                timestamp: this.timestamp,
                amount: this.amount,
                payee: this.payee,
                description: this.description,
                tag_names: this.tagNames,
                status: this.status,
            }

            const axios = require('axios');
            axios
                .post('/expense/api/expenses/', data, {headers: {
                    'X-CSRFTOKEN': Cookies.get('csrftoken')
                }})
                .then(this.$emit('expense-created'))
                .catch(error => {
                    if (error.response.status == 403) {
                        this.$store.dispatch('logout');
                    }
                })
        }
    },
    mounted: function() {
        const axios = require('axios');
        axios.get('/expense/api/set-csrf');
    }
}
</script>
