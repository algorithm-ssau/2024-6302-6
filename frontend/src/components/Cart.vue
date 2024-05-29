<template>
  <div class="cart" v-if="cartItems.length > 0">
    <h2 class="cart-title">Корзина</h2>
    <ul>
      <li v-for="item in cartItems" :key="item.id" class="cart-item">
        {{ item.name }} - {{ item.price }} $
      </li>
    </ul>
    <button @click="makeOrder" class="order-button">Сделать заказ</button>
  </div>
  <div v-else class="empty-cart">Корзина пуста</div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['cartItems'],
  methods: {
    async makeOrder() {
      try {
        const orderData = {
          items: this.cartItems
        };
        await axios.post('http://localhost:5000/api/cart', orderData);
        alert('Заказ успешно оформлен!');
      } catch (error) {
        console.error('Ошибка при оформлении заказа:', error);
      }
    }
  }
};
</script>

<style scoped>
.cart {
  width: 50%;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
  animation: appear 0.5s ease-in-out;
}

.cart-title {
  font-size: 24px;
  color: #333;
  margin-bottom: 20px;
}

.cart ul {
  list-style: none;
  padding: 0;
}

.cart-item {
  font-size: 16px;
  margin-bottom: 10px;
  border-bottom: 1px solid #ccc;
  padding-bottom: 5px;
}

.order-button {
  background-color: #42b983;
  border: none;
  border-radius: 5px;
  color: white;
  cursor: pointer;
  font-size: 14px;
  padding: 10px 20px;
  transition: background-color 0.3s ease;
}

.order-button:hover {
  background-color: #369a75;
}

.empty-cart {
  font-size: 18px;
  color: #999;
  text-align: center;
  margin-top: 20px;
}

@keyframes appear {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
