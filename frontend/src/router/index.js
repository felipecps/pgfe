import Vue from 'vue'
import VueRouter from 'vue-router'
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
import exemplo_para_form1entrada from '../components/exerciciosEstruturaSequencial/exemplo_para_form1entrada.vue';


Vue.use(VueRouter)

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
