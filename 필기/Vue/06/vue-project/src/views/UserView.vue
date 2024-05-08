<template>
    <div>
        <h1>UserView</h1>
        <RouterLink :to="{name:'user-profile'}">Profile</RouterLink>
        <RouterLink :to="{name:'user-posts'}">Posts</RouterLink>
        <h2>{{ userId }}번 User 페이지</h2>
        <button @click="goHome">홈으로!</button>
        <hr>
        <button @click="routeUpdate">100번 유저 페이지로!</button>
        <!-- 이건 사실상 같은 페이지로 이동하는 것이다. 값만 바뀌는 거임 -->
        <RouterView/>

</div>
</template>

<script setup>
import { ref } from 'vue';
import {useRoute, useRouter,onBeforeRouteLeave,onBeforeRouteUpdate} from 'vue-router'
const route = useRoute()
const userId=ref(route.params.id) //userRoute는 Route 안의 params의 접근할 떄 사용

const router = useRouter()

const goHome=function(){
    // router.push({name:'home'})
    router.replace({name:'home'})
}
onBeforeRouteLeave((to,from)=>{
    console.log(from)
    console.log(to)

    const answer=window.confirm('정말 떠나실건가요?')
    if (answer===false){
        return false
    }
})

const routeUpdate=function(){
    router.push({name:'user',params:{id:100}})
}

onBeforeRouteUpdate((to,from )=>{
    // console.log(to)// 이걸 통해 100이라는 params가 어디에 있는지 개발자모드에서 확인 가능

    userId.value = to.params.id
})


</script>
