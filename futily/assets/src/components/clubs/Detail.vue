<template>
  <div class="club">
    {{ club.name }}
  </div>
</template>

<script>
  export default {
    data () {
      return {
        club: {}
      }
    },

    route: {
      data () {
        this.$http.get(`/api/clubs/${this.$route.params.id}`).then((response) => {
          this.club = response.data
        })
      }
    }
  }
</script>
