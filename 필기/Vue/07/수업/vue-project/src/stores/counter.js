import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // const count = ref(0)
  // const doubleCount = computed(() => count.value * 2)
  // function increment() {
  //   count.value++
  // }

  let id = 0
  const todos = ref([
    {id:id++,text:'할일1',isDone:false},
    {id:id++,text:'할일2',isDone:false}
  ])

  const addTodo=function(todoText){
    todos.value.push(
      {
        id:id++,
        text:todoText,
        isDone:false
      }
    )
  }

  const deleteTodo=function(todoId){
    // console.log('delete')
    const index=todos.value.findIndex((todo)=>todo.id===todoId)
    todos.value.splice(index,1)
    console.log(todos.value)
  }

  const updateTodo = function(todoId){
    
    // 전달 받은 todoId(수정대상)을 활용
    // todos 배열을 순회하면서 id가 일치하면 isDone을 반대로 변경 -> map 함수 활용
    // 변경된 새로운 배열을 반환
    
    todos.value = todos.value.map((todo)=>{
      // console.log(todo)
      if (todo.id===todoId){
        todo.isDone =! todo.isDone
      }
      // console.log(todo)
      return todo
    })
  }

  const doneTodosCount = computed(()=>{
    const doneTodos = todos.value.filter((todo) => todo.isDone)
    return doneTodos.length
  })
  return { todos,addTodo,deleteTodo,updateTodo,doneTodosCount }
})
