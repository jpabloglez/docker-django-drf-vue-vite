<!--
<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
// import HelloWorld from './components/HelloWorld.vue'
import HelloWorld from './components/Tasks.vue'
</script>
-->
<template>
  <div>
    <Sidebar></Sidebar>
  </div>
  <div>
    <Navbar></Navbar>
  </div>
  <br>
  <div align="center">
      <Tutorial></Tutorial>
  </div>

  <!--
  <div id="app">
    Tasks: <Tasks/>
  </div>
  -->
  <div id="app">
    Analyses: <Analyses/>
  </div>
  
</template>

<script>
  //import Tasks from "./components/Tasks.vue";
  import Navbar from "./components/Navbar.vue";
  import Sidebar from "./components/Sidebar.vue";
  import Analyses from "./components/Analyses.vue";
  import Tutorial from "./components/tutorial/Tutorial.vue";
  
  // import Vue from Vue;
  // Vue.loadScript("src/assets/js/particles.js")
  export default {
    name: "App",
    components: {
      Analyses,
      Navbar,
      Sidebar,
      Tutorial,
      // Tasks,
    },
  };

</script>


<!--
<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Hello Vue 3 + TypeScript + Vite" />
</template>
-->

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
