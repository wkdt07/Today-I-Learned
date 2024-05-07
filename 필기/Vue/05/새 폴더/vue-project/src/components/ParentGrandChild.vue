<template>
    <div>
        <h2>
            {{ myMsg }}
        </h2>

        <button @click="updateName">updateName</button>
    </div>
</template>

<script setup>
defineProps({
    myMsg:String
})

const emit = defineEmits(['updateName'])

const updateName = function(){
    emit('updateName')
}
</script>
<style scoped>

</style>