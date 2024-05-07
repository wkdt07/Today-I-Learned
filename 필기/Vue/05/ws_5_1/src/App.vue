
<script setup>
import BusinessCard from './components/BusinessCard.vue';
import CreateCardForm from './components/CreateCardForm.vue';
import { ref } from 'vue';

const newCardInfo=ref({})
const updateCard = function(cardInfo){
  console.log('update Card!')
  newCardInfo.value=cardInfo
}
</script>

<template>
  <div class="app">
    
    <header class="header">
      <h1>명함 관리 페이지</h1>
    </header>
    
    <main class="main">
      <CreateCardForm
      @create-card-event="updateCard"
      />
      <!-- 여기에 있는 create-card-event를 자식에서 emit으로 가져가는 것 -->
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
      <BusinessCard
      :new-card-info="newCardInfo"/>
    </main>
    
    <footer class="footer">
      &copy; 2024 Business Cards
    </footer>
  </div>
  </template>

<style scoped>

/* body{
  margin: 0px;
} */

.app {
  text-align: center;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
.header {
  background-color: blue;
  color:white;
  padding: 20px;
  
}
.main{
  /* flex-grow: 1; */
}
.article{
  flex-grow: 1;
}

.footer{
  background-color: #f0f0f0;
  width: 100%;
  padding: 10px;
}
</style>
