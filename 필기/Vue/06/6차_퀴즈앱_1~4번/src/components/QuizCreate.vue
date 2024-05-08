<template>
  <div class="quiz-create">
    <h2>퀴즈 생성</h2>
    <form class="quiz-form" @submit.prevent="createQuiz">
      <label class="form-label" for="question">문제</label>
      <textarea 
        class="form-input"
        v-model="newQuiz.question" 
        required
      >
      </textarea>
      <label class="form-label"  for="answer">답안</label>
      <input type="text" class="form-input" v-model="newQuiz.answer" required>
      <button class="submit-button">퀴즈 생성</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const newQuiz = ref({
  question: '',
  answer: ''
})

const emit = defineEmits(['createQuiz'])

const createQuiz = function() {
  emit('createQuiz', newQuiz.value)
  newQuiz.value.question = ''
  newQuiz.value.answer = ''
}
</script>

<style scoped>
.quiz-create {
  background-color: #f9f9f9;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  padding: 20px;
  border-radius: 10px;
}

.quiz-form {
  display: flex;
  flex-direction: column;
}

.form-label {
  margin-top: 10px;
}

.form-input {
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-top: 5px;
  padding: 10px;
}

.submit-button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px;
  margin-top: 15px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #0a4580;
}
</style>