<template>
    <div class="analyses_container">
        <div class="analyses_content">
            <ul class="analyses_list">
                <li v-for="analysis in analyses" :key="analysis.id"> 
                <b>Description:</b> {{ analysis.description }} - <b>Modality:</b> {{ analysis.modality }} <b>Customer:</b> {{ analysis.customer }}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'Analyses',
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
