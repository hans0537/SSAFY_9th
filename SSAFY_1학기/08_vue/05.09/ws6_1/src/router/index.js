import Vue from 'vue'
import VueRouter from 'vue-router'
import AllTodoPage from '../views/AllTodoPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'all',
    component: AllTodoPage
  },
  {
    path: '/today',
    name: 'today',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/TodayTodoPage.vue')
  },
  {
    path: '/important',
    name: 'important',
    component: () => import(/* webpackChunkName: "about" */ '../views/ImportantTodoPage.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
