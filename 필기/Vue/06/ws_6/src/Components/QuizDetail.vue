 <template>
    <div class="quiz-item">
        
        <div class="quiz-question">
            {{ quiz.pk }}번 문제.
            {{ quiz.question }}
       </div>
        <label for="answer" class="answer-label">정답 입력:</label>
        <input type="text"
         :id="quiz.pk"
         v-model="userAnswer"
         class="answer-input"
        @keyup.enter="submitAnswer(quiz)">
    </div>
 </template>
 
 <script setup>
import {useRouter} from 'vue-router'
import {ref,computed} from 'vue'
defineProps({
    quiz:Object
})

const userAnswer = ref('')
const router = useRouter() // 라우터를 사용할거다. 

// 여기선 quiz를 바로 사용할 수 없다. html 영역에서는 사용 가능
const submitAnswer=function(quiz){
    console.log(userAnswer.value)
    router.push({
        name:'answer',
        params:{
            pk:quiz.pk,
            // answer:quiz.answer,
            userAnswer:userAnswer.value
        },
        query:{
            answer:quiz.answer,
        }
    })
}



 </script>
 
 <style scoped>
 .quiz-item {
    background-color: #f9f9f9;
    border: 1px solid#ccc;
    margin: 20px 0;
    padding: 20px;
    border-radius: 10px;
}

.quiz-question {
    font-size: 18px;
    margin: 0;
}

.answer-label {
    display: block;
    font-size: 16px;
    margin-top: 16px;
}

.answer-input {
    width: calc(100%-24px);
    padding: 12px;
    border: 1px solid #ccc;
}
 </style>