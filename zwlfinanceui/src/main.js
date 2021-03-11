import Vue from 'vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'

import App from './App.vue'
import Welcome from './components/Welcome.vue'
import ExpenseMain from './components/ExpenseMain.vue'
import ExpenseCreate from './components/ExpenseCreate.vue'
import ExpenseList from './components/ExpenseList.vue'
import ExpenseDetail from './components/ExpenseDetail.vue'
import AuthLogin from './components/AuthLogin.vue'
import AuthLogout from './components/AuthLogout.vue'

Vue.config.productionTip = false
Vue.use(Vuex)
Vue.use(VueRouter)

const store = new Vuex.Store({
  state: {
    isLoggedIn: false,
    expenses: null,
    expenseCurrentPage: 1,
    expenseHasPrevious: false,
    expenseHasNext: false,
  },
  mutations: {
    initIsLoggedIn(state) {
      if (localStorage.getItem('isLoggedIn')) {
        state.isLoggedIn = true;
      }
    },
    setLoggedIn(state, isLoggedIn) {
      localStorage.setItem('isLoggedIn', isLoggedIn);
      state.isLoggedIn = isLoggedIn;
    },
    setExpenses(state, expenseData) {
      state.expenses = expenseData.data.results;
      state.hasPrevious = expenseData.data.previous !== null;
      state.hasNext = expenseData.data.next !== null;
    }
  },
  actions: {
    login(context) {
      context.commit('setLoggedIn', true);
    },
    logout(context) {
      context.commit('setLoggedIn', false);
    },
    setExpenses(context, expenseData) {
      context.commit('setExpenses', expenseData);
    }
  }
})

const router = new VueRouter({
  mode: 'history',
  base: '/vue',
  routes: [
    { path: '/', name: 'welcome', components: { public: Welcome }},
    { path: '/expense', name: 'expense', components: { content: ExpenseMain },
      children: [
        { path: 'create', component: ExpenseCreate },
        { path: 'list', component: ExpenseList },
        { path: 'detail/:id', component: ExpenseDetail },
      ]},
    { path: '/login', name: 'login', components: { public: AuthLogin }},
    { path: '/logout', name: 'logout', components: { public: AuthLogout }},
  ]
})

new Vue({
  el: '#app',
  render: h => h(App),
  store,
  router,
  beforeCreate: function() {
    this.$store.commit('initIsLoggedIn');
  }
})
