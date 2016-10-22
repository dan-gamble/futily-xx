<template>
  <div>
    <select @change="updateFormation" :value="builder.selectedFormation">
      <option v-for="formation in builder.formations"
              :value="formation[1]"
              :selected="builder.selectedFormation === formation[1]">{{ formation[0] }}</option>
    </select>

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
  import { mapActions, mapGetters, mapMutations } from 'vuex'
  import buildUrl from 'build-url'

  import * as types from './types'
  import Player from './Player.vue'
  import { apiUrls } from '../../../config/urls'

  export default {
    components: {
      Player
    },

    data: () => ({
      search: {
        index: 0,
        results: [],
        term: '',
        show: false
      }
    }),

    computed: {
      ...mapGetters([
        'builder'
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
        'updatePlayer': types.UPDATE_PLAYER_PLAYER
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

      updateFormation (e) {
        this.$store.commit(types.UPDATE_FORMATION, { formation: e.target.value })
      }
    }
  }
</script>

<style scoped>
  input {
    background-color: #fff;
  }
</style>
