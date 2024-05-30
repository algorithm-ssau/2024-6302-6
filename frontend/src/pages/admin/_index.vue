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




/* ПРОДУКТ */
import { ref } from 'vue';

const name_product = ref("");
const price_product = ref("");
const image_product = ref("");

const URL_prod = "http://localhost:5000";

async function addProduct() {
  try {
    const response = await fetch(URL_prod + "/api/products", {
      mode: "cors",
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: name_product.value,
        price: parseFloat(price_product.value),
        image: image_product.value
      }),
    });

    if (response.ok) {
      alert("Продукт успешно добавлен!");
      // Очистка полей ввода после успешного добавления продукта
      name_product.value = "";
      price_product.value = "";
      image_product.value = "";
    } else {
      console.error("Ошибка при добавлении продукта:", response.statusText);
      alert("Ошибка при добавлении продукта.");
    }
  } catch (error) {
    console.error("Ошибка при добавлении продукта:", error);
    alert("Ошибка при добавлении продукта.");
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

    

  <! -- ПРОДУКТЫ -->
  <div class="admin-panel flex flex-col p-4"> 
    <h2 class="text-center mb-4">Продукт</h2>
    <input type="text" placeholder="Название продукта" v-model="name_product" class="border p-2 mb-2" />
    <input type="text" placeholder="Цена продукта" v-model="price_product" class="border p-2 mb-2" />
    <input type="text" placeholder="URL изображения продукта" v-model="image_product" class="border p-2 mb-2" />
    <button @click="addProduct" class="bg-blue-500 text-white p-2 mt-2 rounded">Добавить продукт</button>
  </div>
</template>
