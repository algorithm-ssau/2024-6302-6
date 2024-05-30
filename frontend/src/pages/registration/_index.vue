<script setup>
import Header from "../../components/Header.vue";
const username = defineModel("username");
    const email = defineModel("email");
    const password = defineModel("password");
    const URL = "http://localhost:3000";

    async function add() 
    {
      try {
        await fetch(URL + "/users", {
          mode: "no-cors",
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: username.value,
            email: email.value,
            password: password.value,
          }),
        });
      } catch (error) {
        console.log(error);
      }
    }
</script>
<!-- template - username - email - password -->
  <template>
    <Header/>
    <div class="registration-form">
      <h2>Регистрация</h2>
      <form @submit.prevent="registerUser">
        <label for="username">Имя пользователя:</label>
        <input type="text" id="username" v-model="username" required>
  
        <label for="email">Email:</label>
        <input type="text" id="email" v-model="email" required>
  
        <label for="password">Пароль:</label>
        <input type="text" id="password" v-model="password" required>
        <button @click="add">Зарегистрироваться</button>
      </form>
    </div>
  </template>
    
  <style scoped>
  .registration-form {
    padding-top: 140px;
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
