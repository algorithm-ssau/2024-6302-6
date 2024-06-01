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
        <a href="/catalog" class="hover:underline underline-offset-4">
          Наши питомцы
        </a>
        <a href="/donations" class="hover:underline underline-offset-4">Пожертвования</a>
        <a href="/about" class="hover:underline underline-offset-4">
          О нас
        </a>
        <a href="/registration" class="hover:underline underline-offset-4">
          Вход
        </a>
        
      </div>
    </div>
  </header>
</template>
