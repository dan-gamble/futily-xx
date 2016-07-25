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
        this.$http.get('/api/leagues/').then((response) => {
          const res = response.json()

          this.leagues = res.results
          this.pages.next = res.next
          this.pages.prev = res.prev
        })
      }
    }
  }
</script>
