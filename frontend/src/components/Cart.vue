<template>
  <div class="cart">
    <h2 class="cart-title">Корзина</h2>
    <ul>
      <li v-for="item in cartItems" :key="item.id">
        {{ item.name }} - {{ item.price }} $
      </li>
    </ul>
    <div v-if="cartItems.length === 0" class="empty-cart">Корзина пуста</div>
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
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
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

.cart li {
  font-size: 16px;
  margin-bottom: 10px;
}

.empty-cart {
  font-size: 18px;
  color: #999;
  text-align: center;
  margin-top: 20px;
}
</style>
