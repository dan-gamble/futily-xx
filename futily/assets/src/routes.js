export function configRouter (router) {
  router.hashbang = false

  router.map({
    '/': {
      component: require('./components/Hello.vue')
    },
    '/nations': {
      name: 'nations:list',
      component: require('./components/nations/List.vue')
    }
  })
}
