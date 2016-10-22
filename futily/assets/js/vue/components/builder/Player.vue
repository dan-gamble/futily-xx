<template>
  <div class="player">
    {{ Number(index) + 1 }} - {{ player.player.common_name }} {{ player.position }} - Chem: {{ overallChemistry }}
    <button type="button" @click="search">Search</button>
  </div>
</template>

<script>
  export default {
    props: {
      player: {
        type: Object,
        required: true
      },
      index: {
        required: true
      }
    },

    computed: {
      overallChemistry () {
        const chemistry = Math.round(this.player.chemistry.links * this.player.chemistry.position)

        return Math.min(10, chemistry + this.player.chemistry.boost)
      }
    },

    methods: {
      search () {
        this.$emit('activate-search', this.index)
      }
    }
  }
</script>

<style scoped>
  button {
    display: inline-block;

    background-color: #fff;
    border: 1px solid #dedede;
  }
</style>
