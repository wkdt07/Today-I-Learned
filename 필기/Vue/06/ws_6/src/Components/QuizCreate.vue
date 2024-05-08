<template>
    <div>
        <h2>퀴즈 생성</h2>
        <form>
            <label for="question">문제</label>
            <textarea v-model="question" required></textarea>>

            <label for="answer">답</label>
            <input type="text" v-model="answer">

            <button @click.prevent="createQuizFunc" style="background-color: blue; color: azure; text-align: center;">퀴즈 생성</button>

        </form>
    </div>
</template>

<script setup>
import {ref} from 'vue'
const emit=defineEmits(['createQuiz'])

const question=ref('')
const answer=ref('')

const createQuizFunc=function(){
    const quizInfo={
        
        question:question.value,
        answer:answer.value,
    }
    emit('createQuiz',quizInfo)
}

</script>

<style scoped>

</style>