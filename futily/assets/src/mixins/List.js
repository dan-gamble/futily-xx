export default {
  data () {
    return {
      app: '',
      loading: false,
      pages: {
        next: null,
        prev: null,
        current: 1,
        total: null
      }
    }
  },

  methods: {
    assignData (data) {
      const { next, prev, current, total, results } = data

      Object.assign(this, { items: results })
      Object.assign(this.pages, { next, prev, current, total })

      this.loading = false
    },

    fetchData (url) {
      this.loading = true

      this.$http.get(url).then((response) => {
        this.assignData(response.json(), this.app)
      })
    },

    paginate (direction) {
      if (this.pages[ direction ] === null) return

      this.loading = true

      this.$http.get(this.pages[ direction ]).then((response) => {
        this.assignData(response.json(), this.app)
      })
    },
    nextPage () {
      this.paginate('next')
    },
    prevPage () {
      this.paginate('prev')
    }
  }
}
