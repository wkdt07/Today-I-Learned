<template>
    <div>
        <TodoListItem
        v-for="todo in store.todos"
        :key="todo.id"
        :todo="todo" 
        />

        <!-- :todo는 props -->
    </div>
</template>

<script setup>
import TodoListItem from './TodoListItem.vue';
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
</script>

<style scoped>

</style>