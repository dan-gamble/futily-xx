<template>
  <div class="player-cards">
    <router-link :to="{ name: 'players:detail', params: { id: player.slug } }"
                 v-for="player in data"
                 class="player-card">
      <h4>{{ player.common_name }} ({{ player.overall_rating }})</h4>
    </router-link>
  </div>
</template>

<script>
  export default {
    props: ['data']
  }
</script>

<style rel="stylesheet/scss" scoped>
  .player-cards {
    flex-wrap: wrap;
    justify-content: space-between;

    display: flex;
  }

  .player-card {
    width: 33.33%;
  }
</style>
