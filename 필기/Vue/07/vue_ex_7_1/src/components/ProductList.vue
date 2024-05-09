<template>
    <div>
        <h1>ProductList</h1>

            <ul>

                <li v-for="product in store.products">

                    <ProductListItem
                    
                    :product="product"
                    />
                </li>
            </ul>
         
    </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';
import ProductListItem from "./ProductListItem.vue"
import { onMounted } from 'vue';

const store = useProductStore()

// 1. setup 할 때 
// store.fetchProducts()
// 얘는 템플릿쪽에 문제가 생겨도 외부로 요청


// 2. onMounted
// 조금 더 선호하는 유형

onMounted(()=>{
    store.fetchProducts()
})

</script>

<style scoped>

</style>