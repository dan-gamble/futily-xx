import _ from 'lodash'

import * as types from './types'
import { goodChem, weakChem } from './utils/chemPosition'
import positionLinks from './utils/positionLinks'
import positionMap from './utils/positionMap'
import { FORMATIONS, POSITION_LINES, LEGENDS_LEAGUE_ID } from './utils/constants'

const state = {
  // Object order isn't guaranteed so we'll store them as nested arrays
  formations: Object.keys(FORMATIONS).sort().map((formation) => {
    return [ formation, FORMATIONS[ formation ] ]
  }),

  name: '',
  hasPlayers: false,
  selectedFormation: '352',
  searchTerm: '',

  // Prices
  xbox: 0,
  playstation: 0,
  pc: 0,

  filledPlayers: [],

  // Players
  players: [
    {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0,
        total: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0,
        total: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0,
        total: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0,
        total: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0,
        total: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0,
        total: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0,
        total: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0,
        total: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0,
        total: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0,
        total: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    },
    {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0,
        total: 0
      },
      player: {},
      position: '',
      links: [],
      filledLinks: []
    }
  ]
}

const mutations = {
  [types.UPDATE_HAS_PLAYERS] (state, { bool }) {
    state.hasPlayers = bool
  },

  [types.UPDATE_FORMATION] (state, { formation }) {
    state.selectedFormation = formation
  },

  [types.UPDATE_NAME] (state, { name }) {
    state.name = name
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
    } else if (goodChem.hasOwnProperty(player.position) &&
               goodChem[ player.position ].includes(playerPosition)) {
      player.chemistry.position = positionChemSchema.good
    } else if (weakChem.hasOwnProperty(player.position) &&
               weakChem[ player.position ].includes(playerPosition)) {
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

    const roundedChem = Math.round(player.chemistry.links * player.chemistry.position)
    player.chemistry.total = Math.min(10, roundedChem + player.chemistry.boost)
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
    console.log(player, index)
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
  averageRating: (state) => getAverage(state, 'rating', false),

  averageDef: (state) => getAverage(state, 'rating', false, POSITION_LINES.DEF),

  averageMid: (state) => getAverage(state, 'rating', false, POSITION_LINES.MID),

  averageAtt: (state) => getAverage(state, 'rating', false, POSITION_LINES.ATT),

  averagePace: (state) => getAverage(state, 'card_att_1', true),

  averageShooting: (state) => getAverage(state, 'card_att_2', true),

  averagePassing: (state) => getAverage(state, 'card_att_3', true),

  averageDribbling: (state) => getAverage(state, 'card_att_4', true),

  averageDefending: (state) => getAverage(state, 'card_att_5', true),

  averagePhysical: (state) => getAverage(state, 'card_att_6', true),

  builder (state) {
    return state
  },

  overallChem (state) {
    let total = 0

    for (const player in state.players) {
      total += state.players[player].chemistry.total
    }

    return total
  },

  players (state) {
    return state.players
  },

  selectedFormation (state) {
    return state.selectedFormation
  },

  starRating (state, getters) {
    if (getters.averageRating > 82) return '5'
    else if (getters.averageRating > 78) return '4.5'
    else if (getters.averageRating > 74) return '4'
    else if (getters.averageRating > 70) return '3.5'
    else if (getters.averageRating > 68) return '3'
    else if (getters.averageRating > 66) return '2.5'
    else if (getters.averageRating > 64) return '2'
    else if (getters.averageRating > 62) return '1.5'
    else if (getters.averageRating > 59) return '1'
    else if (getters.averageRating > 1) return '0.5'
    else return '0'
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

function filledPlayers (state, line = [], excludeGk = false) {
  const players = []

  for (const player in state.players) {
    if ((excludeGk && Number(player) === 0) ||
        (line.length && !line.includes(state.players[player].position))) continue

    if (!_.isEmpty(state.players[player].player)) players.push(state.players[player])
  }

  return players
}

function getAverage (state, attribute, excludeGk, line) {
  const players = filledPlayers(state, line, excludeGk).map(player => player.player[attribute])

  return players.length ? Math.round(players.reduce((a, b) => a + b) / players.length) : 0
}
