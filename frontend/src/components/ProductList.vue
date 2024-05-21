
<template>
    <div class="product-list">
      <h2>Каталог продуктов</h2>
      <ul>
        <li v-for="product in products" :key="product.id">
          {{ product.name }} - {{ product.price }} $
          <button @click="addToCart(product)">Добавить в корзину</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    props: ['addToCart'],
    data() {
      return {
        products: [
          { id: 1, name: 'Продукт 1', price: 100 },
          { id: 2, name: 'Продукт 2', price: 200 },
          { id: 3, name: 'Продукт 3', price: 300 }
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  .product-list {
    width: 50%;
    padding: 20px;
  }
  </style>
  