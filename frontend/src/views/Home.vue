<template>

  <section class="bg-white">
    <div class="w-full px-5 py-6 mx-auto space-y-5 sm:py-8 md:py-12 sm:space-y-8 md:space-y-16 max-w-7xl">
      <Recipecard :recipes="recipes"/>
      <div class="flex grid grid-cols-12 pb-10 sm:px-5 gap-x-8 gap-y-16">
        <RecipeCardSmall/>
        <RecipeCardSmall/>
        <RecipeCardSmall/>
      </div>
    </div>
  </section>

</template>

<script>
import axios from "axios";
import Recipecard from "@/components/recipecard";
import RecipeCardSmall from "@/components/recipecardsmall";

export default {
  name: "app",
  components: {Recipecard, RecipeCardSmall},
  data() {
    return {
      recipes: {}
    }
  },
  async created() {
    try {
      const res = await axios.get("http://localhost:8080/v1/recipes/1", {
            headers: {
              "accept": "application/json"
            }
          }
      );
      this.recipes = res.data;
      this.recipes.image_url = "http://placekitten.com/g/200/200"
    } catch (e) {
      console.error(e);
    }
  }
};
</script>