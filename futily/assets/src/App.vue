<template>
  <div id="app">
    <router-link :to="{ path: '/' }">
      <img class="logo" src="./assets/logo.png">
    </router-link>

    <div class="links">
      <router-link :to="{ name: 'nations:list' }">Nations</router-link>
      <router-link :to="{ name: 'leagues:list' }">Leagues</router-link>
      <router-link :to="{ name: 'clubs:list' }">Clubs</router-link>
      <router-link :to="{ name: 'players:list' }">Players</router-link>
    </div>

    <transition name="view" mode="out-in">
      <router-view class="view"></router-view>
    </transition>
  </div>
</template>

<style>
  .view {
    transition: all 0.5s ease;
  }

  .view {
    transition: all .35s ease;
  }

  .view-enter, .view-leave-active {
    opacity: 0;
  }

  #app {
    color: #2c3e50;
    max-width: 800px;
    margin-right: auto;
    margin-left: auto;
    font-family: Source Sans Pro, Helvetica, sans-serif;
  }

  a {
    color: #42b983;
    text-decoration: none;
  }

  .logo {
    width: 100px;
    height: 100px
  }

  .link-active {
    text-decoration: underline;
  }
</style>
