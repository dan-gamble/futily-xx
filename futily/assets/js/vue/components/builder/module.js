import _ from 'lodash'

import * as types from './types'
import { goodChem, weakChem } from './utils/chemPosition'
import positionLinks from './utils/positionLinks'
import positionMap from './utils/positionMap'
import { FORMATIONS, LEGENDS_LEAGUE_ID } from './utils/constants'

const state = {
  // Object order isn't guaranteed so we'll store them as nested arrays
  formations: Object.keys(FORMATIONS).sort().map((formation) => {
    return [ formation, FORMATIONS[ formation ] ]
  }),

  name: '',
  hasPlayers: false,
  selectedFormation: '352',
  searchTerm: '',

  // Averages
  chem: 0,
  ovr: 0,
  pac: 0,
  sho: 0,
  pas: 0,
  dri: 0,
  def: 0,
  phy: 0,

  // Prices
  xbox: 0,
  playstation: 0,
  pc: 0,

  filledPlayers: [],

  // Players
  players: {
    0: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    1: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    2: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    3: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    4: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    5: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    6: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    7: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    8: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    9: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    10: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    }
  }
}

const mutations = {
  [types.UPDATE_HAS_PLAYERS] (state, { bool }) {
    state.hasPlayers = bool
  },

  [types.UPDATE_FORMATION] (state, { formation }) {
    state.selectedFormation = formation
  },

  [types.UPDATE_PLAYERS_POSITIONS] (state, { formation }) {
    const positions = positionMap[ formation ]

    for (const player in state.players) {
      state.players[ player ].position = positions[ player ]
    }
  },

  [types.UPDATE_PLAYERS_LINKS] (state, { formation }) {
    const links = positionLinks[ formation ]

    for (const player in state.players) {
      state.players[ player ].links = links[ player ]
    }
  },

  [types.UPDATE_PLAYER_PLAYER] (state, { player, index }) {
    state.players[ index ].player = player
    state.filledPlayers = _.xor(state.filledPlayers, [ index ]).map(index => Number(index))
  },

  [types.UPDATE_PLAYER_FILLED] (state, { index, filled }) {
    state.players[ index ].filledLinks = filled
  },

  [types.UPDATE_PLAYER_CHEMISTRY] (state, { index }) {
    const player = state.players[ index ]

    // Position
    const positionChemSchema = {
      strong: 3,
      good: 2.5,
      weak: 1.5,
      poor: 0.5
    }
    const playerPosition = player.player.position

    if (playerPosition === player.position) {
      player.chemistry.position = positionChemSchema.strong
    } else if (goodChem[ player.position ].includes(playerPosition)) {
      player.chemistry.position = positionChemSchema.good
    } else if (weakChem[ player.position ].includes(playerPosition)) {
      player.chemistry.position = positionChemSchema.weak
    } else {
      player.chemistry.position = positionChemSchema.poor
    }

    // Links
    const playerLinks = player.filledLinks
    const strength = {}
    let chemClub = 0
    let chemLeague = 0
    let chemNation = 0

    for (const index of playerLinks) {
      const linkedPlayer = state.players[ index ]
      let chem = 0

      if (player.player.club === linkedPlayer.player.club) {
        chem++
        chemClub++
      }

      if (player.player.league === linkedPlayer.player.league ||
        [ player.player.league, linkedPlayer.player.league ].includes(LEGENDS_LEAGUE_ID)) {
        chem++
        chemLeague++
      }

      if (player.player.nation === linkedPlayer.player.nation) {
        chem++
        chemNation++
      }

      strength[ index ] = chem
    }

    chemClub = playerLinks.length && (chemClub / playerLinks.length * 3)
    chemLeague = playerLinks.length && (chemLeague / playerLinks.length * 3)
    chemNation = playerLinks.length && (chemNation / playerLinks.length * 3)

    const chemTotal = chemClub + chemLeague + chemNation

    if (chemTotal >= 5) {
      player.chemistry.links = 3.5
    } else if (chemTotal >= 3) {
      player.chemistry.links = 3
    } else if (chemTotal >= 1) {
      player.chemistry.links = 2
    } else {
      player.chemistry.links = 0.9
    }

    // Bonus
    // TODO: This is hardcoded for now
    const manager = 0
    const loyalty = 0
    player.chemistry.boost = manager + loyalty
  }
}

const actions = {
  [types.UPDATE_FORMATION] ({ commit, state }) {
    commit(types.UPDATE_FORMATION, { formation: state.selectedFormation })
    commit(types.UPDATE_PLAYERS_POSITIONS, { formation: state.selectedFormation })
    commit(types.UPDATE_PLAYERS_LINKS, { formation: state.selectedFormation })
  },

  [types.UPDATE_PLAYER_PLAYER] ({ commit, state }, { player, index }) {
    console.time()
    commit(types.UPDATE_PLAYER_PLAYER, { player, index })

    const filledPlayers = linkedPlayers(state, index)
    commit(types.UPDATE_PLAYER_FILLED, { index, filled: filledPlayers })

    commit(types.UPDATE_PLAYER_CHEMISTRY, { index })

    for (const index of filledPlayers) {
      commit(types.UPDATE_PLAYER_FILLED, { index, filled: linkedPlayers(state, index) })
      commit(types.UPDATE_PLAYER_CHEMISTRY, { index })
    }
    console.timeEnd()
  }
}

const getters = {
  builder (state) {
    return state
  },

  players (state) {
    return state.players
  },

  selectedFormation (state) {
    return state.selectedFormation
  }
}

export default {
  state,
  mutations,
  actions,
  getters
}

function linkedPlayers (state, index) {
  const playerObj = state.players[ index ]

  return playerObj.links.filter(index => state.filledPlayers.includes(index))
}
