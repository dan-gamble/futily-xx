<template>
  <div class="league">
    {{ league.name }}
  </div>
</template>

<script>
  export default {
    name: 'LeaguesDetail',
    data () {
      return {
        league: {}
      }
    },

    mounted () {
      this.$http.get(`/api/leagues/${this.$route.params.id}`).then((response) => {
        this.league = response.json()
      })
    }
  }
</script>
