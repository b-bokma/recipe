<template>

  <!-- Section 1 -->
  <section class="relative w-full px-8 text-gray-700 bg-white body-font">
    <div class="container flex flex-col flex-wrap items-center justify-between py-5 mx-auto md:flex-row max-w-7xl">
      <a class="relative z-10 flex items-center w-auto text-2xl font-extrabold leading-none text-black select-none"
         href="#_">bokma.</a>

      <nav
          class="top-0 left-0 z-0 flex items-center justify-center w-full h-full py-5 -ml-0 space-x-5 text-base md:-ml-5 md:py-0 md:absolute">

        <router-link v-if="isLoggedIn" :to="{ name: 'Home' }"
                     class="relative font-medium leading-6 text-gray-800 transition duration-150 ease-out hover:text-green-600"
                     x-data="{ hover: false }" @mouseenter="hover = true" @mouseleave="hover = false"><span class="block">Home</span>
        </router-link>
        <router-link v-if="isLoggedIn" :to="{ name: 'RecipeSearch' }"
                     class="relative font-medium leading-6 text-gray-800 transition duration-150 ease-out hover:text-green-600"
                     x-data="{ hover: false }" @mouseenter="hover = true" @mouseleave="hover = false"><span
            class="block">Search</span>

        </router-link>
        </nav><nav class="justify-items-end">
                <router-link v-if="isLoggedIn" :to="{ name: 'Logout' }"
                     class="relative font-medium leading-6 text-gray-800 transition duration-150 ease-out hover:text-green-600"
                     x-data="{ hover: false }" @mouseenter="hover = true" @mouseleave="hover = false"><span
            class="block">Logout</span>
        </router-link>
      </nav>
    </div>
  </section>

</template>

<script>
export default {
    name: 'login',
  data () {
    return {
      isLogged: this.checkIfIsLogged()
    }
  },
  computed: {
  isLoggedIn() {
    return this.$store.state.accessToken;
  }
},
  methods: {
    checkIfIsLogged() {
      if (localStorage.hasOwnProperty("accessToken")) {
        let accessToken = localStorage.getItem('accessToken')
      };
      if (typeof accessToken != "undefined") {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style scoped>

</style>

