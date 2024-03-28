<script setup>
const type = defineModel("type");
const description = defineModel("description");
const age = defineModel("age");
const name = defineModel("name");
const image_url = defineModel("image_url");

const URL = "http://localhost:3000";

async function add() {
  try {
    await fetch(URL + "/animals", {
      mode: "no-cors",
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        type: type.value,
        name: name.value,
        age: age.value,
        description: description.value,
        image_url: image_url.value,
      }),
    });
  } catch (error) {
    console.log(error);
  }
}
</script>

<template>
  <div class="flex flex-col">
    <a class="text-center" href="/">AnimalShelter</a>
    <input type="text" placeholder="type" v-model="type" class="border" />
    <input type="text" placeholder="name" v-model="name" class="border" />
    <input type="text" placeholder="age" v-model="age" class="border" />
    <input
      type="text"
      placeholder="image url"
      v-model="image_url"
      class="border"
    />
    <input
      type="text"
      placeholder="description"
      v-model="description"
      class="border"
    />
    <button @click="add">Добавить</button>
  </div>
</template>
