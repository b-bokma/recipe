<template>
  <div class="container h-full">
    <div class="bg-gray-100 opacity-60 container h-40 flex justify-center items-center">
      <div class="relative">
        <div class="absolute top-4 left-3">
          <i class="fa fa-search text-gray-400 z-20 hover:text-gray-500"></i>
        </div>
        <input id="searchField" class="h-14 w-96 pl-10 pr-20 rounded-lg z-0 shadow focus:outline-none"
               placeholder="Search Recipe..." type="search"/>
        <div class="absolute top-2 right-2">
          <button class="h-10 w-20 text-white rounded-lg bg-red-500 hover:bg-red-600" @click="search">Search</button>
        </div>

      </div>
    </div>
    <div class="bg-white">

      <ul id="array-rendering">

        <li v-for="dish in dishes">
          <recipe-card :recipes="dish">
          </recipe-card>
        </li>

      </ul>
      <div :class="{'visible': ResultsVisible , 'invisible': !ResultsVisible}" class="bg-gray-50 from-gray-50 p-10"><p
          class="text-black hover:text-blue-600"> Total Results: {{ totalResults }} </p></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import RecipeCard from "@/components/recipecard";

export default {
  name: "RecipeSearch",
  components: {RecipeCard},
  data() {
    return {
      dishes: null,
      offset: 0,
      number: 5,
      totalResults: null,
      ResultsVisible: false
    }
  },
  mounted() {
    console.log(process.env.VUE_APP_SPOONACULAR_API_KEY)
  },
  methods: {
    search() {
      let searchDishes = document.querySelector("#searchField").value;
      axios.get('https://api.spoonacular.com/recipes/complexSearch?query='
          + searchDishes + '&offset=' + this.offset + '&number=' + this.number
          + '&apiKey=' + process.env.VUE_APP_SPOONACULAR_API_KEY)
          .then(response => (
              this.dishes = response.data.results,
                  this.totalResults = response.data.totalResults,
                  this.ResultsVisible = true)
          )
    }
  }
}
</script>

<style scoped>

</style>