<template>
  <div id="app">
    <h1>Oliver's Website Critique</h1>
    <SimpleUI />
  </div>
</template>

<script>
import SimpleUI from './components/SimpleUI.vue';

export default {
  name: 'App',
  components: {
    SimpleUI
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
