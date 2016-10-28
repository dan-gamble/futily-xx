<template>
  <a :class="classNames" @dragstart="handleDragStart" @dragover.prevent="handleDragOver" @drop.stop="handleDrop" href="#">
    {{ Number(index) + 1 }} - {{ player.player.common_name }} {{ player.position }} - Chem: {{ overallChemistry }}
    <button type="button" @click="search">Search</button>
  </a>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import _ from 'lodash'

  import * as types from './types'

  export default {
    props: {
      player: {
        type: Object,
        required: true
      },
      index: {
        required: true
      }
    },

    data: () => ({
      classNames: ['player']
    }),

    computed: {
      ...mapGetters([
        'players'
      ]),

      overallChemistry () {
        const chemistry = Math.round(this.player.chemistry.links * this.player.chemistry.position)

        return Math.min(10, chemistry + this.player.chemistry.boost)
      }
    },

    methods: {
      ...mapActions({
        'updatePlayer': types.UPDATE_PLAYERS_PLAYER
      }),

      handleDragStart (e) {
        e.dataTransfer.effectAllowed = 'copy' // only dropEffect='copy' will be dropable
        e.dataTransfer.setData('SrcIndex', this.index) // required otherwise doesn't work
        console.log('start', e)
      },

      handleDragOver (e) {
        return false
      },

      handleDrop (e) {
        const dropeeIndex = e.dataTransfer.getData('SrcIndex')
        const dropeePlayer = this.players[dropeeIndex].player
        const currentPlayer = this.player.player

        this.classNames.push('droppedOn')

        this.updatePlayer({ player: dropeePlayer, index: this.index })
        this.updatePlayer({ player: currentPlayer, index: dropeeIndex })
      },

      search () {
        this.$emit('activate-search', this.index)
      }
    }
  }
</script>

<style scoped>
  .player {
    display: block;
    height: 50px;

    background-color: red;
    cursor: move;
  }

  button {
    display: inline-block;

    background-color: #fff;
    border: 1px solid #dedede;
  }
</style>
