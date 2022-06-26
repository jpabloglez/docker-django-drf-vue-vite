<template>
    <div class="tasks_container">
        <div class="tasks_content">
            <!--<div id="card">-->
            <h1> Tasks status</h1>
            <ul class="tasks_list">
                <li v-for="task in tasks" :key="task.id">
                    <h2>title: {{ task.title }}</h2>
                    <p>description: {{ task.description }}</p>
                    <button @click="toggleTask(task)">
                        {{ task.completed ? 'Undo' : 'Complete' }}
                    </button>
                    <button @click="deleteTask(task)">Delete</button>
                </li>
            </ul>
            <!--</div>-->
        </div>
    </div>
</template>



<script>
import axios from 'axios';

export default {
  data() {
    return {
      tasks: ['']
    }
  },
  mounted() {
    axios.get('http://localhost:8000/api/tasks/').then((response) => {
        console.log("LOG:", response.data)
        this.tasks = response.data
      })
    /* Try to add Particles JS annimation
    let particlesScript = document.createElement('script')
    particlesScript.setAttribute('src', 'src/assets/js/particles.js')
    document.head.appendChild(particlesScript)*/
  }
}

</script>

<!--
<script>
    export default {
        data() {
            return {
                // tasks
                tasks: ['']
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch tasks
                    const response = await this.axios.get('http://localhost:8000/api/tasks/');
                    console.log(response)
                    this.tasks = response.data; 
                } catch (error) {
                    console.log(error);
                }
            },
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>
-->

<style>
    button {
    padding: 1.3em 3em;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 2.5px;
    font-weight: 500;
    color: #000;
    background-color: #fff;
    border: none;
    border-radius: 45px;
    box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease 0s;
    cursor: pointer;
    outline: none;
    }

    button:hover {
    background-color: #b8deff;
    box-shadow: 0px 15px 20px rgb(123, 163, 224);
    color: #fff;
    transform: translateY(-7px);
    }

    button:active {
    transform: translateY(-1px);
    }

    #card {
    width: 190px;
    height: 254px;
    border-radius: 30px;
    background: #e0e0e0;
    box-shadow: 15px 15px 30px #bebebe,
                -15px -15px 30px #ffffff;
    }
</style>
