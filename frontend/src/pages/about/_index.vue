<script setup>
import Header from "../../components/Header.vue";
</script>
<template>
<Header/> 
<div class="about-us">
  <div class="background-image"></div>
  <div class="background-image"></div>
  <div class="empty-block"></div>
      <div class="content">
        <div class="about-section">
          <div class="section-background"></div>
          <h2>О нас</h2>
          <p>
            Мы - команда AnimalShelter, приюта для животных, который стремится к спасению и защите бездомных животных.
            Наша миссия - обеспечить заботу, лечение и поиск новых домов для наших пушистых друзей.
          </p>
        </div>
        <div class="goal-section">
          <div class="section-background"></div>
          <h2>Наша цель</h2>
          <p>
            Наша цель - помочь каждому животному найти любящий дом и создать безопасную и поддерживающую среду для них.
            Мы также стремимся к просвещению общества о проблемах бездомных животных и необходимости их защиты.
          </p>
        </div>
        <div class="activities-section">
          <div class="section-background"></div>
          <h2>Контакты</h2>
            <p>Telegram: @AnimalShelter</p>
            <p>Телефон: +7 (123) 456-7890</p>
            <p>Email: info@animalshelter.com</p>
        </div>
      </div>
      <div class="join-us">
        <h2>Присоединяйтесь к AnimalShelter и помогите нам создать лучшую жизнь для животных!</h2>
        <button class="join-btn" @click="join">Присоединиться</button>
      </div>
      <div class="location">
        <h2>Где мы находимся</h2>
        <a href="https://yandex.ru/maps/?um=constructor%3Af0f2a4dd687fe4d0c1eef58189d6ee09f102e5772af4304f72848d96ca6d52dd&amp;source=constructorStatic" target="_blank"><img src="https://api-maps.yandex.ru/services/constructor/1.0/static/?um=constructor%3Af0f2a4dd687fe4d0c1eef58189d6ee09f102e5772af4304f72848d96ca6d52dd&amp;width=500&amp;height=300&amp;lang=ru_RU" alt="" style="border: 0; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.455); border-radius: 20px;" /></a>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AboutUs',
  }
  </script>
  
  
<style scoped>

.empty-block{
  height: 64px;
}
.about-us {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

.background-image {
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-image: url('https://www.proplan.ru/sites/default/files/styles/image_1920x767/public/2023-02/uhod%20za%20kotenkom_1920.png?itok=fgr6Yypd'); 
background-size: cover;
background-position: center;
filter: brightness(0.7) blur(8px);
z-index: -1;
}

.content {
  width: 100%;
  max-width: 1200px;
  padding: 40px;
  text-align: center;
  color: #ffffff;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.about-section,
.goal-section,
.activities-section {
  width: 100%;
  flex-basis: calc(33.333% - 40px);
  position: relative;
}

.section-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(115, 114, 112, 0.4);
  border-radius: 20px;
  
}

.about-section h2,
.goal-section h2,
.activities-section h2 {
  font-size: 32px;
  margin-bottom: 20px;
  position: relative;
}

.about-section p,
.goal-section p,
.activities-section p {
  font-size: 18px;
  line-height: 1.6;
  padding: 20px;
  position: relative;
}

@media (max-width: 767px) {
  .content {
    flex-direction: column;
    align-items: center;
  }
  
  .about-section,
  .goal-section,
  .activities-section {
    margin-bottom: 40px;
  }
}

.join-us {
  text-align: center;
  padding: 20px 0;
  color: #fff;
}

.join-us h2 {
  font-size: 24px;
  margin: 0;
  margin-bottom: 20px;
}
.join-btn {
  background-color: #8a8a8a;
  color: white;
  border: none;
  padding: 10px 40px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 18px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.join-btn:hover {
  background-color: #c4c2c2;
}
.location{
  text-align: center;
  padding: 20px 0;
  color: #fff;
}

.location h2{
  font-size: 24px;
  margin: 0;
  margin-bottom: 20px;
}

  </style>
  