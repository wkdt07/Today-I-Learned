<template>
  <div>
    <!-- {{ item }} -->
    <h1>it is detail</h1>
    <h2>{{ final?.snippet.title }}</h2>
    
    <iframe id="final.id" type="text/html" width="640" height="360" :src="`https://www.youtube.com/embed/${final.id.videoId}?autoplay=0`"></iframe>
    <p>{{ final.snippet.description }}</p>
    <!-- {{ laterStore.laterVideos }} -->
    <button @click="laterStore.updateVideo(final)">{{ laterStore.flag ? 'Remove from Later' : 'Add to Later' }}</button>
  </div>
    

</template>

<script setup>

import { ref } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter';


const route = useRoute()
const etag = route.params.id
const kw = route.params.kw
const api_key = 'AIzaSyAe3O9nUpz_pg7hJCCsp7DXadnpHUZ5kjU'
const results = ref([])
const final = ref({})
const youtubeSearch = function(userSearch){
  axios({
    method: 'get',
    url: `https://www.googleapis.com/youtube/v3/search?q=${userSearch}&type=video&part=snippet&key=${api_key}`
  }).then((response)=>{
    console.log(response)
    results.value = response.data.items // 데이터 할당
    findResultByEtag() // 데이터가 도착한 후에 실행되어야 함
  }).catch((error)=>{
    console.log(error)
  })}

const findResultByEtag = () => {
  for (const result of results.value) {
    if (result.etag === etag) {
      final.value = result
      break // 찾았으면 반복 중지
    }
  }
}

youtubeSearch(kw)


const laterStore = useCounterStore()




</script>

<style scoped>

</style>