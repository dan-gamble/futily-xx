<template>
  <div class="league">
    {{ league.name }}
  </div>
</template>

<script>
  export default {
    data () {
      return {
        league: {}
      }
    },

    route: {
      data () {
        this.$http.get(`/api/leagues/${this.$route.params.id}`).then((response) => {
          this.league = response.json()
        })
      }
    }
  }
</script>
