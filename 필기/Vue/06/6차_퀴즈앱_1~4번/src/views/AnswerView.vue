<template>
  <div class="answer-view">
    <div class="title-section">
      <p class="quiz-question">{{ pk }}번 문제</p>
      <h2 class="answer-title">정답 확인</h2>
    </div>
    <div class="content-section">
      <p class="result-message" :class="{ correct: isCorrect, incorrect: !isCorrect }">
        {{ isCorrect ? '정답입니다!' : '오답입니다.' }}
      </p>
      <p class="user-answer" :class="{ correct: isCorrect, incorrect: !isCorrect }">
        나의 제출 답안: {{ userAnswer }}
      </p>
      <p class="correct-answer">정답: {{ answer }}</p>
    </div>
  </div>
</template>
<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()

// console.log('route = ', route)

const { pk, answer } = route.params
const userAnswer = route.query.userAnswer

const isCorrect = computed(() => answer === userAnswer)
</script>

<style scoped>
.answer-view {
  max-width: 600px;
  margin: 30px auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
  border-radius: 10px;
  border: 1px solid rgb(219, 219, 219);
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

.title-section {
  text-align: center;
  margin-bottom: 20px;
}

.answer-title {
  font-size: 24px;
  margin: 0;
}

.quiz-question {
  font-size: 18px;
  margin: 0;
}

.user-answer,
.correct-answer {
  font-size: 16px;
  margin-top: 15px;
}

.content-section {
  background: white;
  padding: 20px;
  border-radius: 10px;
  border: 1px solid rgb(199, 199, 199);
}
.result-message {
  font-size: 18px;
  font-weight: bold;
  margin-top: 20px;
}

.correct {
  color: #007f00; /* Green for correct answers */
}

.incorrect {
  color: #ff0000; /* Red for incorrect answers */
}
</style>
