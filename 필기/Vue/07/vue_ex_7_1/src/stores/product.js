import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import axios from 'axios'
export const useProductStore = defineStore('product', () => {
    // const products = ref([
    //     {id:1, title:'Product1' ,body:'asfgagsg'},
    //     {id:2, title:'Product2' ,body:'bsfgafsagsg'},
    //     {id:3, title:'Product3' ,body:'csfgagsg'},


    // ])
    const products = ref([]) 

    const fetchProducts=function(){
    axios({
        method:'get',
        url:'https://jsonplaceholder.typicode.com/posts'
    }).then((response)=>{
        console.log(response)
        products.value =response.data
        console.log(products.value)
    })
    .catch((error)=>{
        console.log(error)
    })
}

    const productCount = computed(()=>{
        return products.value.length
    })

    const deleteProduct = function(productId){
        const index = products.value.findIndex((product)=>product.id===productId)
        products.value.splice(index,1)

    }

    return {products,productCount,deleteProduct,fetchProducts}
})
