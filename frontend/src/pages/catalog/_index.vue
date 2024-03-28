<script setup>
import Header from "../../components/Header.vue";
import Petcard from "../../components/Petcard.vue";
import { ref } from "vue";

const pets = ref([]);
(async function f() {
  const response = await fetch("http://localhost:3000/animals");
  pets.value = await response.json();
})();
</script>
<template>
  <Header />
  <div class="h-16" />
  <div class="h-20 bg-blue-50 flex justify-center items-center">
    <p class="text-lg">Наши друзья ищут свой дом!</p>
  </div>
  <div class="flex flex-wrap p-10 gap-10 justify-center">
    <Petcard
      v-for="pet in pets"
      :name="pet.name"
      :image="pet.image_url"
      href="/"
    />
  </div>
</template>
