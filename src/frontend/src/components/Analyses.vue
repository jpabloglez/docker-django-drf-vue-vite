<template>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Analyses</title>
    </head>
    <body>
        <sidebar></sidebar>
        <!-- Insert Sidebar component -->
            <div id="section-borders">
                <div id="btest">
                    <!-- Bootstrapp buttom -->
                    <button class="btn btn-primary"> Bootstrapp </button>
                    <!-- User router to link page -->
                    <button id="buttom" @click="$router.push('/')">Tutorial</button>
                </div>
                <section id="say-hello">
                    <div class="analyses_container">
                        <div class="analyses_content">
                            <ul class="analyses_list">
                                <li v-for="analysis in analyses" :key="analysis.id"> 
                                <b>Description:</b> {{ analysis.description }} - <b>Modality:</b> {{ analysis.modality }} <b>Customer:</b> {{ analysis.customer }}
                                </li>
                            </ul>
                        </div>
                    </div>
                </section>
            </div>
    </body>
    </html>
</template>


<script>
    import Sidebar from "./Sidebar.vue";
    //import Tutorial from "./tutorial/Tutorial.vue";
    import axios from 'axios';
    export default {
        name: 'Analyses',
        components: {
            'sidebar': Sidebar,
            //'tutorial': Tutorial,
        },
        data() {
            return {
                analyses: [],
                errors: []
            }
        },
        methods: {
            async getData() {
                try {
                    const response = await axios.get('http://localhost:8000/api/analyses/');
                    console.log("LOG", response);
                    this.analyses = response.data; 
                } catch (error) {
                    console.log(error);
                    this.errors.push(e);
                }
            },
        },
        created() {
            this.getData();
        }
    }
</script>


<style>

    @import "../assets/css/base.css";

    .analyses_container {
        display: flex;
        background-color: lightcyan;
    }
    .analyses_content {
        width: 100%;
        padding: 20px;
        background-color: lightcyan;
        align-content: center;
    }
    .analysis_list {
        align-content: center;
        list-style: none;
        padding: 0;
    }
    ul {
        text-align: center;
        list-style-position: inside;
    }
    
</style>
