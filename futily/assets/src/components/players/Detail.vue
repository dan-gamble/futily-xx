<template>
  <div class="player">
    {{ player.common_name }} ({{ player.overall_rating }})
    <img alt="" :src="player.image_sm">
    <img alt="" :src="player.image_md">
    <img alt="" :src="player.image_lg">
  </div>
</template>

<script>
  export default {
    data () {
      return {
        player: {}
      }
    },

    mounted () {
      this.$http.get(`/api/players/${this.$route.params.id}`).then((response) => {
        this.player = response.json()
      })
    }
  }
</script>
