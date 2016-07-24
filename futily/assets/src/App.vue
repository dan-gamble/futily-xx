<template>
  <div id="app">
    <a v-link="{ path: '/' }"><img class="logo" src="./assets/logo.png"></a>
    <div class="links">
      <a v-link="{ name: 'nations:list' }">Nations</a>
    </div>

    <router-view class="view" transition="test" transition-mode="out-in" keep-alive></router-view>
  </div>
</template>

<script>
  import store from './vuex/store'

  export default {
    store
  }
</script>

<style>
  .view {
    transition: all 0.5s ease;
  }

  .test-enter, .test-leave {
    opacity: 0;
    transform: translate3d(10px, 0, 0);
  }

  #app {
    color: #2c3e50;
    max-width: 600px;
    margin-right: auto;
    margin-left: auto;
    font-family: Source Sans Pro, Helvetica, sans-serif;
    text-align: center;
  }

  #app a {
    color: #42b983;
    text-decoration: none;
  }

  .logo {
    width: 100px;
    height: 100px
  }
</style>
