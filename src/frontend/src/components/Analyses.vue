<template>
    <body style="display: inline; width: auto;">
        <div>
            <sidebar></sidebar>
        </div>
        <!-- Insert Sidebar component -->
            <div id="section-borders">
                <div id="btest">
                    <!-- Bootstrapp buttom -->
                    <button class="btn btn-primary"> Bootstrapp </button>
                    <!-- User router to link page -->
                    <button id="buttom" @click="$router.push('/')">Tutorial</button>
                </div>
                <!-- Cards section -->
                
                <section id="cards_section">
                    
                    <div class="analyses_container">
                        <div class="analyses_content">
                            <ul class="analyses_list">
                                <li v-for="analysis in analyses" :key="analysis.id"> 
                                <div id="card">
                                    <div class="card-body">
                                        <p class="card-text"><b>Description:</b> {{ analysis.description }} - <b>Modality:</b> {{ analysis.modality }} <b>Customer:</b> {{ analysis.customer }}</p>
                                        <button id="buttom" @click="$router.push('/')">Results</button>
                                    </div>
                                </div>
                                
                                </li>
                            </ul>
                        </div>
                    </div>
                </section>

            </div>
    </body>
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
        width: 100%;
        background-color: lightcyan;
    }
    .analyses_content {
        width: 100%;
        padding: 20px;
        background-color: lightcyan;
        align-content: center;
    }
    .analysis_list {
        width: 100%;
        align-content: center;
        list-style: none;
        background-color: lightcyan;
        padding: 0;
    }
    
    #cards_section{
        width: 100%;
        justify-content: space-between;
        align-items: center;
        flex-direction: column;
    }

    #card{
        width: 100%;
        background-color: lightcyan;
        padding: 20px;
        margin: 20px;
        border-radius: 10px;
    }

    ul {
        text-align: center;
        list-style-position: inside;
    }
    
</style>
