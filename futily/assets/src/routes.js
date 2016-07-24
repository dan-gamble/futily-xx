export function configRouter (router) {
  router.hashbang = false

  router.map({
    '/': {
      component: require('./components/Hello.vue')
    },
    '/nations': {
      name: 'nations:list',
      component: require('./components/nations/Index.vue'),
      subRoutes: {
        '/': {
          component: require('./components/nations/List.vue')
        },
        ':id': {
          name: 'nations:detail',
          component: require('./components/nations/Detail.vue')
        }
      }
    },
    '/leagues': {
      name: 'leagues:list',
      component: require('./components/leagues/Index.vue'),
      subRoutes: {
        '/': {
          component: require('./components/leagues/List.vue')
        },
        ':id': {
          name: 'leagues:detail',
          component: require('./components/leagues/Detail.vue')
        }
      }
    },
    '/clubs': {
      name: 'clubs:list',
      component: require('./components/clubs/Index.vue'),
      subRoutes: {
        '/': {
          component: require('./components/clubs/List.vue')
        },
        ':id': {
          name: 'clubs:detail',
          component: require('./components/clubs/Detail.vue')
        }
      }
    }
  })
}
