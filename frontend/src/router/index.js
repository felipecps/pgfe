import Vue from 'vue'
import VueRouter from 'vue-router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import Ping from '../views/Ping.vue';
import PaginaInicial from '../views/PaginaInicial.vue';
import EmailAlert from '../views/EmailAlert.vue';
import CalculaCorretagem from '../views/CalculaCorretagem.vue';
import PythonExercicios from '../views/Python.vue';
import estruturaSequencial from '../components/EstruturaSequencial.vue';
import Ex1 from '../components/exerciciosEstruturaSequencial/ex1.vue';
import Ex2 from '../components/exerciciosEstruturaSequencial/ex2.vue';
import Ex3 from '../components/exerciciosEstruturaSequencial/ex3.vue';
import Ex4 from '../components/exerciciosEstruturaSequencial/ex4.vue';
import Ex5 from '../components/exerciciosEstruturaSequencial/ex5.vue';
import Ex6 from '../components/exerciciosEstruturaSequencial/ex6.vue';
import Ex7 from '../components/exerciciosEstruturaSequencial/ex7.vue';
import Ex8 from '../components/exerciciosEstruturaSequencial/ex8.vue';
import Ex9 from '../components/exerciciosEstruturaSequencial/ex9.vue';
import Ex10 from '../components/exerciciosEstruturaSequencial/ex10.vue';
import Ex11 from '../components/exerciciosEstruturaSequencial/ex11.vue';
import Ex12 from '../components/exerciciosEstruturaSequencial/ex12.vue';
import Ex13 from '../components/exerciciosEstruturaSequencial/ex13.vue';
import Ex14 from '../components/exerciciosEstruturaSequencial/ex14.vue';
import Ex15 from '../components/exerciciosEstruturaSequencial/ex15.vue';
import Ex16 from '../components/exerciciosEstruturaSequencial/ex16.vue';
import Ex18 from '../components/exerciciosEstruturaSequencial/ex18.vue';
import exemplo_para_form1entrada from '../components/exerciciosEstruturaSequencial/exemplo_para_form1entrada.vue';


Vue.use(VueRouter)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

const routes = [
  {
    path: '/',
    name: 'PaginaInicial',
        component: PaginaInicial,
  },
  {
    path: '/emailalert',
    name: 'EmailAlert',
    component: EmailAlert,
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/calculacorretagem',
    name: 'CalculaCorretagem',
    component: CalculaCorretagem,
   },
   {
    path: '/python',
    name: 'PythonExercicios',
    component: PythonExercicios,
   },
   {
    path: '/python/estruturaSequencial',
    name: 'EstruturaSequencial',
    component: estruturaSequencial,
    },
    {
        path: '/python/estruturaSequencial/ex1',
        name: 'Ex1',
        component: Ex1,
    },
    {
        path: '/python/estruturaSequencial/ex2',
        name: 'Ex2',
        component: Ex2,
    },
    {
        path: '/python/estruturaSequencial/ex3',
        name: 'Ex3',
        component: Ex3,
    },
    {
        path: '/python/estruturaSequencial/ex4',
        name: 'Ex4',
        component: Ex4,
    },
    {
        path: '/python/estruturaSequencial/ex5',
        name: 'Ex5',
        component: Ex5,
    },
    {
        path: '/python/estruturaSequencial/ex6',
        name: 'Ex6',
        component: Ex6,
    },
    {
        path: '/python/estruturaSequencial/ex7',
        name: 'Ex7',
        component: Ex7,
    },
    {
        path: '/python/estruturaSequencial/ex8',
        name: 'Ex8',
        component: Ex8,
    },
    {
        path: '/python/estruturaSequencial/ex9',
        name: 'Ex9',
        component: Ex9,
    },
    {
        path: '/python/estruturaSequencial/ex10',
        name: 'Ex10',
        component: Ex10,
    },
    {
        path: '/python/estruturaSequencial/ex11',
        name: 'Ex11',
        component: Ex11,
    },
    {
        path: '/python/estruturaSequencial/ex12',
        name: 'Ex12',
        component: Ex12,
    },
    {
        path: '/python/estruturaSequencial/ex13',
        name: 'Ex13',
        component: Ex13,
    },
    {
        path: '/python/estruturaSequencial/ex14',
        name: 'Ex14',
        component: Ex14,
    },
    {
        path: '/python/estruturaSequencial/ex15',
        name: 'Ex15',
        component: Ex15,
    },
    {
        path: '/python/estruturaSequencial/ex16',
        name: 'Ex16',
        component: Ex16,
    },
    {
        path: '/python/estruturaSequencial/ex18',
        name: 'Ex18',
        component: Ex18,
    },
    {
        path: '/python/estruturaSequencial/exemplo_para_form1entrada',
        name: 'exemplo_para_form1entrada',
        component: exemplo_para_form1entrada,
    }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
