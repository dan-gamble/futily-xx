<template>
  <div class="nations detail" :class="{ 'loading': loading }">
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
      <div v-for="(nation, index) in items" :key="nation.id" :data-index="index" class="list-item">
        <router-link :to="{ name: 'nations:detail', params: { id: nation.slug } }">
          <img alt="" :src="nation.image_sm">
          {{ nation.name }}
        </router-link>
        {{ nation.average_rating }} Average - {{ nation.total_players }} Players - {{ nation.total_bronze }} Bronze - {{ nation.total_silver }} Silver - {{ nation.total_gold }} Gold - {{ nation.total_inform }} Informs - {{ nation.total_special }} Special
      </div>
    </transition-group>

    <hr>

    <pagination :config="pages" :next="nextPage" :prev="prevPage"></pagination>
  </div>
</template>

<script>
  import ListMixin from '../../mixins/List'
  import { NATIONS_API_URL } from '../../utils/constants'

  export default {
    name: 'NationsList',
    mixins: [ListMixin],

    data () {
      return {
        apiUrl: NATIONS_API_URL
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
