<script setup>
import Header from "../../components/Header.vue";
import { ref } from "vue";
    const username = defineModel("username");
    const email = defineModel("email");
    const password = defineModel("password");
    const usersystem = defineModel("usersystem");
    const URL = "http://localhost:3000";
    const persons = ref([]);    

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
            usersystem: usersystem.value
          }),
        });
      } catch (error) {
        console.log(error);
      }
    };

    async function get_2() {
      const response = await fetch(URL + "/users/:name");
      persons.value = await response.json();
      console.log("Вывод результата в консоль: ");
      console.log(persons.value[0].username);
    };

    get_2();


    

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
        <template v-for="person in persons">
          <p v-if="person.username === username">
            <button @click="">Войти</button>
          </p>          
        </template>        
        <button v-if="persons.length === 0 || !persons.some(person => person.username === username)" @click="add">Зарегистрироваться</button>        
        <div v-if="persons.length > 0">
          <template v-for="person in persons">
            <p v-if="person.username === username">Человек под именем {{ person.username }} уже существует</p>          
          </template>
        </div>
      </form>
    </div>    
  </template>
    
  <style scoped>
    registration-form {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
  }

  .registration-form h2 {
    text-align: center;
  }

  .registration-form form {
    display: flex;
    flex-direction: column;
  }

  .registration-form label {
    margin-top: 10px;
  }

  .registration-form input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
  }

  .registration-form button {
    padding: 8px 15px;
    margin-top: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 3px;
    cursor: pointer;
  }

  .registration-form button:hover {
    background-color: #0056b3;
  }

  /* Стили для сообщений об ошибке или успешной регистрации */
  .registration-form p {
    margin-top: 10px;
  }

  /* Стили для кнопки "Войти" */
  .registration-form button.login-button {
    background-color: #28a745;
  }

  .registration-form button.login-button:hover {
    background-color: #218838;
  }


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
