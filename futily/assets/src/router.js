import Vue from 'vue'
import Router from 'vue-router'

import Hello from './components/Hello.vue'
import Hello2 from './components/Hello2.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', component: Hello },
    { path: '/foo', component: Hello2 }
  ]
})
