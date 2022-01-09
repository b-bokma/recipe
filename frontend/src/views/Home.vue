<template>

  <section class="bg-white">
    <div class="w-full px-5 py-6 mx-auto space-y-5 sm:py-8 md:py-12 sm:space-y-8 md:space-y-16 max-w-7xl">
      <Recipecard :recipes="APIData"/>
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
import {getAPI} from "@/axios-api";
import {mapState} from 'vuex'

export default {
  name: "app",
  components: {Recipecard, RecipeCardSmall},
  computed: mapState(['APIData']),
  created() {
    getAPI.get("/recipes/1", {
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`,
            Accept: "application/json"
          }
        }
    ).then(response => {
      this.$store.state.APIData = response.data
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>