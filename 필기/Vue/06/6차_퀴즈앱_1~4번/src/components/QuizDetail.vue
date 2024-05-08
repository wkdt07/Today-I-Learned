<template>
  <div class="quiz-item">
    <h5 class="quiz-question">{{ quiz.pk }}번 문제. {{ quiz.question }}</h5>
    <label class="answer-label" for="answer">정답 입력</label>
    <input
      type="text"
      class="answer-input"
      v-model="userAnswer"
      @keyup.enter="submitAnswer(quiz)"
    >
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue';

defineProps({
  quiz: Object
})

const router = useRouter()
const userAnswer = ref('')

const submitAnswer = function(quiz) {
  // console.log(userAnswer.value)
  router.push({
    name: 'answer',
    params: {
      pk: quiz.pk,
      answer: quiz.answer
    },
    query: {
      userAnswer: userAnswer.value
    }
  })
}
</script>

<style scoped>
.quiz-item {
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin: 20px;
  padding: 20px;
}

.quiz-question {
  font-size: 18px;
  margin: 0;
}

.answer-label {
  display: block;
  margin-top: 16px;
}

.answer-input {
  width: calc(100% - 24px);
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-top: 8px;
}
</style>