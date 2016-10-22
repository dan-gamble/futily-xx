import Vue from 'vue'
import Vuex from 'vuex'
import _ from 'lodash'

import modules from '../components/modules'
import * as builderTypes from '../components/builder/types'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

const store = new Vuex.Store({
  modules,
  strict: debug
})

store.watch(() => store.getters.selectedFormation, (val) => {
  // Make it call the action in builder/module
  store.dispatch(builderTypes.UPDATE_FORMATION, { formation: val })

  if (store.state.builder.hasPlayers) {
    const players = store.state.builder.players

    const filledPlayers = Object.keys(players).filter(index => {
      return !_.isEmpty(players[index].player)
    })

    for (const index of filledPlayers) {
      store.commit(builderTypes.UPDATE_PLAYER_CHEMISTRY, { index })
    }
  }
})

store.watch(() => store.getters.players, (val) => {
  /**
   * We want to know if the builder has players for when we change formation
   *
   * If we have players we'll need to recalculate chemistry
   */
  const hasPlayers = Object.keys(val).filter(index => {
    return !_.isEmpty(val[index].player)
  })

  store.commit(builderTypes.UPDATE_HAS_PLAYERS, { bool: Boolean(hasPlayers.length) })
}, {
  deep: true
})

export default store
