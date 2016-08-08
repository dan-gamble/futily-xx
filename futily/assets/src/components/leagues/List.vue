<template>
  <div class="leagues detail" :class="{ 'loading': loading }">
    <hr>

    <pagination :config="pages" :next="nextPage" :prev="prevPage"></pagination>

    <hr>

    <transition-group name="list"
                      tag="div"
                      :css="false"
                      @before-enter="beforeEnter"
                      @enter="enter"
                      @leave="leave">
      <div v-for="(league, index) in items" :key="league.id" :data-index="index">
        <router-link :to="{ name: 'leagues:detail', params: { id: league.slug } }">
          {{ league.name }}
        </router-link>
      </div>
    </transition-group>

    <hr>

    <pagination :config="pages" :next="nextPage" :prev="prevPage"></pagination>
  </div>
</template>

<script>
  import _ from 'lodash'
  import Velocity from 'velocity-animate'
  import ListMixin from '../../mixins/List'
  import { LEAGUES_API_URL } from '../../utils/constants'

  import Pagination from '../pagination/Pagination.vue'

  export default {
    name: 'LeaguesList',
    mixins: [ListMixin],

    components: {
      Pagination
    },

    data () {
      return {
        items: []
      }
    },

    created () {
      let url = LEAGUES_API_URL

      if (_.has(this.$route.query, 'page')) {
        url += `?page=${this.$route.query.page}`
      }

      this.fetchData(url)
    },

    watch: {
      '$route' () {
        this.fetchData(LEAGUES_API_URL)
      }
    },

    methods: {
      beforeEnter (el) {
        el.style.opacity = 0
        el.style.height = 0
      },

      enter (el, done) {
        const delay = el.dataset.index * 50

        setTimeout(function () {
          Velocity(
              el,
              { opacity: 1, height: '1.6em' },
              { complete: done }
          )
        }, delay)
      },

      leave (el, done) {
        const delay = el.dataset.index * 50

        setTimeout(function () {
          Velocity(
              el,
              { opacity: 0, height: 0 },
              { complete: done }
          )
        }, delay)
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
</style>
