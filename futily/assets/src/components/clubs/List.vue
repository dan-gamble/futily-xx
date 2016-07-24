<template>
  <div class="clubs">
    <hr>

    <div v-for="club in clubs">
      <a v-link="{ name: 'clubs:detail', params: { id: club.slug } }">{{ club.name }}</a>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        clubs: [],
        pages: {
          next: '',
          prev: ''
        }
      }
    },

    route: {
      data () {
        this.$http.get('/api/clubs').then((response) => {
          this.clubs = response.data.results
          this.pages.next = response.data.next
          this.pages.prev = response.data.prev
        })
      }
    }
  }
</script>
