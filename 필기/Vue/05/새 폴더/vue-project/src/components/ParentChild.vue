<template>
    <div>
        <p>{{ myMsg }}</p>
        <ParentGrandChild :my-msg="myMsg"
        @update-name="updateName"
        />
        <p>{{ dynamicProps }}</p>
        <button @click="$emit('someEvent')">클릭</button>
        <hr>
        <button @click="buttonClick">defineEmits</button>
        <!-- 위의 2개가 같은거임. -->
        <hr>
        <button @click="emitArgs">추가인자 전달</button>    

    </div>
</template>

<script setup>

import ParentGrandChild from '@/components/ParentGrandChild.vue'

const emit = defineEmits(['someEvent','emitArgs','updateName'])


const updateName = function(){
    emit('updateName')
} // 여기서도 한 번 더 올린다. 

const emitArgs = function(){
    emit('emitArgs',1,2,3)
}
const buttonClick = function(){
    emit('someEvent')
}

// 내려받은 props를 선언해야 사용할 수 있음

// 1. 배열식
// defineProps(['myMsg'])//Parent에서 my-msg로 선언하고(HTML), Script(JS)에서 myMsg로 사용
// 이제 이 파일에서 myMsg 사용 가능


// 2. 객체식
defineProps({
    myMsg:String,
    dynamicProps:String
})


// const props = defineProps({
//     myMsg:String
// })

// console.log(props)//{myMsg:'message'}라는 객체가 나옴. 

// console.log(props.myMsg) // 'message'
</script>

<style scoped>

</style>