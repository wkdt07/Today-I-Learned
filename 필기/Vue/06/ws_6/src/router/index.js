import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '/src/views/HomeView.vue';
import QuizView from '@/views/QuizView.vue'
import QuizDetail from '@/Components/QuizDetail.vue'
import AnswerView from '@/views/AnswerView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path:'/quizes',
      name:'quizes',
      component: QuizView,
      children:[{
        path:':pk',name:'detail',component:QuizDetail
      },
    ]},
    {
      path:'/quizes/:pk/:userAnswer',
      name:'answer',
      component : AnswerView
    }
    
  ]
})

export default router
