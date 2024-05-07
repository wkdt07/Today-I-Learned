<!-- 실질적으로 공닥하는 곳 -->

<template>
    <!-- <createCardForm
    @create-card-func="createCardFunc"
    /> -->
    <!-- 이렇게 해도 된다. 사실 이렇게 하는게 정석 -->
    <div v-if="computedLength">
        <h1>보유 명함 목록</h1>
        <p>현재 보유중인 명함수 : {{ computedLength }}</p>
        
        <div class="card">

            <BusinessCardDetail
            v-for="businessCard in businessCards"
            :key="businessCard.id"
            :propOne="businessCard"
            @remove-card="removeCard"
            />
            <!-- 자바스크립트 쪽 변수라는걸 알려주는게 바인딩 (:) -->
        </div>
    </div>
    <p v-else>
        아직 명함이 없습니다.</p>
</template>

<script setup>
import {computed, ref, watch} from 'vue'
import BusinessCardDetail from "@/components/BusinessCardDetail.vue"
import createCardForm from './CreateCardForm.vue';
const businessCards =ref([
    {id:1,name:'일론 머스크',title:'테슬라 테크노킹'},
    {id:2,name:'래리 엘리슨', title:'오라클 창업주'},
    {id:3,name:'빌 게이츠', title:'마이크로소프트 공동창업주'},
    {id:4,name:'래리 페이지', title:'구글 공동창업주'},
    {id:5,name:'세르게이 브린', title:'구글 공동창업주'},
])

// 왜 computed 썼을까?
// 캐시 기능 때문에 단순 계산은 가장 효율적
const computedLength = computed(()=>{
    return businessCards.value.length
})
const props = defineProps({
  newCardInfo: Object
})
// watch :  
//특정 변수의 변화에 따라 다른 변수를 수정하는 등 사이드 이펙트가 있을 때
watch(() => props.newCardInfo, (newCard) => {
  businessCards.value.push(newCard)
})

const removeCard = function(businessCard){
    const index = businessCards.value.findIndex(card => card.id === businessCard.id);
    if (index !== -1) {
        businessCards.value.splice(index, 1);
    }
}
// const createCardFunc= function(name,title){
//     console.log(name,title)
//     businessCards.value.push({id:computedLength,name:name,title:title})
// }
// 이렇게 해도 된다. 사실 이렇게 하는게 정석


// ctrl+alt+아래
</script>

<style scoped>
.card{
    /* background-color: #f0f0f0; */
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    /* text-align: center;
    align-items: center;
    margin: 10px;
    padding: 10px; */
    
}
</style>