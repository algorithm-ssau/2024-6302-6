<template>
  <div class="w-72 h-80 border-2 shadow-lg rounded-xl overflow-hidden">
    <div class="relative h-full w-full flex flex-col-reverse">
      <div class="z-[1] absolute w-full h-full overflow-hidden">
        <img class="object-cover h-full w-full" :src="image" />
      </div>
      <div
        class="z-[2] absolute bottom-0 w-full h-1/3 overflow-hidden bg-gradient-to-t from-white to-transparent"
      />
      <div
        class="z-[3] h-16 w-full flex backdrop-blur bg-white/30 items-center"
      >
        <p class="w-full truncate pl-4">{{ name }}</p>
        <div class="aspect-square h-full flex justify-center items-center">
          <a
            :href="href"
            class="bg-yellow-300 aspect-square h-2/3 rounded-full flex justify-center items-center"
          >
            &rarr;
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps(["name", "image", "href"]);
</script>
