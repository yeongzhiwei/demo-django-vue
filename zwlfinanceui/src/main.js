import Vue from 'vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'

import App from './App.vue'
import Welcome from './components/Welcome.vue'
import ExpenseMain from './components/ExpenseMain.vue'
import AuthLogin from './components/AuthLogin.vue'
import AuthLogout from './components/AuthLogout.vue'

Vue.config.productionTip = false
Vue.use(Vuex)
Vue.use(VueRouter)

const store = new Vuex.Store({
  state: {
    isLoggedIn: false
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
    }
  },
  actions: {
    login(context) {
      context.commit('setLoggedIn', true);
    },
    logout(context) {
      context.commit('setLoggedIn', false);
    }
  }
})

const router = new VueRouter({
  mode: 'history',
  base: '/vue',
  routes: [
    { path: '/', name: 'welcome', components: { public: Welcome }},
    { path: '/expense', name: 'expense', components: { content: ExpenseMain }},
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
