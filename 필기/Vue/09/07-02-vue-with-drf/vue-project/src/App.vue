<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'ArticleView'}">Articles</RouterLink><hr>
      <RouterLink :to="{ name: 'SignUpView'}">SignUpPage</RouterLink><hr>
      <RouterLink :to="{ name: 'LogInView'}">LogInPage</RouterLink><hr>
      
      <button v-if="store.isLogin" @click.prevent="logOut">로그아웃</button>
      
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useCounterStore } from './stores/counter';
import { useRouter } from 'vue-router';
const store = useCounterStore()
const router = useRouter()
const logOut=function(){
  store.logOut()
  router.push({name:'LogInView'})
}
</script>

<style scoped>
</style>
