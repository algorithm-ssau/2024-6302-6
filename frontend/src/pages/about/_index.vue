<script setup>
import Header from "../../components/Header.vue";
</script>
<template>
<Header/>    
    <div class="about-us">
        <div class="background-image"></div>
      <div class="background-image"></div>
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
        </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AboutUs',
  }
  </script>
  
  <style scoped>
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
  }
  
  .about-section p,
  .goal-section p,
  .activities-section p {
    font-size: 18px;
    line-height: 1.6;
    margin-bottom: 40px;
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
}
  </style>
  