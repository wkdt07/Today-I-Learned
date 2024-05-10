<template>
  <h1>나중에 볼 동영상</h1>
  <div v-if="store.laterVideos.length === 0">
    <h1>등록된 비디오 없음</h1>
  </div>
  <div v-else>
    <!-- {{ store.laterVideos }} -->
    <div v-for="item in store.laterVideos"
    style="background-color: aliceblue; border:1px black solid; margin: auto; padding: auto; text-align: center; align-items: center;">
    

      <img :src="item.snippet.thumbnails.default.url" alt="이미지 오류">
      <h3>{{ item.snippet.title }}</h3>

      <!-- {{ item }} -->
   
    </div>
  </div>
</template>

<script setup>


import { useCounterStore } from '@/stores/counter';


const store = useCounterStore()

</script>

<style scoped>

</style>