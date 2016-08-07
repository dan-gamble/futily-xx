import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App.vue'
import { router } from './routes'

Vue.use(VueResource)

const app = new Vue({
  router,
  ...App
})

app.$mount('#app')
