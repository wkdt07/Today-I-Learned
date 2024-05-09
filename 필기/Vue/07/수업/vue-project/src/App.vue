<script setup>
// 중앙 저장소 import 
import { useCounterStore } from './stores/counter';

// const store=useCounterStore()

// // 그럼 여기 들어가는 애들은 어떻게 접근? 
// // defineStore의 리턴 값은 객체 -> 속성 접근하는것처럼 접근해도 된다


// // 1.state: 반응형 변수
// console.log(store.count)
// const newNumber=store.count + 1


// // 2.getters : computed
// console.log(store.doubleCount)


// 3.actions: 함수, state 조작, 비동기, api호출이나 다른 로직을 진행할 수 있음



//==================
import TodoForm from './components/TodoForm.vue';
import TodoList from './components/TodoList.vue';

// import { useCounterStore } from './stores/counter';

const store = useCounterStore()

</script>

<template>
 <!-- 여기서 사용? -->

 <!-- 새 변수에 담아서 사용하던가 -->
 <!-- <p>{{ newNumber }}</p> -->
 <!-- 속성으로 접근 -->
 <!-- <p>{{ store.doubleCount }}</p> -->

 <!-- // 3.actions: 함수, state 조작, 비동기, api호출이나 다른 로직을 진행할 수 있음 -->
<!-- <button @click="store.increment()">++</button>  -->

<h1>TodoProject</h1>
<h2>완료된 Todo : {{ store.doneTodosCount }}</h2>

<TodoList/>
<TodoForm/>

</template>

<style scoped>

</style>
