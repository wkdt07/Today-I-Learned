import { createRouter, createWebHistory, createWebHashHistory } from 'vue-router'
import HomeView from '/src/views/HomeView.vue';
import QuizView from '../views/QuizView.vue';
import AnswerView from '../views/AnswerView.vue';


const router = createRouter({
  // 해시 모드
  // 히스토리 모드: 일반적으로 우리가 쓰는 URL 방식
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/quiz',
      name: 'quiz',
      // lazy loading 기법이 적용
      // loading 이 느린 페이지가 존재해서
      // 따로 불러와야 할 때 사용함
      // component: () => import('../views/QuizView.vue')
      component: QuizView
    },
    {
      path: '/answer/:pk/:answer',
      name: 'answer',
      component: AnswerView
    }
  ]
})

export default router
