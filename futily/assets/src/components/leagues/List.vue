<template>
  <div class="leagues detail" :class="{ 'loading': loading }">
    <hr>

    <div class="pagination">
      <button type="button" @click="paginate('prev')" :disabled="!pages.prev">Prev</button>
      <button type="button" @click="paginate('next')" :disabled="!pages.next">Next</button>
    </div>
    
    <hr>

    <div v-for="league in leagues">
      <a v-link="{ name: 'leagues:detail', params: { id: league.slug } }">{{ league.name }}</a>
    </div>
  </div>
</template>

<script>
  import ListMixin from '../../mixins/List'

  export default {
    mixins: [ListMixin],

    data () {
      return {
        app: 'leagues',
        leagues: []
      }
    },

    route: {
      data () {
        this.$http.get('/api/leagues').then((response) => {
          this.assignData(response.json(), this.app)
        })
      }
    }
  }
</script>
