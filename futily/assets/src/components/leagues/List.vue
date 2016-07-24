<template>
  <div class="leagues">
    <hr>

    <div v-for="league in leagues">
      <a v-link="{ name: 'leagues:detail', params: { id: league.slug } }">{{ league.name }}</a>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        leagues: [],
        pages: {
          next: '',
          prev: ''
        }
      }
    },

    route: {
      data () {
        this.$http.get('/api/leagues').then((response) => {
          this.leagues = response.data.results
          this.pages.next = response.data.next
          this.pages.prev = response.data.prev
        })
      }
    }
  }
</script>
