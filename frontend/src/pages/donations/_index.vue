<script setup>
import Header from "../../components/Header.vue";
</script>
<template>
<Header/> 
    <div id="app" class="container">
      <ProductList :addToCart="addToCart" />
      <Cart :cartItems="cartItems" />
    </div>
  </template>
  
  <script>
    import ProductList from "../../components/ProductList.vue";
    import Cart from "../../components/Cart.vue";
  export default {
    name: 'App',
    components: {
      ProductList,
      Cart
    },
    data() {
      return {
        cartItems: []
      };
    },
    methods: {
      addToCart(product) {
        this.cartItems.push(product);
      }
    }
  };
  </script>
  
  <style>
  .container {
    display: flex;
    justify-content: space-between;
  }
  </style>
  