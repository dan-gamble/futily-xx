<template>
  <div class="pagination">
    <button type="button" @click="prev" :disabled="!config.prev">Prev</button>
    {{ config.current }} / {{ config.total }}
    <button type="button" @click="next" :disabled="!config.next">Next</button>
  </div>
</template>

<script>
  import _ from 'lodash'

  const defaultConfig = {
    next: null,
    prev: null,
    current: 1,
    total: null
  }

  export default {
    name: 'Pagination',
    props: {
      config: {
        type: Object,
        validator (val) {
          return _.isEqual(Object.keys(defaultConfig), Object.keys(val))
        },
        required: true
      },
      next: {
        type: Function,
        required: true
      },
      prev: {
        type: Function,
        required: true
      },
      animation: {
        type: Boolean,
        default: false
      }
    }
  }
</script>
