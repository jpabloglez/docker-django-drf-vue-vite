import App from './App.vue';

import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import store from './store';
import axios from 'axios';
//import DashboardPlugin from '@/plugins/blackDashboard'

//import Vue from 'vue';
//import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap and BootstrapVue CSS files (order is important)
//import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

//import "bootstrap" ;
//import "bootstrap/dist/css/bootstrap.min.css";


//axios.defaults.baseURL = 'http://localhost:8080';

//import App from './components/tutorial/Tutorial.vue';
//import Vue from 'vue';

// Import components
//import Login from './components/login/Login.vue';
import LogIn from './components/login/LogIn.vue';
import SignUp from './components/login/SignUp.vue';
import SignIn from './components/login/SignIn.vue';
import Analyses from './components/Analyses.vue';
import Tutorial from './components/tutorial/Tutorial.vue';
//import Drop from './components/tutorial/Drop.vue';

//import Base from './App.vue';



// Create the router app
const router = createRouter({
    history: createWebHistory(),
    routes: [
        { 
            path: '/', 
            name: 'Home',
            component: Tutorial 
        },
        { 
            path: '/SignIn', 
            name: 'SignIn',
            component: SignIn 
        },
        { 
            path: '/LogIn', 
            name: 'LogIn',
            component: LogIn 
        },
        { 
            path: '/SignUp', 
            name: 'SignUp',
            component: SignUp 
        },
        { 
            path: '/Analyses', 
            name: 'Analyses',
            component: Analyses 
        },
        //{ path: '/login', component: LogIn },
        //{ path: '/analyses', component: Analyses },
        //{ path: '/app', component: App },
        //{ path: '/signin', component: SignIn },
    ]
});

// Mount the app
const app = createApp(App); 

app.use(router, axios);
app.use(store);
//app.use(DashboardPlugin)
//app.component("bootsrap");
//app.use(BootstrapVue)


app.mount('#app'); 

// createApp(App).mount('#app'); // this can also do the trick
//{ path: '/analyses', component: Analyses },
