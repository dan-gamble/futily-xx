import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const scrollBehavior = (to, from, savedPosition) => {
  if (savedPosition) {
    // savedPosition is only available for popstate navigations.
    return savedPosition
  } else {
    // new navigation.
    // scroll to anchor
    if (to.hash) {
      return { anchor: true }
    }
    // explicitly control scroll position
    // check if any matched route config has meta that requires scrolling to top
    if (to.matched.some(m => m.meta.scrollToTop)) {
      return { x: 0, y: 0 }
    }
  }
}

/* eslint-disable no-new */
export const router = new VueRouter({
  scrollBehavior,

  mode: 'history',
  routes: [
    { path: '/', component: require('./components/Hello.vue') },
    { path: '/nations', component: require('./components/nations/Index.vue'),
      children: [
        { path: '', name: 'nations:list', component: require('./components/nations/List.vue') },
        { path: ':id', name: 'nations:detail', component: require('./components/nations/Detail.vue') }
      ]
    },
    { path: '/leagues', component: require('./components/leagues/Index.vue'),
      children: [
        { path: '', name: 'leagues:list', component: require('./components/leagues/List.vue') },
        { path: ':id', name: 'leagues:detail', component: require('./components/leagues/Detail.vue') }
      ]
    },
    { path: '/clubs', component: require('./components/clubs/Index.vue'),
      children: [
        { path: '', name: 'clubs:list', component: require('./components/clubs/List.vue') },
        { path: ':id', name: 'clubs:detail', component: require('./components/clubs/Detail.vue') }
      ]
    },
    { path: '/players', component: require('./components/players/Index.vue'),
      children: [
        { path: '', name: 'players:list', component: require('./components/players/List.vue') },
        { path: ':id', name: 'players:detail', component: require('./components/players/Detail.vue') }
      ]
    }
  ]
})
