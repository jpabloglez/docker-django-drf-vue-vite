<template>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LogIn</title>
    </head>
    <body style="display: inline; width: auto;">
        <div>
            <sidebar></sidebar>
        </div>
        <!-- Insert Sidebar component -->
            <div id="section-borders">
                <section>
                    <p>LogIn</p>
                </section>
            </div>
    </body>
    </html>
</template>


<script>
    import Sidebar from "../Sidebar.vue";
    //import Tutorial from "./tutorial/Tutorial.vue";
    import axios from 'axios';
    export default {
        name: 'LogIn',
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
            doLogin() {
                if (this.emailLogin === "" || this.passwordLogin === "") {
                    this.emptyFields = true;
                } else {
                    alert("You are now logged in");
                }
            },
            doRegister() {
                if (this.emailReg === "" || this.passwordReg === "" || this.confirmReg === "") {
                    this.emptyFields = true;
                } else {
                    alert("You are now registered");
                }
            }
        }
        /*
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
        */
    }
</script>

<style>
    @import "../../assets/css/base.css";
</style>