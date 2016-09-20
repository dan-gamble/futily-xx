<template>
  <div class="clubs detail" :class="{ 'loading': loading }">
    <hr>

    <pagination :config="pages" :next="nextPage" :prev="prevPage"></pagination>

    <form class="search">
      <div>
        Search: <input type="search" placeholder="Search" v-model="searchQuery">
      </div>

      <div>
        Sort by:
        <select v-model="order">
          <option :value="option" v-for="option in orderOptions">
            {{ option | capFirstNormalize }}
          </option>
        </select>
      </div>
    </form>

    <hr>

    <div v-if="searchQuery.length && !objects.filtered.length">
      There are no search results
    </div>
    <transition-group name="list"
                      tag="div"
                      :css="false"
                      @before-enter="beforeEnter"
                      @enter="enter"
                      @leave="leave"
                      v-else>
      <div v-for="(club, index) in items" :key="club.id" :data-index="index" class="list-item">
        <router-link :to="{ name: 'clubs:detail', params: { id: club.slug } }">
          <img alt="" :src="club.image_dark_sm">
          {{ club.name }}
        </router-link>
        {{ club.average_rating }} Average - {{ club.total_players }} Players - {{ club.total_bronze }} Bronze - {{ club.total_silver }} Silver - {{ club.total_gold }} Gold - {{ club.total_inform }} Informs - {{ club.total_special }} Special
      </div>
    </transition-group>

    <hr>

    <pagination :config="pages" :next="nextPage" :prev="prevPage"></pagination>
  </div>
</template>

<script>
  import ListMixin from '../../mixins/List'
  import { CLUBS_API_URL } from '../../utils/constants'

  export default {
    name: 'ClubsList',
    mixins: [ListMixin],

    data () {
      return {
        apiUrl: CLUBS_API_URL
      }
    }
  }
</script>

<style rel="stylesheet/scss">
  .list {
    display: flex;
    flex-direction: column;
  }

  .list-item-move {
    transition: transform 1s;
  }

  .list-item {
    justify-content: space-between;

    display: flex;
  }
</style>
