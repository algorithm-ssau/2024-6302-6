<template>
  <div>
    <Header />
    <div id="app" class="container">
      <div class="product-container">
        <ProductList class="product-list" :addToCart="addToCart" />
      </div>
      <div class="cart-container">
        <Cart class="cart" :cartItems="cartItems" />
      </div>
    </div>
  </div>
</template>

<script>
import Header from "../../components/Header.vue";
import ProductList from "../../components/ProductList.vue";
import Cart from "../../components/Cart.vue";

export default {
  name: 'App',
  components: {
    Header,
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
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}

#app {
  display: flex;
  flex: 1;
}

.container {
  display: flex;
  justify-content: space-between;
  width: 100%;
  height: 100%;
}

.product-container,
.cart-container {
  margin-top: 60px;
  flex: 1;
  display: flex; /* Добавьте эту строку */
  flex-direction: row; /* Добавьте эту строку */
}

.product-list,
.cart {
  flex: 1;
}

.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: white;
  z-index: 1000;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
</style>
