import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '../views/UserView.vue'
import UserProfile from '@/components/UserProfile.vue'
import UserPosts from '@/components/UserPosts.vue'
import UserHome from '@/components/UserHome.vue'
import LoginView from '@/views/LoginView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path:'/user/:id',
      // name:'user',
      component: UserView,
      beforeEnter:(to,from)=>{
        console.log(to)
        console.log(from)
      },
      children:[
        {path:'',name:'user',component:UserHome},
        {path:'profile',name:'user-profile',component:UserProfile},
        {path:'posts',name:'user-posts',component:UserPosts}
      ]
    },
    {
      path:'/login',
      name:'login',
      component:LoginView,
      beforeEnter:(to,from)=>{
        console.log('beforeEnter')
        const isAuthenticated = true // 얘도 일단은 이렇게 막아두자. 
        if (isAuthenticated===true) {
          console.log('이미 로그인 상태입니다.')
          return {name:'home'}
        }
      }
    }
  ]
})

// 전역가드
// router.beforeEach((to,from)=>{
//   console.log(to)
//   console.log(from)
// })// 전역가드는 위치랑 상관 없이 url이 변경될 떄마다 호출되는 함수이다. 

// 예시: 로그인 되어있는지 아닌지를 확인할 수 있다.
router.beforeEach((to,from)=>{
  const isAuthenticated = true

  if (!isAuthenticated && to.name !== 'login'){ // 1. 로그인이 안 되어있고, 2. 지금 가는 곳이 로그인 화면이 아니면
    console.log('로그인이 필요합니다.')
    return {name:'login'}
  }
})

export default router
