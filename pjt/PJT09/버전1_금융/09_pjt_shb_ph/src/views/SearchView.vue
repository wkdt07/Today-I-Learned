<template>
  <div>
    <h1>It is Search</h1>
    <form @submit.prevent="ourSearch(searchStore.userSearch)">
      <!-- @submit="ourSearch()" -->
    <input type="text" placeholder="검색어를 입력하세요." v-model="searchStore.userSearch">
    <input type="submit" value="찾기">
    </form>
    <div v-for="item in searchStore.results.items"
    style="background-color: aliceblue; border:1px black solid; margin: auto; padding: auto; text-align: center; align-items: center;">
    <RouterLink :to="{name:'detail',params:{'id':item.etag,'kw':keyword}}">
      <p>{{ keyword}}</p>
      <img :src="item.snippet.thumbnails.default.url" alt="이미지 오류">
      <h3>{{ item.snippet.title }}</h3>

      <!-- {{ item }} -->
    </RouterLink>
</div> 
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted,reactive,ref,watch } from 'vue';
import axios from 'axios'
import { RouterLink, RouterView } from 'vue-router'


const searchStore = useCounterStore()

const keyword = ref('ssafy')
// const result = ref(searchStore.result)

const ourSearch = function(kw){
  keyword = kw
  searchStore.youtubeSearch(kw)
  // console.log(result.value)
}

onMounted(()=>{


  searchStore.youtubeSearch('ssafy')
  // axios(
  //   {
  //     method : 'get',
  //     url : 'https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=6&regionCode=kr&key=AIzaSyAmcDjxq-FTH-nvtSfz_89lV3ruYfQCMg4'
  //   }
  // ).then((response)=>{
  //   // console.log(response)
  //   result.value = response.data
  //   // console.log(result.value)
  // }).catch((error)=>{   
  //   result.value=error 
  //   // console.log(result.value)
  // })

})
// watch(() => searchStore.result, (newValue, oldValue) => {
//   // searchStore.result가 변경될 때마다 result 업데이트
//   result.value = newValue})


// const ourSearch = function(userSearch){
//   searchStore.youtubeSearch(userSearch)
// }

</script>

<style>

</style>

