<template>
    <div>
        
        <form >
           <label for="name">이름</label>
            <input type="text" value="이름" v-model="name" >
            
            <label for="title">직함</label>
            <input type="text" value="직함" v-model="title">
            
            <button @click.prevent="createCardFunc">명함 추가</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';

// emit은 '이벤트'를 알리는 것
const emit = defineEmits(['createCardEvent'])



// 담아갈 그릇 만들기
const name = ref('')
const title=ref('')

const createCardFunc=function(){
    console.log(name.value,title.value)  
    const cardInfo={
        id:Date.now(),
        name:name.value,
        title:title.value

    }
    emit('createCardEvent',cardInfo)// 얘 이벤트 이름은 부모로부터 가져오는 것
    name.value=''
    title.value=''
}
</script>

<style scoped>

</style>