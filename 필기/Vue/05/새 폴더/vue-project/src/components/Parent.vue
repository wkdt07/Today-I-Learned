<template>
    <div>
        <ParentChild my-msg="message" 
        :dynamic-props="name" 
        @some-event="someCallback"
        @emit-args="getNumber"
        @update-name="updateName"
        /> 
        <ParentItem 
            v-for="item in items"
            :key="item.id"
            :my-prop="item"
        />

    </div>
</template>

<script setup>
import ParentChild from './ParentChild.vue';
import ParentItem from './ParentItem.vue';
import {ref} from 'vue'

const name = ref('Alice')
const updateName=function(){
    name.value = 'Bella'
}
const items = ref([
    {id:1,name:"사과"},
    {id:2,name:'바나나'},
    {id:3,name:'딸기'},

])
const getNumber=function(...args){
    console.log(args)
    console.log(`ParentChild가 전달한 ${args}를 수신했어요.`)
}

// 자식으로부터 데이터를 받았으니 이제 그에 대한 반응을 parent가 해줘야한다.
const someCallback=function(){
    console.log('ParentChild가 발신한 이벤트를 수신했어요.')
}
</script>

<style scoped>

</style>