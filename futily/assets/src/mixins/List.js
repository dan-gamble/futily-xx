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
      searchQuery: '', // The search query
      searchQueryThrottling: false // Are we in the search throttle
    }
  },

  computed: {
    items () {
      /**
       * If we have filtered objects and a current searchQuery return the filtered items, else fall
       * back to the objects we had before filtering
       */
      if (this.objects.filtered.length > 0 && this.searchQuery.length) {
        return this.objects.filtered
      } else {
        return this.objects.base
      }
    }
  },

  watch: {
    searchQuery () {
      /**
       * Grab items from the API that match our search
       */
      this.searchForItems(this.apiUrl)
    }
  },

  methods: {
    assignData (data, filtered = false) {
      /**
       * Assign the data we receive from the API to our component, if the data being sent is based
       * on a search we need to assign the items to a different key
       */
      const { next, prev, current, total, results } = data

      const key = filtered ? 'filtered' : 'base'
      Object.assign(this.objects, { [key]: results })
      Object.assign(this.pages, { next, prev, current, total })

      this.loading = false
    },

    fetchData (url) {
      /**
       * Grab our data from the API
       */
      this.loading = true

      this.$http.get(url).then((response) => {
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

    searchForItems: _.throttle(function () {
      /**
       * API call based on our search, throttled to prevent excess calls to the backend
       */
      this.$http.get(this.apiUrl, { params: { query: this.searchQuery } }).then((response) => {
        this.assignData(response.json(), true)
      })
    }, 300)
  }
}
