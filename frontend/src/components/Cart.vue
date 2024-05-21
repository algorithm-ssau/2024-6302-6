<template>
    <div class="cart">
      <h2>Корзина</h2>
      <ul>
        <li v-for="item in cartItems" :key="item.id">
          {{ item.name }} - {{ item.price }} $
        </li>
      </ul>
      <div v-if="cartItems.length === 0">Корзина пуста</div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['cartItems']
  };
  </script>
  
  <style scoped>
  .cart {
    width: 50%;
    padding: 20px;
    background: #f9f9f9;
  }
  </style>
  