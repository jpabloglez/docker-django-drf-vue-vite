<template>
  <div class="dropdown">
    <button
      class="btn btn-primary dropdown-toggle"
      type="button" id="dropdownMenuButton1"
      data-bs-toggle="dropdown"
      aria-expanded="false">
      Dropdown button: {{value}}
    </button>
    <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1" role="menu">
      <li v-for="option in options" :key="option">
        <a class="dropdown-item" @click="value = option" href="javascript:void(0)">{{option}}</a>
      </li>
    </ul>
  </div>
  </template>
  
  <script>

    export default {

        name: 'Drop', // Name of the current component
        data() {
            return {
                options: ["Hola Caracola", "B", "c"],
                value: "B",
            }
        },
    }
  
</script>