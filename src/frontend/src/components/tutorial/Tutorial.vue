

<template>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <div id="section-borders">
            <section id="say-hello">
                <!-- Data interpolation example-->
                <p> <b>Mensaje:</b> {{ message }}</p>
                <!-- Data binding example -->
                <h3> Visit Vue reference: <a v-bind:href="vue_link"> about Vue </a></h3>
                <!-- Show the result of applying a method-->
                <p> Resultado aleatorio: {{ selectOption() }} </p>
                <!-- HTML binding in order to include html elements-->
                <p> v-html="htmlTag" </p>
                <!-- On click directive-->
                <div>
                    <button id="buttom" v-on:click="Add(2)"> Add element </button> - <button id="buttom" v-on:click="Remove(1)"> Remove element </button>
                </div>
                <h2> Counter: {{ counter }}</h2>
                <!-- Listener to input data-->
                <input type="text" v-on:input="setName($event, 'PEREZ')">
                <!-- Show the data inserted by user -->
                <p> Your name: {{ name }} </p>
                <!-- Event modifiers-->
                <form id="form">
                    <input type="text">
                    <button> Sign up </button>
                </form>
            
                
            </section>
        </div>
    </body>
    </html>
</template>

<script>
    export default {
        /*
        Data container to be exported
        */
        data() {
            return {
                message: "Hola Caracola",
                vue_link: "https://vuejs.org/",
                htmlTag: "<h2> Esto es un H2 <h2>",
                optionA: "Ha salido menor que 0.5 (opción A)",
                optionB: "Ha salido >= 0.5 (opción B)",
                counter: 0,
                name: "",
            }
        },

        methods: {
            selectOption(){
                const randomNumber = Math.random(); /* This is a JS built-in method */
                if (randomNumber <0.5) {
                    return this.optionA
                }
                else{
                    return this.optionB
                }
            },
            Add(num){
                this.counter += num;
            },
            Remove(num){
                this.counter -= num;
            },
            setName(event, lastName){
                this.name = event.target.value + ' ' + lastName;
            },
        }

    }

</script>

<style>
/*
* Here it is defined the styling 
*/

/* Import CSS from assets files */
@import "../../assets/css/buttoms.css";

  #section-borders{
    background-color: lightcyan;
    align-self: center;
    width: 80%;
    height: 40%;
    border-radius: 20px;
    border-color: lightcyan;
  }
  #buttom{
    background-color: lightpink;
    border-radius: 10px;
  }
  #form{
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 15px 15px;
    background-color: lightpink;
  }
    
</style>

