<template>
  <div class="nation">
    {{ nation.name }}

    <h3>Players</h3>

    <div class="filters">
      <select name="color" id="color" v-model="filter.quality">
        <option value="-">Pick Quality</option>
        <option value="bronze">Bronze</option>
        <option value="silver">Silver</option>
        <option value="gold">Gold</option>
        <option value="inform">In form</option>
        <option value="special">Special</option>
      </select>
    </div>

    <player-card-list :data="players"></player-card-list>
  </div>
</template>

<script>
  import { NATIONS_API_URL, PLAYERS_API_URL } from '../../utils/constants'
  import PlayerCardList from '../players/CardList.vue'

  export default {
    name: 'NationsDetail',
    components: {
      PlayerCardList
    },
    data () {
      return {
        basePlayersUrl: `${PLAYERS_API_URL}?nation=${this.$route.params.id}`,
        filter: {
          quality: '-'
        },
        loading: false,
        nation: {},
        players: []
      }
    },

    mounted () {
      this.loading = true

      this.$http.get(`${NATIONS_API_URL}${this.$route.params.id}/`).then((response) => {
        this.nation = response.json()

        this.$http.get(this.basePlayersUrl).then((response) => {
          this.players = response.json().results

          this.loading = false
        })
      })
    },

    watch: {
      'filter.quality' (val, oldVal) {
        this.filterPlayers()
      }
    },

    methods: {
      filterPlayers () {
        this.loading = true

        const params = {
          quality: this.filter.quality
        }

        this.$http.get(this.basePlayersUrl, { params }).then((response) => {
          this.players = response.json().results

          this.loading = false
        })
      }
    }
  }
</script>
