<template>
    <div class="tasks_container">
        <h3 style="color:lightcoral"> Tasks creation </h3>

        <div class="add_task">
            <!-- Create new Tasks (action)-->
            <form v-on:submit.prevent="submitForm">
                <div class="form-group">
                    <label for="title"> <h4> Title </h4> </label>
                    <input type="text" class="form-control" id="title" v-model="title">
                </div>
                <div class="form-group">
                    <label for="description"> <h4> Description </h4> </label>
                    <textarea class="form-control" id="description" v-model="description"></textarea>
                </div>
                <div class="form-group">
                    <button type="submit">Add Task</button>
                </div>
            </form>
        </div>

        <div class="tasks_content">
            <!-- Display Tasks properties-->
            <h3 style="color:lightcoral"> Tasks status </h3>
            <ul class="tasks_list">
                <li v-for="task in tasks" :key="task.id">
                    <h4> - Title: {{ task.title }}</h4>
                    <h4> - Description: {{ task.description }}</h4>
                    <button @click="toggleTask(task)">
                        {{ task.completed ? 'Undo' : 'Complete' }}
                    </button>
                    <button @click="deleteTask(task)">Delete</button>
                </li>
            </ul>
        </div>

    </div>
</template>


<!--  <script lang="ts"> -->
<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                tasks: [''],
                title: '',
                description: '',
            }
        },

        methods: {
            // Getting tasks data from API
            async getData() {
                try {
                    const response = await axios.get('http://localhost:8000/api/tasks/');
                    console.log("LOG", response);
                    this.tasks = response.data; 
                } catch (error) {
                    console.log(error);
                    this.errors.push(e);
                }
            },
            // Creating a new Task (action)
            async submitForm() {
                try {
                    const response = await axios.post('http://localhost:8000/api/tasks/', {
                        title: this.title,
                        description: this.description,
                        completed: false,
                    });
                    this.tasks.push(response.data);
                    this.title = '';
                    this.description = '';
                } catch (error) {
                    console.log(error);
                }
            },
            // Updating a Task (action)
            async toggleTask(task) {
                try {
                    const response = await axios.patch(`http://localhost:8000/api/tasks/${task.id}/`, {
                        completed: !task.completed,
                        title: task.title,
                        description: task.description,
                    });

                    // Get the index of the task being updated
                    let taskIndex = this.tasks.findIndex(t => t.id === task.id);
                    // Reset the tasks array with the new data of the updated task
                    this.tasks = this.tasks.map((task) => {
                        if(this.tasks.findIndex(t => t.id === task.id) === taskIndex){
                            return response.data;
                        }
                        return task;
                    });
                }catch(error){
                    console.log(error);
                }   

            },
            // Deleting a Task (action)
            async deleteTask(task) {
                let confirmation = confirm("Do you want to delete this task?"); 
                if(confirmation){
                    try{
                        // Send a request to delete the task
                        const response = await axios.delete(`http://localhost:8000/api/tasks/${task.id}`);
                        // Refresh the tasks
                        this.getData();
                    }catch(error){
                        console.log(error)
                    }
                }  
            },
        },

    }

</script>


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

    .tasks_container {
        display: flex;
        background-color: lightgrey;


    }
    .form_group{
        border-color: lightgray;
        border-radius: 10px;
        
    }
</style>
