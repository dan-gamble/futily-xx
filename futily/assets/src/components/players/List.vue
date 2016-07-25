<template>
  <div class="players">
    <hr>

    <div v-for="player in players">
      <a v-link="{ name: 'players:detail', params: { id: player.slug } }">{{ player.common_name }} ({{ player.overall_rating }})</a>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        players: [],
        pages: {
          next: '',
          prev: ''
        }
      }
    },

    route: {
      data () {
        this.$http.get('/api/players.json').then((response) => {
          const res = response.json()

          this.players = res.results
          this.pages.next = res.next
          this.pages.prev = res.prev
        })
      }
    }
  }
</script>
