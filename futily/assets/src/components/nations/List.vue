<template>
  <div class="nations">
    <hr>

    <div v-for="nation in nations">
      <a v-link="{ name: 'nations:detail', params: { id: nation.slug } }">{{ nation.name }}</a>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        nations: [],
        pages: {
          next: '',
          prev: ''
        }
      }
    },

    route: {
      data () {
        this.$http.get('/api/nations').then((response) => {
          const res = response.json()

          this.nations = res.results
          this.pages.next = res.next
          this.pages.prev = res.prev
        })
      }
    }
  }
</script>
