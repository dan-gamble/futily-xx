<template>
  <div class="nation">
    {{ nation.name }}
    <img alt="" :src="nation.image_sm">
    <img alt="" :src="nation.image_md">
    <img alt="" :src="nation.image_lg">
  </div>
</template>

<script>
  export default {
    data () {
      return {
        nation: {}
      }
    },

    route: {
      data () {
        this.$http.get(`/api/nations/${this.$route.params.id}`).then((response) => {
          this.nation = response.json()
        })
      }
    }
  }
</script>
