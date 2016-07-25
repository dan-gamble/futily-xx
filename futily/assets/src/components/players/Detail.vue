<template>
  <div class="player">
    {{ player.common_name }} ({{ player.overall_rating }})
  </div>
</template>

<script>
  export default {
    data () {
      return {
        player: {}
      }
    },

    route: {
      data () {
        this.$http.get(`/api/players/${this.$route.params.id}`).then((response) => {
          console.log(response, response.json())
          this.player = response.json()
        })
      }
    }
  }
</script>
