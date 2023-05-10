import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView'
import NotFound404 from '@/views/NotFound404'
import DogView from '@/views/DogView'

Vue.use(VueRouter)
const isLoggedIn = true

const routes = [
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn) {
        console.log('이미 로그인 함')
        next({ name:'home' })
      }else { // 로그인이 안 되어 있다면, 로그인 페이지로 이동
        next()
      }
    }
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView
  },


  // 위에서부터 해당하는 url을 몾찾고 여기까지 오면
  // 404로 리다이렉트 보낸다 즉 설정하지 않은 url을 잡는거니까 맨 밑에 
  {
    path: '*',
    redirect: '/404',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// // router/index.js
// router.beforeEach((to, from, next) => {
//   // console.log('to', to)
//   // console.log('from', from)
//   // console.log('next', next)

//   // 로그인 여부
//   const isLoggedIn = false

//   // 로그인이 필요한 페이지 지정
//   // const authPages = ['hello', 'about', 'home']
//   const allowAuthPages = ['login'] // 로그인 안해도 되는 페이지로 하는 방법

//   //앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
//   // const isAuthRequired = authPages.includes(to.name)
//   const isAuthRequired = !allowAuthPages.includes(to.name)  // 안해도 되는 페이지에 없다면

//   if (isAuthRequired && !isLoggedIn) {  // 로그인필요 페이지인데 로그인이 안되어 있다면
//     console.log('Login으로 이동')
//     next({name: 'login'})
//   }else {
//     console.log('to로 이동')
//     // next를 사용하지 않으면 이동이 안된다.
//     next()
//   }
// })
export default router
