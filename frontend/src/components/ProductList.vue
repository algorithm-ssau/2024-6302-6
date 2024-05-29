<template>
  <div class="product-list">
    <h2 class="catalog-title">Каталог продуктов</h2>
    <div class="products-container">
      <div class="product-card" v-for="product in products" :key="product._id">
        <img :src="product.image" :alt="product.name" class="product-image">
        <h3>{{ product.name }}</h3>
        <p>{{ product.price }} $</p>
        <button @click="addToCart(product)">Добавить в корзину</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['addToCart'],
  data() {
    return {
      products: []
    };
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get('http://localhost:5000/api/products');
        this.products = response.data;
      } catch (error) {
        console.error("There was an error fetching the products:", error);
      }
    }
  },
  created() {
    this.fetchProducts();
  }
};
</script>

<style scoped>
.product-list {
  width: 70%;
  margin: 0 auto;
  padding: 20px;
  text-align: center; /* Центрируем текст */
}

.catalog-title {
  font-size: 24px;
  color: #333; /* Цвет текста */
  margin-bottom: 20px; /* Отступ снизу */
}

.products-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.product-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  padding: 20px;
  text-align: center;
  width: 200px;
}

.product-card h3 {
  margin: 10px 0;
  font-size: 18px;
}

.product-card p {
  margin: 10px 0;
  font-size: 16px;
  color: #333;
}

.product-card .product-image {
  width: 100%;
  height: auto;
  border-radius: 10px;
}

.product-card button {
  background-color: #42b983;
  border: none;
  border-radius: 5px;
  color: white;
  cursor: pointer;
  font-size: 14px;
  padding: 10px 20px;
  transition: background-color 0.3s ease;
}

.product-card button:hover {
  background-color: #369a75;
}
</style>
