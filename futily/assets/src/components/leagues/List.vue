<template>
  <div class="leagues detail" :class="{ 'loading': loading }">
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
      <div v-for="(league, index) in items" :key="league.id" :data-index="index" class="league">
        <router-link :to="{ name: 'leagues:detail', params: { id: league.slug } }">
          <img alt="" :src="league.image_sm">
          {{ league.name }}
        </router-link>
        {{ league.average_rating }} Average - {{ league.total_players }} Players - {{ league.total_bronze }} Bronze - {{ league.total_silver }} Silver - {{ league.total_gold }} Gold - {{ league.total_inform }} Informs - {{ league.total_special }} Special
      </div>
    </transition-group>

    <hr>

    <pagination :config="pages" :next="nextPage" :prev="prevPage"></pagination>
  </div>
</template>

<script>
  import ListMixin from '../../mixins/List'
  import { LEAGUES_API_URL } from '../../utils/constants'

  export default {
    name: 'LeaguesList',
    mixins: [ListMixin],

    data () {
      return {
        apiUrl: LEAGUES_API_URL
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

  .league {
    justify-content: space-between;

    display: flex;
  }
</style>
