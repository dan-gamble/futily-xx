<template>
  <div class="players detail" :class="{ 'loading': loading }">
    <hr>

    <div class="pagination">
      <button type="button" @click="paginate('prev')" :disabled="!pages.prev">Prev</button>
      <button type="button" @click="paginate('next')" :disabled="!pages.next">Next</button>
    </div>

    <hr>

    <div v-for="player in players">
      <a v-link="{ name: 'players:detail', params: { id: player.slug } }">{{ player.common_name }} ({{ player.overall_rating }})</a>
    </div>
  </div>
</template>

<script>
  import ListMixin from '../../mixins/List'

  export default {
    mixins: [ListMixin],

    data () {
      return {
        app: 'players',
        players: []
      }
    },

    route: {
      data () {
        this.$http.get('/api/players').then((response) => {
          this.assignData(response.json(), this.app)
        })
      }
    }
  }
</script>
