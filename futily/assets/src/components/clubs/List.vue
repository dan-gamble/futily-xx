<template>
  <div class="clubs detail" :class="{ 'loading': loading }">
    <hr>

    <div class="pagination">
      <button type="button" @click="paginate('prev')" :disabled="!pages.prev">Prev</button>
      <button type="button" @click="paginate('next')" :disabled="!pages.next">Next</button>
    </div>

    <hr>

    <div v-for="club in clubs">
      <a v-link="{ name: 'clubs:detail', params: { id: club.slug } }">{{ club.name }}</a>
    </div>
  </div>
</template>

<script>
  import ListMixin from '../../mixins/List'

  export default {
    mixins: [ListMixin],

    data () {
      return {
        app: 'clubs',
        clubs: []
      }
    },

    route: {
      data () {
        this.$http.get('/api/clubs').then((response) => {
          this.assignData(response.json(), this.app)
        })
      }
    }
  }
</script>
