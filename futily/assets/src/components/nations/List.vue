<template>
  <div class="nations detail" :class="{ 'loading': loading }">
    <hr>

    <div class="pagination">
      <button type="button" @click="paginate('prev')" :disabled="!pages.prev">Prev</button>
      <button type="button" @click="paginate('next')" :disabled="!pages.next">Next</button>
    </div>

    <hr>

    <div v-for="nation in nations">
      <a v-link="{ name: 'nations:detail', params: { id: nation.slug } }">{{ nation.name }}</a>
    </div>
  </div>
</template>

<script>
  import ListMixin from '../../mixins/List'

  export default {
    mixins: [ListMixin],

    data () {
      return {
        app: 'nations',
        nations: []
      }
    },

    route: {
      data () {
        this.$http.get('/api/nations').then((response) => {
          this.assignData(response.json(), this.app)
        })
      }
    }
  }
</script>
