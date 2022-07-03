<!--
<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
// import HelloWorld from './components/HelloWorld.vue'
import HelloWorld from './components/Tasks.vue'
</script>
-->

<!--
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
  
  <div id="app"> <h2> Tasks </h2> <Tasks/> </div>
  
  <div id="app">  <h2> Analyses </h2> <Analyses/>  </div>
  
</template>
-->

<template>
  <!--<the-navigation @set-page="setActivePage"></the-navigation>-->
  <main>
    <router-view></router-view>
  </main>
</template>

<script>
  import Tasks from "./components/Tasks.vue";
  import Navbar from "./components/Navbar.vue";
  import Sidebar from "./components/Sidebar.vue";
  import Analyses from "./components/Analyses.vue";
  import Tutorial from "./components/tutorial/Tutorial.vue";
  
  export default {
    name: "Base",
    components: {
      Analyses,
      Navbar,
      Sidebar,
      Tutorial,
      Tasks,
    },
  };

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
