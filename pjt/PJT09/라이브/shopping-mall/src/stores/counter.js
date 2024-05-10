import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useCartStore = defineStore('cart', () => {
  
  // store에 저장되는 '반응형'변수 : state(상태)
  const products=ref([])

  // 2. 누가 getProducts를 호출해야 할까??
    // 1) store가 만들어질 때
    // 2) 실제로 데이터가 필요할 때 v
  const getProducts = function(){
    // 1. 외부에서 데이터 가져오기(axios 라이브러리)
    // axios.get(url)
    axios({
      method:'get',
      url:'https://fakestoreapi.com/products'
    }).then((response)=>{
      // console.log(response.data)
      products.value=response.data

    })
    .catch((error)=>{
      console.log(error)
    })
  }
  return { products,getProducts }
})
