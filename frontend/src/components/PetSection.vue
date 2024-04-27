<template>
  <div class="h-16" />
  <div class="h-full w-full">
    <div class="h-20 flex justify-center items-center bg-orange-100">Имя - Возраст</div>
    <div class="flex flex-col">
      <div class="flex">
        <div class="p-8">
          <div class="w-72 h-80 border-2 shadow-lg rounded-xl overflow-hidden">
            <img
              class="object-cover h-full w-full"
              src="https://i.pinimg.com/736x/3c/39/6b/3c396bcea19f7e845ed39f682773214f.jpg"
            />
          </div>
          <div class="m-8">
            <a
              href="/catalog"
              class="mx-6 border rounded-full py-4 px-8 transition-all bg-orange-100 hover:bg-orange-300 hover:text-black"
            >
              Взять котика
            </a>
          </div>
        </div>
        <div class="py-8 mr-8 w-full">
            <div class="bg-orange-100 h-16 border-2  rounded-tl-xl rounded-tr-xl overflow-hidden">1</div>
            <div class="h-64 border-2 rounded-b-xl">2</div>
        </div>
    </div>
    </div>
  </div>
</template>
