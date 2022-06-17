import { createApp } from 'vue'
//import axios from 'axios'
//import VueAxios from 'vue-axios'
import App from './App.vue'

//import Vue from 'vue'
import axios from 'axios'
//import VueAxios from 'vue-axios'

//const app = createApp(App)
//app.use(VueAxios, axios) // 👈
//app.mount('#app')
createApp(App).mount('#app')

// set a prototype for http
Vue.prototype.$http = axios;

