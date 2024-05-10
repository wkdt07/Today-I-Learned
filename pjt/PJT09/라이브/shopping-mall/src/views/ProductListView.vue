<template>
  <div>
    <h1>전체 상품 목록</h1>
    <div v-for="product in cartStore.products">
    <p>상품명: {{ product.title }}</p>
    <p>설명 ㅣ {{product.detail }}</p>
    </div>
  </div>
</template>

<script setup>
import {useCartStore} from '@/stores/counter'
import { onMounted } from 'vue';
const cartStore=useCartStore()

// cartStore.getProducts()

onMounted(()=>{
  cartStore.getProducts()
})

items = store.items

v-for="item in items"

id = item.id
url = `www.youtube.com/${id}`
</script>

<style scoped>

</style>