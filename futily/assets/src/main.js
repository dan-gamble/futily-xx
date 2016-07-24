import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

import { configRouter } from './routes'

Vue.use(VueResource)
Vue.use(VueRouter)

/* eslint-disable no-new */
const router = new VueRouter({
  history: true,
  mode: 'html5',
  saveScrollPosition: true
})

configRouter(router)

const App = Vue.extend(require('./App.vue'))

router.start(App, '#app')

window.router = router
