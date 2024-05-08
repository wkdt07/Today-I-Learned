<template>
    <div>
        <p>{{pk}}번 문제</p>
        <h2>정답 확인</h2>
        <p> {{ isCorrect ? '정답입니다!' : '오답입니다.' }} </p>
    </div>
</template>

<script setup>
import {useRoute} from 'vue-router'
import {computed} from 'vue'
const route = useRoute()

// console.log('route=',route)

const {pk,userAnswer} =route.params

const answer = route.query.answer

const isCorrect = computed(()=>
    answer===userAnswer
)
</script>

<style scoped>

</style>