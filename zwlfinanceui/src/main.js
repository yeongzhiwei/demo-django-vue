import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Welcome from './components/Welcome.vue'
import Expense from './components/Expense.vue'

Vue.config.productionTip = false
Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    { path: '/welcome', component: Welcome },
    { path: '/expense', component: Expense }
  ]
})

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
