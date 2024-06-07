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
  <div class="background"></div>
  <div class="h-16" />
  <div class="label">
    <p class="text-lg">Наши друзья ищут свой дом!</p>
  </div>
  <div class="flex flex-wrap p-10 gap-10 justify-center">
    <Petcard
      v-for="pet in pets"
      :name="pet.name"
      :image="pet.image_url"
      :href="'/petpage?id='+pet._id"
    />
  </div>
</template>

<style scoped>
.background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('https://img.freepik.com/free-vector/dog-cat-paw-print-with-heart-pattern-design_1017-36752.jpg?w=1380&t=st=1717697142~exp=1717697742~hmac=5c237a5918037f1f28610bafc24def9c2d7e68eb535d72204bdde07c178d5b41'); 
  background-size: cover;
  background-position: center;
  filter: brightness(0.7) blur(8px);
  z-index: -1;
}

.label{
  /*h-20 bg-blue-50 flex justify-center items-center */
  height: 5rem;
  display:  flex;
  justify-content: center;
  align-items: center;
  background-color: white;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.355); 
}
</style>