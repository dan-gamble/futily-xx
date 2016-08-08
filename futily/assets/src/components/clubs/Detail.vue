<template>
  <div class="club">
    {{ club.name }}
  </div>
</template>

<script>
  export default {
    name: 'ClubsDetail',
    data () {
      return {
        club: {}
      }
    },

    mounted () {
      this.$http.get(`/api/clubs/${this.$route.params.id}`).then((response) => {
        this.club = response.json()
      })
    }
  }
</script>
