<!-- 시작은 vbase-3-setup -->
<template>
    <!-- html -->
    <div>
        <p class="greeting">{{ msg }}</p>


    </div>
</template>

<script setup>
// JS
// 여기선 우리가 사용하던 setup 함수가 이미 적용되고 있음
// 그냥 여기가 setup 함수의 안이라 생각

import {ref} from 'vue' //이제 이런 식으로 갖고와라


const msg = ref('Hello')


// return {msg}
// 이제 더 이상 리턴하지 않는다

</script>


<!-- <style lang="scss" scoped> -->
<style scoped>
/* css */

.greeting{
    color:crimson
}
</style>



