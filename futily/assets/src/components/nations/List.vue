<template>
  <div class="nations detail" :class="{ 'loading': loading }">
    <hr>

    <div class="pagination">
      {{ pages.current }} / {{ pages.total }}
      <button type="button" @click="paginate('prev')" :disabled="!pages.prev">Prev</button>
      <button type="button" @click="paginate('next')" :disabled="!pages.next">Next</button>
    </div>

    <hr>

    <div v-for="nation in items">
      <router-link :to="{ name: 'nations:detail', params: { id: nation.slug } }">
        {{ nation.name }}
      </router-link>
    </div>
  </div>
</template>

<script>
  import ListMixin from '../../mixins/List'
  import { NATIONS_API_URL } from '../../utils/constants'

  export default {
    name: 'NationsList',
    mixins: [ListMixin],

    data () {
      return {
        app: 'nations',
        items: []
      }
    },

    created () {
      this.fetchData(NATIONS_API_URL)
    }
  }
</script>
