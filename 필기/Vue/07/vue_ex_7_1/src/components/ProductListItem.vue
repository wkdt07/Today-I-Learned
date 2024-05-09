<template>
    <div>
        {{ product.id }}-{{ product.title }}-{{ product.body }}
        <button 
        @click.prevent="deleteProduct(product.id)">Delete</button>
    </div>
</template>

<script setup>
defineProps({
    product:Object
})

import { useProductStore } from '@/stores/product';
const store = useProductStore()
const deleteProduct = function(productId){
    store.deleteProduct(productId)
}

</script>

<style scoped>

</style>