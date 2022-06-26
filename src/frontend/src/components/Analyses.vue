<template>
    <div class="analyses_container">
        <div class="analyses_content">
            <h1> Analyses </h1>
            <ul class="analyses_list">
                <li v-for="analysis in analyses" :key="analysis.id">
                    <h3>Description: {{ analysis.description }}</h3>
                    <h3>Modality: {{ analysis.modality }}</h3>
                    <h3>Customer: {{ analysis.customer }}</h3>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
    export default {
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
                    console.log("LOG", response)
                    this.analyses = response.data; 
                } catch (error) {
                    console.log(error);
                    this.errors.push(e)
                }
            },
        },
        created() {
            this.getData();
        }
    }
</script>


<style>
    body {
    background-color: lightcyan;
    }
</style>
