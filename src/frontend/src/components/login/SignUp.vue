<template>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SignIn</title>
    </head>
    <body style="display: inline; width: auto; padding: 10px 10px">
        <div style="display: inline;" align="center">
            <!-- Insert Sidebar component -->
            <div id="section-borders" style="width: 40%">
                <h3>Sign Up</h3>
                <form  @submit.prevent="submitForm" align="left">
                    <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label">Email address</label>
                        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" value="email">
                        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input type="password" class="form-control" id="exampleInputPassword1" value="password">
                    </div>
                    <div class="mb-3 form-check">
                        <input type="checkbox" class="form-check-input" id="exampleCheck1">
                        <label class="form-check-label" for="exampleCheck1">Check me out</label>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                    </form>
            </div>
        </div>
    </body>
    </html>
</template>


<script>

    import axios from 'axios';

    export default {
        name: 'SignUp',
        data() {
            return {
                email: '',
                password: '',
            }
        },
        methods: {

            submitForm(e) {
                //const endpoint = 'http://localhost:8000/api/v1/users';
                const formData = {
                    email: this.email,
                    password: this.password,
                    //email: this.email,
                }

                console.log("formData", formData);

                axios.post("http://localhost:8000/api/v1/users/", formData)
                    .then(response => {
                        this.$router.push('/LogIn');
                        console.log(response);
                    })
                    .catch(error => console.log(error));
                
            }
        }
    }
</script>

<style>
    @import "../../assets/css/base.css";
</style>