import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

const api_key = 'AIzaSyAe3O9nUpz_pg7hJCCsp7DXadnpHUZ5kjU'
export const useCounterStore = defineStore('search', () => {

  const userSearch=ref('')

  const results = ref([])


  const youtubeSearch = function(userSearch){
    axios({
      method : 'get',
      url: `https://www.googleapis.com/youtube/v3/search?q=${userSearch}&type=video&part=snippet&key=${api_key}`
    }).then((response)=>{
      console.log(response)

      results.value = response.data

    }).catch((error)=>{
      console.log(error)
    })
  }

  // const favorites = ref([])

  // const likes = function(id){
  //   const flag = true
  //   for(favorite in favorites){
  //     if(favorite.id === id){
  //       // 배열안에 이미 있다는 거니깐
  //       // 배열에서 제거
  //       // flag = false
  //       // break
  //     }

  //   if(flag === true){
  //     // push
  //   }
    
  //   }
  // }
  const laterVideos=ref([])

  const flag = ref(false)

  const updateVideo = function(video) {
      for(later in laterVideos){
        if(later.etag === video.value.etag){
          flag.value = true
          break
        }
    }
    if (flag) {
      const index = laterVideos.value.indexOf(video)
      // 값이 이미 배열에 있으면 제거
      laterVideos.value.splice(index, 1)
      flag.value = false
    } else {
      // 값이 배열에 없으면 추가
      laterVideos.value.push(video)
      flag.value =true
    }
  }
  return { results,userSearch,youtubeSearch,laterVideos,updateVideo,flag }
},{ persist: true })
