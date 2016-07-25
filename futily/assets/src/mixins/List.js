export default {
  data () {
    return {
      app: '',
      loading: false,
      pages: {
        next: null,
        prev: null
      }
    }
  },

  methods: {
    assignData (data, app) {
      this.$set(app, data.results)

      this.pages.next = data.next
      this.pages.prev = data.previous

      this.loading = false
    },

    paginate (direction) {
      if (this.pages[direction] === null) return

      this.loading = true

      this.$http.get(this.pages[direction]).then((response) => {
        this.assignData(response.json(), this.app)
      })
    }
  }
}
