<script setup>
import Header from "../../components/Header.vue";
</script>

<template>
<Header/>
    <div class="registration-form">
      <h2>Регистрация</h2>
      <form @submit.prevent="registerUser">
        <label for="username">Имя пользователя:</label>
        <input type="text" id="username" v-model="username" required>
  
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
  
        <label for="password">Пароль:</label>
        <input type="password" id="password" v-model="password" required>
  
        <button type="submit">Зарегистрироваться</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: ''
      };
    },
    methods: {
      registerUser() {
        // Здесь можно добавить логику для регистрации пользователя, например, отправку данных на сервер
        console.log('Регистрация пользователя:', this.username, this.email, this.password);
      }
    }
  };
  </script>
  
  <style scoped>
  .registration-form {
    max-width: 400px;
    margin: 0 auto;
  }
  
  form {
    display: flex;
    flex-direction: column;
  }
  
  label {
    margin-top: 10px;
  }
  
  input {
    padding: 5px;
    margin-top: 5px;
  }
  
  button {
    margin-top: 10px;
    padding: 8px 15px;
    background-color: #007bff;
    color: white;
    border: none;
  }
  </style>
