<template>
    <div>
        <h3>TodoForm</h3>
        <form @submit.prevent="createTodo(todoText)" ref="formElem">
            <input type="text" v-model="todoText">
            <input type="submit" value="create">

        </form>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
const todoText = ref('')


const formElem=ref(null)

const createTodo=function(todoText){
    store.addTodo(todoText)
    formElem.value.reset() //form에 입력한 값과 동기화 하고, 이벤트 발생하면 리셋
}

</script>

<style scoped>

</style>