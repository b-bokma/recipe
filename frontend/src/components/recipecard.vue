<template>
  <div class="bg-gray-50 p-3 m-10">
    <div class="flex flex-col items-center sm:px-5 md:flex-row">
      <div class="w-full md:w-1/4">
        <a class="block" href="#_" @click="show=!show, retrieve_details(recipes.id)">
          <img :src=recipes.image class="object-cover w-full h-full rounded-t-lg rounded-lg max-h-64 sm:max-h-96">
        </a>
      </div>
      <div class="flex flex-col items-start justify-center w-full h-full py-6 mb-6 md:mb-0 md:w-1/2">
        <div
            class="flex flex-col items-start justify-center h-full space-y-3 transform md:pl-10 lg:pl-16 md:space-y-5">

          <h1 class="text-2xl font-bold leading-none lg:text-3xl xl:text-4xl"><a
              href="#_" @click="show=!show, retrieve_details(recipes.id)">{{ recipes.title }}</a></h1>
        </div>

      </div>

    </div>
    <div :class="{block: show, hidden: !show}" class="bg-slate-50 px-4 py-3 my-2   min-h-80">
      <h3 class="text-l text-gray-800 mt-3 mb-4">Summary:</h3>
      <div class="text-sm text-gray-500" v-html="recipe_details.summary"></div>
      <h3 class="text-l text-gray-800 mt-3 mb-4">Instructions</h3>
      <div class="text-sm text-gray-500" v-html="recipe_details.instructions"></div>
      <ul>
        <li v-for="instruction in recipe_details.analyzedInstructions"/>
        {{ instruction }}
      </ul>
      <div class="text-sm text-gray-500" v-html="recipe_details.ingredients"></div>
    </div>
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: 'RecipeCard',
  props: ['recipes'],
  data() {
    return {
      show: false,
      recipe_details: {
        'summary': null,
        'instructions': null,
        'analyzedInstructions': []
      }
    }
  },
  methods: {
    retrieve_details(recipe_id) {
      axios.get('https://api.spoonacular.com/recipes/' + recipe_id + '/information?includeNutrition&apiKey=' + process.env.VUE_APP_SPOONACULAR_API_KEY)
          .then(response => {
                if (this.recipe_details.summary === null) {
                  this.recipe_details = response.data
                }
              }
          )
    }
  }
}
</script>