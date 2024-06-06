<template>
  <div>
    <Header />
    <div id="app" class="container">
      <div class="background"></div>
      <div class="product-container">
        <ProductList class="product-list" :addToCart="addToCart" />
      </div>
      <div class="cart-container">
        <Cart class="cart" :cartItems="cartItems" @update:cartItems="updateCartItems" />
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
    },
    updateCartItems(newCartItems) {
      this.cartItems = newCartItems;
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
.background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('https://img.freepik.com/free-vector/cute-playful-footprint-pattern-background-fauna-fun_1017-44713.jpg?t=st=1717696958~exp=1717700558~hmac=f9984bbb44cc02c31a9c7eed0e5d073f4f8dd65e8faa287a27afbcbab57226b4&w=1380'); 
  background-size: cover;
  background-position: center;
  filter: brightness(0.7) blur(8px);
  z-index: -1;
}
</style>
