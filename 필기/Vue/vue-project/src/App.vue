<script setup>
// import HelloWorld from './components/HelloWorld.vue'
// import TheWelcome from './components/TheWelcome.vue'

import MyComponent from './components/MyComponent.vue'; // 내가 만들어놓은 MyComponent.vue를 불러오기
// import MyComponent from '@/components/MyComponent.vue'
// 이렇게 써도 된다. 


import MyComponentItem from './components/MyComponentItem.vue';
</script>



<template>
  <header>

    <div >
      <h1>App.vue</h1>
      <MyComponent/>
      <MyComponentItem/>
      <MyComponentItem/>
      <MyComponentItem/>

    </div>
  </header>

</template>

  <style scoped>
  header {
    line-height: 1.5;
  }
  
  .logo {
    display: block;
    margin: 0 auto 2rem;
  }
  
  @media (min-width: 1024px) {
    header {
      display: flex;
      place-items: center;
      padding-right: calc(var(--section-gap) / 2);
    }
  
    .logo {
      margin: 0 2rem 0 0;
    }
  
    header .wrapper {
      display: flex;
      place-items: flex-start;
      flex-wrap: wrap;
    }
  }
  </style>
