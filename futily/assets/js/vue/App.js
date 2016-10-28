import Vue from 'vue'
import VueDragula from 'vue-dragula'
import VueResource from 'vue-resource'

import components from './components'
import store from './store'

Vue.use(VueDragula)
Vue.use(VueResource)

export default {
  components,
  store,

  events: {
    overflowBody (val) {
      if (val) {
        document.body.style.overflow = 'hidden'
      } else {
        document.body.style.overflow = ''
      }
    }
  }
}
