<template>
    <!DOCTYPE html>
    <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Analyses</title>
          <!--<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous" />-->
      </head>

      <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <div class="container-fluid">
            <a class="navbar-brand" href="#">Qubiotech.ai</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
              <div class="navbar-nav">
                <a class="nav-link" href="#"><router-link to="/">Home</router-link></a>
                <a class="nav-link" href="#"><router-link to="/SignUp">Sign Up</router-link></a>
                <a class="nav-link" href="#"><router-link to="/LogIn">Log In</router-link></a>
                <a class="nav-link" href="#"><router-link to="/Analyses">Analyses</router-link></a>
                <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
              </div>
            </div>
          </div>
        </nav>
        <div align="center">
          <router-view></router-view>
        </div>
      </body>
    </html>
</template>

<script>
  import axios from 'axios';
  
  
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

