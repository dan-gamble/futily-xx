import Vue from 'vue'
import Vuex from 'vuex'

import app from './modules/app'

Vue.use(Vuex)

const store = new Vuex.Store({ // eslint-disable-line new-cap
  modules: {
    app
  }
})

export default store
