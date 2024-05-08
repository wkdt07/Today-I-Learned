<template>
  <div class="quiz-app">
    <div class="app-header">
      <h1 class="app-title">Quiz 퀴즈</h1>
    </div>
    <div class="app-description">
      <p>
        여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!
      </p>
    </div>
    <nav class="app-nav">
      <RouterLink to="/" class="nav-link">Home</RouterLink> | 
      <RouterLink to="/quiz" class="nav-link">Quiz</RouterLink> | 
    </nav>
  </div>
  <RouterView />
</template>

<script setuo>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>
.quiz-app {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
  text-align: center;
}

.app-header {
  background-color: #ff922b;
  color: white;
  padding: 20px;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.app-title {
  font-size: 28px;
  margin: 0;
}

.app-description {
  padding: 20px;
  font-size: 16px;
  background-color: white;
  border: 1px solid #ddd;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
}


.app-nav {
  margin-top: 30px;
  background-color: #333;
  padding: 10px 0;
  color: white;
}

.nav-link {
  color: white;
  text-decoration: none;
  padding: 10px 20px;
  transition: background-color 0.3s;
}
</style>
