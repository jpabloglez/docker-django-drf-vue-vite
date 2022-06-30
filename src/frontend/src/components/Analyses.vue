<template>
    <div class="analyses_container">
        <div class="analyses_content">
            <ul class="analyses_list">
                <li v-for="analysis in analyses" :key="analysis.id">
                    <p> <b>Description:</b> {{ analysis.description }} - <b>Modality:</b> {{ analysis.modality }} <b>Customer:</b> {{ analysis.customer }} </p>
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
/*
    body {
    background-color: lightcyan;
    }
    */

    .analyses_container {
        background-color: lightgray;
    }
</style>
