<script setup>
const type = defineModel("type");
const description = defineModel("description");
const age = defineModel("age");
const name = defineModel("name");
const image_url = defineModel("image_url");
const id = defineModel("id");

const URL = "http://localhost:3000";

const pets = ref([]);
async function fetchPets() {
  const response = await fetch("http://localhost:3000/animals");
  pets.value = await response.json();
}
await fetchPets();

async function addEntry() {
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
    await fetchPets();
  } catch (error) {
    console.log(error);
  }
}

async function findEntry() {
  try {
    const response = await fetch(URL + "/animals/" + id.value);
    const data = await response.json();
    image_url.value = data.image_url;
    type.value = data.type;
    description.value = data.description;
    age.value = data.age;
    name.value = data.name;
    id.value = data._id;
    await fetchPets();
  } catch (error) {
    console.log(error);
  }
}

async function updateEntry() {
  try {
    await fetch(URL + "/animals/" + id.value + "/update", {
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
    await fetchPets();
  } catch (error) {
    console.log(error);
  }
}

async function deleteEntry() {
  try {
    await fetch(URL + "/animals/" + id.value + "/delete");
    await fetchPets();
  } catch (error) {
    console.log(error);
  }
}

/* ПРОДУКТ */
import { ref } from "vue";

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
        image: image_product.value,
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
  <div class="flex flex-col m-4 gap-2">
    <a class="text-center" href="/">AnimalShelter</a>
    <input type="text" placeholder="id" v-model="id" class="border px-2" />
    <input type="text" placeholder="type" v-model="type" class="border px-2" />
    <input type="text" placeholder="name" v-model="name" class="border px-2" />
    <input type="text" placeholder="age" v-model="age" class="border px-2" />
    <input
      type="text"
      placeholder="image url"
      v-model="image_url"
      class="border px-2"
    />
    <input
      type="text"
      placeholder="description"
      v-model="description"
      class="border px-2"
    />
    <div class="flex gap-2 justify-evenly">
      <button
        class="border hover:text-white hover:bg-blue-500 transition px-2 py-1 w-full"
        @click="findEntry"
      >
        Найти
      </button>
      <button
        class="border hover:text-white hover:bg-blue-500 transition px-2 py-1 w-full"
        @click="addEntry"
      >
        Добавить
      </button>
      <button
        class="border hover:text-white hover:bg-blue-500 transition px-2 py-1 w-full"
        @click="updateEntry"
      >
        Обновить
      </button>
      <button
        class="border hover:text-white hover:bg-blue-500 transition px-2 py-1 w-full"
        @click="deleteEntry"
      >
        Удалить
      </button>
    </div>
  </div>
  <hr class="mx-4" />
  <div class="flex flex-wrap m-4 gap-4">
    <div v-for="pet in pets" class="border p-2">
      <div>{{ pet._id }}</div>
      <div>{{ pet.name }} - {{ pet.type }}</div>
    </div>
  </div>

  <hr class="mx-4" />

  <! -- ПРОДУКТЫ -->
  <div class="admin-panel flex flex-col p-4">
    <h2 class="text-center mb-4">Продукт</h2>
    <input
      type="text"
      placeholder="Название продукта"
      v-model="name_product"
      class="border p-2 mb-2"
    />
    <input
      type="text"
      placeholder="Цена продукта"
      v-model="price_product"
      class="border p-2 mb-2"
    />
    <input
      type="text"
      placeholder="URL изображения продукта"
      v-model="image_product"
      class="border p-2 mb-2"
    />
    <button @click="addProduct" class="bg-blue-500 text-white p-2 mt-2 rounded">
      Добавить продукт
    </button>
  </div>
</template>
