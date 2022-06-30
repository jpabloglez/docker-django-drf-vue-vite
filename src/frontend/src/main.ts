import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';

import App from './App.vue';
//import App from './components/tutorial/Tutorial.vue';
//import Vue from 'vue';

// Import components
import Login from './components/login/Login.vue';
//import Signup from './components/login/Signup.vue';
import Analyses from './components/Analyses.vue';
import Tutorial from './components/tutorial/Tutorial.vue';

// Create the router app
const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: Tutorial },
        { path: '/login', component: Login },
        { path: '/analyses', component: Analyses },
    ]
});

// Mount the app
const app = createApp(App); 

app.use(router);

app.mount('#app'); 

// createApp(App).mount('#app'); // this can also do the trick
