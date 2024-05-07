<template>
    <div>
        <h3>{{ myProp.id }}</h3>
        <h3>{{ myProp.name }}</h3>
    </div>
</template>

<script setup>
defineProps({
    myProp:Object
})
</script>

<style scoped>

</style>