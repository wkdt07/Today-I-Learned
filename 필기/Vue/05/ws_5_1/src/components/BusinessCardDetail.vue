<template>
    <div class="card">
        <!-- <hr> -->
      
            <h3> 이름 : {{ propOne.name }}</h3>
            <p> 직함 : {{ propOne.title }}</p>

            <!-- 1. 전역 EMIT 객체 활용하기 -->
            <!-- <button @click="$emit('deleteCardEvent')">명함 삭제</button> -->
            <!-- 근데 이건 권장사항은 아님. 어디서 정의됐는지 확인이 안된다. -->

            <!-- 2. 함수 쓰기 -->
            <button @click="remove(propOne)">명함 삭제</button>

    </div>
</template>

<script setup>
defineProps({
    propOne:Object
})

// 부모의 이벤트를 받아와서 사용할 수 있도록 등록하는 기능
const emit = defineEmits(['removeCard'])

const remove=function(propOne){
    emit('removeCard',propOne)//인자는 여기서 보내주는거다!!!!!!
}
</script>

<style scoped>
.card{
    /* display:block; */
    flex-direction: column;
    padding:20px;
    margin: 20px;
    background-color: #f0f0f0;
    width:40%;
}
</style>