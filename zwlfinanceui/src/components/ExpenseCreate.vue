<template>
  <v-container>
    <h1>ZWL - Create Expense</h1>

    <v-form v-on:submit.prevent="onSubmit">
      <v-row>
        <label for="timestamp">Timestamp: </label>
        <input
          type="datetime-local"
          id="timestamp"
          v-model="timestamp"
          required
        />
      </v-row>
      <v-row>
        <label for="amount">Amount: </label>
        <input
          type="number"
          id="amount"
          v-model="amount"
          required
          min="0.00"
          step="0.01"
          inputmode="decimal"
        />
      </v-row>
      <v-row>
        <label for="payee">Payee</label>
        <input type="text" id="payee" v-model="payee" required />
      </v-row>
      <v-row>
        <label for="description">Description</label>
        <textarea id="description" v-model="description" rows="3"></textarea>
      </v-row>
      <v-row>
        <input
          type="radio"
          id="unverified"
          value="Unverified"
          v-model="status"
        />
        <label for="unverified">Unverified</label>
        <br />
        <input type="radio" id="verified" value="Verified" v-model="status" />
        <label for="verified">Verified</label>
      </v-row>

      <input type="submit" />
    </v-form>
  </v-container>
</template>

<script>
export default {
  name: "ExpenseCreate",
  data: function () {
    return {
      timestamp: null,
      amount: 0,
      payee: null,
      description: null,
      tagNames: [],
      status: "Unverified",
    };
  },
  methods: {
    onSubmit: function () {
      const Cookies = require("js-cookie");

      const data = {
        timestamp: this.timestamp,
        amount: this.amount,
        payee: this.payee,
        description: this.description,
        tag_names: this.tagNames,
        status: this.status,
      };

      const axios = require("axios");
      axios
        .post("/expense/api/expenses/", data, {
          headers: {
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
          },
        })
        .then(this.$emit("expense-created"))
        .catch((error) => {
          if (error.response.status == 403) {
            this.$store.dispatch("logout");
          }
        });
    },
  },
  mounted: function () {
    const axios = require("axios");
    axios.get("/expense/api/set-csrf");
  },
};
</script>
