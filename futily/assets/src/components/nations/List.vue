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
          this.nations = response.data.results
          this.pages.next = response.data.next
          this.pages.prev = response.data.prev
        })
      }
    }
  }
</script>
