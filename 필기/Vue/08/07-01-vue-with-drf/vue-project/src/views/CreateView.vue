<template>
  <div>
    <form @submit.prevent="createArticle">
      <label for="title">제목:</label>
      <input type="text" id="title" v-model.trim="title">
      <br>
      <label for="content">내용:</label>
      <textarea type="text" id="content" v-model.trim="content"></textarea>
      <br>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';
// import router from '@/router';
const router=useRouter()

const createArticle=function(){
  axios({
    method:'post',
    url:`${store.API_URL}/api/v1/articles/`,
    data:{
      title:title.value,
      content:content.value
    },
  }
  ).then(()=>{
    router.push({name:'ArticleView'}) //다시 ArticleView로 나가기 위해.
  }).catch(err=>console.log(err))
}

const store= useCounterStore()

const title=ref(null)
const content=ref(null)
</script>

<style>

</style>
