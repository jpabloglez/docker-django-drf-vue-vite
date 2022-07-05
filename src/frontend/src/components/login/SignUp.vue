<template>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SignIn</title>
    </head>
    <body style="display: inline; width: auto;">
        <div style="display: inline;">
            <!-- Insert Sidebar component -->
            <div id="section-borders">
                <h3>Sign Up</h3>
                <form @submit.prevent="submitForm">
                    <input type="email" name="username" v-model="username">
                    <input type="password" name="password" v-model="password">
                    <buttom type="submit"> Sing Up </buttom>
                </form>
            </div>
        </div>
    </body>
    </html>
</template>


<script>

    import axios from 'axios';
    //axios.defaults.baseURL = 'http://localhost:8000';
    export default {
        name: 'SignUp',
        data() {
            return {
                username: '',
                password: '',
            }
        },
        methods: {
            submitForm(e) {
                const formData = {
                    username: this.username,
                    password: this.password,
                    //email: this.email,
                }
       
                axios.post('api/v1/users', formData).then(response => {
                    this.$router.push('/log-in');
                    console.log(response);
                }).catch(error => {
                    console.log(error);
                });

            }
        }
    }
</script>

<style>
    @import "../../assets/css/base.css";
</style>