import _ from 'lodash'

export default {
  data () {
    return {
      apiUrl: undefined,
      objects: {
        base: [], // These are the objects attained by page request and/or pagination
        filtered: [] // These are objects attained by filtering
      },
      loading: false, // Track whether we need to hide certain DOM elements
      pages: {
        next: null, // Pagination => Next page
        prev: null, // Pagination => Previous page
        current: 1, // Pagination => Current page
        total: null // Pagination => Total pages
      },
      order: '',
      orderDefault: '',
      orderOptions: [],
      searchQuery: '', // The search query
      searchQueryThrottling: false // Are we in the search throttle
    }
  },

  computed: {
    filtered () {
      return this.searchQuery.length
    },

    items () {
      /**
       * If we have filtered objects and a current searchQuery return the filtered items, else fall
       * back to the objects we had before filtering
       */
      if (this.filtered && this.objects.filtered.length > 0) {
        return this.objects.filtered
      } else {
        return this.objects.base
      }
    }
  },

  watch: {
    order () {
      this.orderItems()
    },

    searchQuery () {
      /**
       * Grab items from the API that match our search
       */
      this.searchItems(this.apiUrl)
    }
  },

  methods: {
    assignData (data) {
      /**
       * Assign the data we receive from the API to our component, if the data being sent is based
       * on a search we need to assign the items to a different key
       */
      /* eslint-disable camelcase, no-undef */
      const {
        next, prev, current, total, results,
        order_options: orderOptions,
        default_order_by: orderByDefault
      } = data
      /* eslint-enable */

      const key = this.filtered ? 'filtered' : 'base'
      Object.assign(this.objects, { [key]: results })
      Object.assign(this.pages, { next, prev, current, total })
      Object.assign(this, { orderOptions, orderDefault: orderByDefault })

      this.loading = false
    },

    fetchData (url = this.apiUrl) {
      /**
       * Grab our data from the API
       */
      this.loading = true

      const options = {
        params: {
          order: this.order,
          query: this.searchQuery
        }
      }

      this.$http.get(url, options).then((response) => {
        this.assignData(response.json())
      })
    },

    paginate (direction) {
      /**
       * Grab data from our API based on the next / previous page
       */
      if (this.pages[ direction ] === null) return

      this.fetchData(this.pages[ direction ])
    },
    nextPage () {
      /**
       * Stub method, mainly so we can use a method with no arguments
       */
      this.paginate('next')
    },
    prevPage () {
      /**
       * Stub method, mainly so we can use a method with no arguments
       */
      this.paginate('prev')
    },

    orderItems () {
      /* eslint-disable no-undef */
      this.fetchData(this.apiUrl)
      /* eslint-enable */
    },

    searchItems: _.throttle(function () {
      /**
       * API call based on our search, throttled to prevent excess calls to the backend
       */
      /* eslint-disable no-undef */
      this.fetchData(this.apiUrl)
      /* eslint-enable */
    }, 300)
  },

  filters: {
    capFirstNormalize (val) {
      let string = val
      string = string.charAt(0).toUpperCase() + string.slice(1)
      string = string.replace('_', ' ')

      return string
    }
  }
}
