<template>
  <div>
    <div>
      <input type="text" @change="updateName" :value="builder.name">

      <select @change="updateFormation" :value="builder.selectedFormation">
        <option v-for="formation in builder.formations"
                :value="formation[1]"
                :selected="builder.selectedFormation === formation[1]">{{ formation[0] }}</option>
      </select>

      <div>Chem: {{ overallChem }}</div>
      <div>Rating: {{ averageRating }}</div>
      <div>Pace: {{ averagePace }}</div>
      <div>Shooting: {{ averageShooting }}</div>
      <div>Passing: {{ averagePassing }}</div>
      <div>Dribbling: {{ averageDribbling }}</div>
      <div>Defending: {{ averageDefending }}</div>
      <div>Physical: {{ averagePhysical }}</div>
      <div>Def: {{ averageDef }}</div>
      <div>Mid: {{ averageMid }}</div>
      <div>Att: {{ averageAtt }}</div>
      <div>Stars: {{ starRating }}</div>
    </div>

      <player v-for="(player, index) in builder.players"
              :player="player"
              :index="index"
              @activate-search="activateSearch"></player>

    <input type="search"
           ref="search"
           v-if="search.show"
           v-model="search.term">

    <div v-for="player in search.results" @click="assignPlayer(player)">
      {{ player.common_name }}
    </div>
  </div>
</template>

<script>
  import buildUrl from 'build-url'
  import { mapActions, mapGetters, mapMutations } from 'vuex'

  import * as types from './types'
  import Player from './Player.vue'
  import { apiUrls } from '../../../config/urls'
  import Draggable from './Draggable'

  export default {
    components: {
      Draggable,
      Player
    },

    data: () => ({
      draggableOpts: {
        sort: false
      },
      search: {
        index: 0,
        results: [],
        term: '',
        show: false
      }
    }),

    computed: {
      ...mapGetters([
        'averageRating',
        'averageDef',
        'averageMid',
        'averageAtt',
        'averagePace',
        'averageShooting',
        'averagePassing',
        'averageDribbling',
        'averageDefending',
        'averagePhysical',
        'builder',
        'overallChem',
        'starRating'
      ])
    },

    created () {
      this.$store.dispatch(types.UPDATE_FORMATION, { formation: this.builder.selectedFormation })
    },

    watch: {
      'search.term' (val) {
        if (val.length > 2) {
          this.$http.get(buildUrl(apiUrls.players, { queryParams: { query: val } })).then((res) => {
            this.search.results = res.body.results
          })
        }
      }
    },

    methods: {
      ...mapActions({
        'updatePlayer': types.UPDATE_PLAYERS_PLAYER
      }),

      activateSearch (index) {
        this.search.index = index
        this.search.show = true

        this.$nextTick(() => this.$refs.search.focus())
      },

      assignPlayer (player) {
        const index = this.search.index

        this.updatePlayer({ player, index })

        this.search.index = null
        this.search.term = ''
        this.search.show = false
        this.search.results = []
      },

      onDragStart (evt) {
        console.log(this)
        console.log('start', evt)
      },

      onDragEnd (evt) {
        console.log(this)
        console.log('end', evt)
      },

      onDragUpdate (evt) {
        console.log('update', evt)
//        const { newIndex, oldIndex } = evt
//        const oldPlayer = this.builder.players[oldIndex]
//        const newPlayer = this.builder.players[newIndex]
//
//        this.updatePlayer({ player: newPlayer.player, index: oldIndex })
//        this.updatePlayer({ player: oldPlayer.player, index: newIndex })
      },

      updateFormation (e) {
        this.$store.commit(types.UPDATE_FORMATION, { formation: e.target.value })
      },

      updateName (e) {
        this.$store.commit(types.UPDATE_NAME, { name: e.target.value })
      }
    }
  }
</script>

<style scoped>
  input {
    background-color: #fff;
  }
</style>
