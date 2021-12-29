<template>
  <div class="flex flex-col items-start col-span-12 space-y-3 sm:col-span-6 xl:col-span-4">
    <a class="block" href="#_">
      <img class="object-cover w-full mb-2 overflow-hidden rounded-lg max-h-56"
           src="https://cdn.devdojo.com/images/may2021/lemons.jpg">
    </a>
    <div
        class="bg-yellow-400 flex items-center px-3 py-1.5 leading-none rounded-full text-xs font-medium uppercase text-white inline-block">
      <span>Nutrition</span>
    </div>
    <h2 class="text-lg font-bold sm:text-xl md:text-2xl">The Fruits Life</h2>
    <p class="text-sm text-gray-500">Take a moment and enjoy to enjoy the many fruits of life. Relaxation and a healthy
      diet can go a long way.</p>
    <p class="pt-2 text-xs font-medium"><a class="mr-1 underline" href="#_">Jake Caldwell</a> · <span class="mx-1">May 15, 2021</span>
      · <span class="mx-1 text-gray-600">3 min. read</span></p>
  </div>
</template>

<script>
export default {
  name: 'RecipeCardSmall',
  props: ['recipes']
}
</script>
