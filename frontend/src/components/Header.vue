<script>
export default {
  methods: {
    changeText() {
      this.$emit('change-text', 'Новая надпись');
    }
  }
}
</script>
<template>
  <header
    class="z-10 fixed w-full flex flex-col px-[30vmin] bg-black/50 backdrop-blur"
  >
    <div class="flex justify-between text-white h-16 items-center">
      <a href="/" class="text-lg">AnimalShelter</a>
      <div class="flex gap-8">
        <a href="/catalog" class="nav-item">Наши питомцы</a>
        <a href="/donations" class="nav-item">Пожертвования</a>
        <a href="/about" class="nav-item">О нас</a>
        <a href="/registration" class="nav-item">Вход</a>
      </div>
    </div>
  </header>
</template>

<style scoped>
.nav-item, .text-lg{
  position: relative;
  text-decoration: none;
  transition:color 0.3s linear;
}

.nav-item::before{
  content: "";
  position: absolute;
  display: block;
  height: 2px;
  left:0;
  bottom:0;
  width: 100%;
  background: bisque;
  transform: scaleX(0);
  transition: transform 0.3s ease;
}
.nav-item:hover, .text-lg:hover{
  color:bisque;
  /*text-decoration: underline;
  text-underline-offset: 4px;*/
}

.nav-item:hover::before{
  transform: scaleX(1);
}

</style>