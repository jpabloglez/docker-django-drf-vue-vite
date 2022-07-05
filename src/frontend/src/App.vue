<template>
<!--
    <body>
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Navbar</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
              <a class="nav-link" href="#">Features</a>
              <a class="nav-link" href="#">Pricing</a>
              <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
            </div>
          </div>
        </div>
      </nav>
    </body>
  -->
    <!--<router-view></router-view>-->
      <div style="display: inline;">
        <router-link to="/SignUp">Sign Up</router-link>
      </div>
      <div>
        <router-link to="/LogIn">Log In</router-link>
      </div>

      <router-view></router-view>
</template>

<script>
  import axios from 'axios';

  import LogIn from "./components/login/LogIn.vue";
  import SignUp from "./components/login/SignUp.vue";
  
  export default {
    name: "App",
    beforeCreate(){
      this.$store.commit('initializeStore');
      const token = this.$store.state.token

      if ( token ){
        axios.defaults.headers.common['Authorization'] = "Token " + token;
      } else {
        axios.defaults.headers.common['Authorization'] = " ";
      }
  }
}
</script>


<!--
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
*/
</script>
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

