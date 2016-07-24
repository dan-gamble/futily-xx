import Vue from 'vue'
import Vuex from 'vuex'

import app from './modules/app'

Vue.use(Vuex)

export default new Vuex.Store({ // eslint-disable-line new-cap
  modules: {
    app
  }
})
